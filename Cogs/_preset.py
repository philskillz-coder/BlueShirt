from discord import app_commands

from BlueShirt.Bot.app import BetterInteraction
from BlueShirt.Bot.bot import BlueShirtBot, BetterCog


class Preset(
    BetterCog,
    name="Preset",
    description="Preset GroupCog"
):
    pass


async def setup(client: BlueShirtBot):
    await client.add_cog(Preset(client))
