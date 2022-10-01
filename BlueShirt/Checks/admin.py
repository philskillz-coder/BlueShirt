from discord import app_commands
from BlueShirt.Bot.app import BetterInteraction
from BlueShirt.Bot.app import BetterCheckFailure
from BlueShirt.Checks import better_check


class NotOwner(BetterCheckFailure):
    id = "admin.errors.not_owner"


def owner_only():
    @better_check
    async def actual_check(interaction: BetterInteraction) -> bool:
        if interaction.user.id != 650254133730869258:
            raise NotOwner()

        return True

    return app_commands.check(actual_check)
