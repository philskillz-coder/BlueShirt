from typing import List

import discord
from discord import app_commands

from BlueShirt.Bot import BetterAppCommandGroup, BetterInteraction


class Test(BetterAppCommandGroup):
    @app_commands.command(
        name="test",
        description="A test command"
    )
    async def test(self, interaction: BetterInteraction):
        await interaction.response.send_message(
            content="hello"
        )
