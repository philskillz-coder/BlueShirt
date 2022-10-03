from discord.ext.commands import Bot, GroupCog
import asyncpg


class BlueShirtBot(Bot):
    pool: asyncpg.Pool  # set in setup_hook method


class BetterCog(GroupCog):
    def __init__(self, client: BlueShirtBot):
        self.client = client
