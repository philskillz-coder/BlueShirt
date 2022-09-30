from discord.ext.commands import Bot
import asyncpg


class BlueShirtBot(Bot):
    pool: asyncpg.Pool  # set in setup_hook method
