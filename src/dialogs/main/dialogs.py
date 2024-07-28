import operator

from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import ScrollingGroup, Select, Button, Back
from aiogram_dialog.widgets.text import Format, Const

from .getters import get_symbols, get_symbol
from .handlers import on_guess_clicked
from src.states import MainSG

dialog = Dialog(
    Window(
        Format("{game_text}"),
        Button(
            Format("{button_text}"),
            id="guess",
            on_click=on_guess_clicked
        ),
        ScrollingGroup(
            Select(
                Format("{item[0]} {item[1]}"),
                id="select_symbol",
                item_id_getter=operator.itemgetter(1),
                items="symbols",
                # on_click=on_group_selected,
            ),
            id="numbers",
            width=5,
            height=10,
            hide_pager=True
        ),
        getter=get_symbols,
        state=MainSG.main
    ),
    Window(
        Format("{symbol}"),
        Back(Const("🔃 Повторить")),
        getter=get_symbol,
        state=MainSG.guess
    )
)
