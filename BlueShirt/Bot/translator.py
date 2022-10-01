from typing import Optional, Dict, List

from discord import app_commands, Locale

from BlueShirt.Bot.bot import BlueShirtBot


class Translator(app_commands.Translator):
    DEFAULT_LANGUAGE = "en-US"

    def __init__(self, client: BlueShirtBot):
        self.client = client
        # noinspection SpellCheckingInspection
        self.translations: Dict[str, Dict[str, str]] = {
            "en-US": {
                "admin.execute_sql.description": "Execute SQL on Database"
            },
            "de": {
                "admin.execute_sql.description": "SQL auf Datenbank ausführen"
            }  # only temporary (should be stored in database)
        }

    async def load(self):
        pass

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

        language_set: dict = self.translations.get(locale.value, self.translations.get(self.DEFAULT_LANGUAGE))
        return language_set.get(locale_str.message, locale_str.message)

        # t_lang = locale.value
        # if locale.value not in self.languages:
        #     # t_lang = self.DEFAULT_LANGUAGE
        #     return None
        #
        # key, extras = locale_str.message, locale_str.extras
        #
        # key_translations = self.translations.get(key)
        # if key_translations is None:
        #     return "no translation found"
        #
        # translation = key_translations.get(t_lang, "error when translating")
        #
        # x = translation.format_map(_AdvancedFormat(**extras))
        # print(x)
        # return x
