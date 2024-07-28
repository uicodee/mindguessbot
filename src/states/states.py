from aiogram.fsm.state import StatesGroup, State


class MainSG(StatesGroup):

    main = State()
    guess = State()
