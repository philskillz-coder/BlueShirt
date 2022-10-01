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
    description="Administrator tools"
):
    @app_commands.command(
        name="execsql",
        description="Execute SQL on Database",

    )
    @app_commands.describe(query="sql")
    @admin.owner_only()
    async def execute_sql(
            self,
            interaction: BetterInteraction,
            query: str
    ):
        async with self.client.pool.acquire() as cursor:  # todo: custom pool class with acquire typehint: Cursor
            rows = await cursor.fetch(query)
            if not rows:
                await interaction.response.send_message(
                    "No Data",
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


async def setup(client: BlueShirtBot):
    await client.add_cog(AdminCog(client), guild=discord.Object(id=880594690297188363))
