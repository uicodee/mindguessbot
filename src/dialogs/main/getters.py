import random

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
    return {"symbols": symbols_table}


async def get_symbol(state: FSMContext, **kwargs):
    data = await state.get_data()
    symbol = data.get("random_symbol")
    return {"symbol": symbol}
