import random
from aiogram.utils.i18n import gettext as _

from aiogram.fsm.context import FSMContext


async def get_symbols(state: FSMContext, **kwargs):
    symbols = ["😂️️", "😁", "🥰", "🥳", "🥵", "🤢", "🤡", "🌚", "👋", "💩", "🎲", "🎯", "⚡️", "🌈", "🐶", "🙈"]
    random_symbol = random.choice(symbols)
    symbols_table = []
    table = {i + 1: random.choice(symbols) for i in range(100)}
    for i in range(9, 100, 9):
        table[i] = random_symbol
    for key, value in table.items():
        symbols_table.append(
            (key, value)
        )
    await state.update_data(random_symbol=random_symbol)
    game_text = _(
        "<b>Виртуальный угадыватель мыслей</b>\n\n"
        "Это очень просто, но забавно!\n\n"
        "1. Задумайте любое двухзначное число до 50 (например 44)\n"
        "2. Вычтите из него составляющие его цифры (Например 44 - 4 - 4 = 36)\n"
        "3. Найдите это число в таблице и символ , которому оно соответствует.\n"
        "4. <b>Вообразите мысленно себе этот значок и щелкните по кнопке ниже.</b> В нем появится этот значок."
    )
    button_text = _("Щелкните сюда!")
    return {
        "symbols": symbols_table,
        "game_text": game_text,
        "button_text": button_text,
    }


async def get_symbol(state: FSMContext, **kwargs):
    data = await state.get_data()
    symbol = data.get("random_symbol")
    return {"symbol": symbol}
