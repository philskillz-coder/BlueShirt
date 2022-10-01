from typing import Optional, Dict

from discord import app_commands, Locale

from BlueShirt.Bot.bot import BlueShirtBot


class Translator(app_commands.Translator):
    def __init__(self, client: BlueShirtBot):
        self.client = client
        self.translations: Dict[str, Dict[str, str]] = {}  # {"key": {"language": "translation"}}

    async def load(self):
        async with self.client.pool.acquire() as cursor:
            # noinspection SpellCheckingInspection
            translations = await cursor.fetch("SELECT tkey, tlanguage, ttext FROM translations")
            for key, language, translation in translations:
                if key not in self.translations:
                    self.translations[key] = {}
                self.translations[key][language] = translation

    async def unload(self):
        pass

    async def translate(
            self,
            key: app_commands.locale_str,
            locale: Locale,
            context: app_commands.TranslationContext
    ) -> Optional[str]:
        """
        `locale_str` is the string that is requesting to be translated `locale` is the target language to translate
        to `context` is the origin of this string, eg TranslationContext.command_name, etc. This function must return
        a string (that's been translated), or `None` to signal no available translation available, and will default
        to the original.
        """

        class _AdvancedFormat(dict):
            def __missing__(self, _key: str):
                return '{' + _key + '}'

        print(locale.name, locale.value)

        # noinspection PyUnresolvedReferences
        return self \
            .translations \
            .get(key.message, {}) \
            .get(locale.name, key.message) \
            .format_map(_AdvancedFormat(**key.extras))
