import discord
from discord import app_commands
from discord.app_commands import locale_str as _T

from BlueShirt.Bot.app import BetterInteraction
from BlueShirt.Bot.bot import BlueShirtBot, BetterCog
from BlueShirt.Checks import admin

from tabulate import tabulate


class AdminCog(
    BetterCog,
    name="administrator",
    description="admin.description"
):
    @app_commands.command(
        name="execsql",
        description="admin.execute_sql.description",
    )
    @app_commands.describe(query="admin.execute_sql.query")
    @admin.owner_only()
    async def execute_sql(
            self,
            interaction: BetterInteraction,
            query: str
    ):

        async with self.client.pool.acquire() as cursor:
            rows = await cursor.fetch(query)
            if not rows:
                await interaction.response.send_message(
                    "The query returned no results",
                    ephemeral=True
                )

            # noinspection SpellCheckingInspection
            data = tabulate(
                headers=list(dict(rows[0]).keys()),
                tablefmt="orgtbl",
                tabular_data=[tuple(r) for r in rows]
            )

            await interaction.response.send_message(
                f"```\n{data}```",
                ephemeral=True
            )

    @app_commands.command(
        name="dispatch_error"
    )
    @admin.owner_only()
    async def error(self, interaction: BetterInteraction):
        raise discord.DiscordException("Error")

    @app_commands.command(
        name="dispatch_guild_join"
    )
    @admin.owner_only()
    async def dispatch_guild_join(self, interaction: BetterInteraction):
        self.client.dispatch("guild_join", guild=interaction.guild)
        await interaction.response.send_message("dispatched")

async def setup(client: BlueShirtBot):
    await client.add_cog(AdminCog(client), guild=discord.Object(id=880594690297188363))
