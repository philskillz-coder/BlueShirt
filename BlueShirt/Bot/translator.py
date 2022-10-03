from typing import Optional, Dict, List

from discord import app_commands, Locale

from BlueShirt.Bot.bot import BlueShirtBot

import json
import aiofiles


class Translator(app_commands.Translator):
    DEFAULT_LOCALE = "en-US"
    SUPPORTED_LOCALES = [
        "en-US",
        "de"
    ]

    def __init__(self, client: BlueShirtBot):
        self.client = client
        self.translations: Dict[str, Dict[str, str]] = {}

    async def load(self):
        for locale in self.SUPPORTED_LOCALES:
            async with aiofiles.open(f"Translations/{locale}.json", "rb") as f:
                data: Dict[str, str] = json.loads((await f.read()).decode())
                self.translations[locale] = data

    async def unload(self):
        pass

    # noinspection PyUnresolvedReferences
    async def translate(
            self,
            locale_str: app_commands.locale_str,
            locale: Locale,
            context: app_commands.TranslationContext
    ) -> Optional[str]:
        class _AdvancedFormat(dict):
            def __missing__(self, _key: str):
                return '{' + _key + '}'

        locale_set: dict = self.translations.get(locale.value, self.translations.get(self.DEFAULT_LOCALE))
        translation = locale_set.get(locale_str.message, locale_str.message)
        translation = translation.format_map(_AdvancedFormat(**locale_str.extras))

        return translation
