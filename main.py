import asyncio
import logging
import logging.handlers
import os

import asyncpg
import discord
from discord.ext import commands
from aiohttp import ClientSession

from BlueShirt.Bot import BlueShirtBot, Translator
from Cogs.test import Test
import config


class Bot(BlueShirtBot):
    async def setup_hook(self):
        guild = discord.Object(id=880594690297188363)

        self.tree.add_command(Test(self), guild=guild)

        await self.tree.sync(guild=guild)

        self.pool = None  # type: ignore

        logging.warning("Successfully synced applications commands")
        logging.warning(f"Connected as {self.user}")
        print("hello")


async def main():
    logger = logging.getLogger('discord')
    logger.setLevel(logging.INFO)

    handler = logging.handlers.RotatingFileHandler(
        filename='discord.log',
        encoding='utf-8',
        maxBytes=32 * 1024 * 1024,  # 32 MiB
        backupCount=5,  # Rotate through 5 files
    )
    dt_fmt = '%Y-%m-%d %H:%M:%S'
    formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    async with Bot(commands.when_mentioned, intents=discord.Intents.default(), application_id=config.application_id) as bot:
        await bot.start(config.client_token)


asyncio.run(main())
