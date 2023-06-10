import discord

from BlueShirt.Bot.app import BetterInteraction
from BlueShirt.Bot.bot import BlueShirtBot, BetterCog


class Guild(
    BetterCog,
    name="guild",
    description="guild.description"
):
    @BetterCog.listener()
    async def on_guild_join(self, guild: discord.Guild):
        print(f"Guild Join: {guild.name}")
        async with self.client.pool.acquire() as cursor:
            guild_exists, = await cursor.fetchrow("SELECT EXISTS(SELECT 1 FROM guilds WHERE guild_id = $1);", guild.id)
            if not guild_exists:
                await cursor.execute("INSERT INTO guilds(guild_id) VALUES($1);", guild.id)

                for channel in guild.text_channels:
                    if channel.permissions_for(guild.default_role).send_messages:
                        embed = discord.Embed(title="Thanks for adding BlueShirt to your guild")
                        # error does not print
                        # under here
                        embed.set_thumbnail(url=guild.icon.url)
                        embed.description = "Start the configuration process with `/guild autoconfigure`\n" \
                                                "You can also do all settings manually. For a list of settings do " \
                                                "`/help settings`"
                        embed.set_footer(text="With Confidence: BlueShirt", icon_url=self.client.user.avatar.url)
                        # above here
                        await channel.send(
                            embed=embed
                        )
                        print(f"message sent in {channel.name}")
                        break


async def setup(client: BlueShirtBot):
    await client.add_cog(Guild(client), guild=discord.Object(id=880594690297188363))
