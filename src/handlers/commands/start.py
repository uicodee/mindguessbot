from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram_dialog import DialogManager, StartMode

from src.infrastructure.database.dao import HolderDao
from src.states import MainSG

router = Router()


@router.message(CommandStart())
async def on_cmd_start(message: types.Message, dao: HolderDao, dialog_manager: DialogManager):
    if await dao.user.get_user_by_telegram_id(telegram_id=message.from_user.id) is None:
        await dao.user.add_user(
            telegram_id=message.from_user.id,
            full_name=message.from_user.full_name,
            username=message.from_user.username
        )
    await dialog_manager.start(MainSG.main, mode=StartMode.RESET_STACK)
