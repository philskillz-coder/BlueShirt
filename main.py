import asyncio
import logging
import logging.handlers

import asyncpg
import discord
from discord.ext import commands

import config
from BlueShirt.Bot.bot import BlueShirtBot
from BlueShirt.Bot.translator import Translator


class Bot(BlueShirtBot):
    async def setup_hook(self):
        guild = discord.Object(id=880594690297188363)

        await self.load_extension("Cogs.admin")

        await self.tree.sync(guild=guild)

        self.pool = await asyncpg.create_pool(
            **config.database_params
        )

        await self.tree.set_translator(Translator(self))

        print("Successfully synced applications commands")
        print(f"Connected as {self.user}")


async def main():
    async with Bot(
            command_prefix=commands.when_mentioned,
            intents=discord.Intents.default(),
            application_id=config.application_id
    ) as bot:
        await bot.start(config.client_token)


asyncio.run(main())
