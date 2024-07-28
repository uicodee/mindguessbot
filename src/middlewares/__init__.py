from aiogram import Dispatcher
from aiogram.utils.i18n import I18n
from sqlalchemy.orm import sessionmaker

from .database import HolderMiddleware
from .locale import LocaleMiddleware


def setup(dp: Dispatcher, pool: sessionmaker):
    dp.update.middleware(HolderMiddleware(pool=pool))
    dp.update.middleware(LocaleMiddleware(
        I18n(path="src/locales", default_locale="uz", domain="messages"),
        i18n_key="i18n",
        middleware_key="i18n_middleware",
    ))
