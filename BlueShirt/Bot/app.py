from __future__ import annotations

import discord
from discord import app_commands
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from BlueShirt.Bot import BlueShirtBot


class BetterAppCommandGroup(app_commands.Group):
    def __init__(
            self,
            client: BlueShirtBot
    ):
        super().__init__()
        self.client: BlueShirtBot = client


class BetterInteraction(discord.Interaction):
    response: discord.InteractionResponse
