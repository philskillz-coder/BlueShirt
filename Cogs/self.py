from discord import app_commands

from BlueShirt.Bot.app import BetterInteraction
from BlueShirt.Bot.bot import BlueShirtBot, BetterCog


class Self(
    BetterCog,
    name="self",
    description="Your own settings"
):
    pass


async def setup(client: BlueShirtBot):
    await client.add_cog(Self(client))
