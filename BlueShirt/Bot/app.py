from __future__ import annotations

import discord
from discord import app_commands
from typing import TYPE_CHECKING, Optional, Dict, Any

if TYPE_CHECKING:
    from BlueShirt.Bot.bot import BlueShirtBot


class BetterAppCommandGroup(app_commands.Group):
    def __init__(
            self,
            client: BlueShirtBot
    ):
        super().__init__()
        self.client: BlueShirtBot = client


class BetterInteraction(discord.Interaction):
    response: discord.InteractionResponse


class BetterCheckFailure(app_commands.CheckFailure):
    id: str

    def __init__(self, data: Optional[Dict[str, Any]] = None):
        self.data: Dict[str, Any] = data or {}
