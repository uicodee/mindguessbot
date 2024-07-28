from typing import Dict, Any

from aiogram import types
from aiogram.utils.i18n import I18nMiddleware


class LocaleMiddleware(I18nMiddleware):
    async def get_locale(self, event: types.Update, data: Dict[str, Any]) -> str:
        if event.message is not None:
            event = event.message
        elif event.callback_query is not None:
            event = event.callback_query
        return event.from_user.language_code
