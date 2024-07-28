from aiogram import Dispatcher
from aiogram_dialog import setup_dialogs

from src.dialogs import main


def setup(dp: Dispatcher):
    setup_dialogs(dp)
    main.setup(dp)
