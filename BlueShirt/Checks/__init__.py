from typing import Coroutine, Callable, Any
from BlueShirt.Bot.app import BetterInteraction
from discord import Interaction
from functools import wraps


def better_check(
        method: Callable[[BetterInteraction], Coroutine[Any, Any, bool]]
) -> Callable[[Interaction], Coroutine[Any, Any, bool]]:
    @wraps(method)
    async def _method(i: Interaction):
        # noinspection PyTypeChecker
        return await method(i)

    return _method
