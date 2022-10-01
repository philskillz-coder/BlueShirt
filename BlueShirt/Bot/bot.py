from discord.ext.commands import Bot, GroupCog
import asyncpg


class Pool(asyncpg.Pool):
    def acquire(self, *, timeout=None) -> asyncpg.Connection:
        return super().acquire(timeout=timeout)


class BlueShirtBot(Bot):
    pool: Pool  # set in setup_hook method


class BetterCog(GroupCog):
    def __init__(self, client: BlueShirtBot):
        self.client = BlueShirtBot
