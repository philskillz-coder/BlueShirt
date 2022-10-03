import asyncio

import asyncpg
import discord
from discord.ext import commands
from discord import app_commands

import config
from BlueShirt.Bot.bot import BlueShirtBot
from BlueShirt.Bot.translator import Translator
from BlueShirt.Bot.app import BetterInteraction


# todo: load, unload, reload with sync command

class Bot(BlueShirtBot):
    async def setup_hook(self):
        self.pool = await asyncpg.create_pool(
            **config.database_params
        )

        await self.load_extension("Cogs.admin")
        await self.load_extension("Cogs.guild")
        await self.load_extension("Cogs.self")

        await self.tree.set_translator(Translator(self))

        guild = discord.Object(id=880594690297188363)

        self.tree.on_error = self.tree_error()
        await self.tree.sync(guild=guild)

        print("Successfully synced applications commands")
        print(f"Connected as {self.user}")

    async def on_error(self, event_method: str, /, *args, **kwargs) -> None:
        print(event_method, args, kwargs)

    # noinspection PyMethodMayBeStatic
    def tree_error(self):
        async def on_tree_error(interaction: BetterInteraction, error: app_commands.AppCommandError):
            print(f"{interaction.user} caused {repr(error)}")

        return on_tree_error


async def main():
    async with Bot(
            command_prefix=commands.when_mentioned,
            intents=discord.Intents.default(),
            application_id=config.application_id
    ) as bot:
        discord.utils.setup_logging()
        await bot.start(config.client_token)


asyncio.run(main())
