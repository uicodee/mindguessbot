import operator

from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import ScrollingGroup, Select, Button, Back
from aiogram_dialog.widgets.text import Format, Const

from .getters import get_symbols, get_symbol
from .handlers import on_guess_clicked
from src.states import MainSG

dialog = Dialog(
    Window(
        Const(
            "<b>Виртуальный угадыватель мыслей</b>\n\n"
            "Это очень просто, но забавно!\n\n"
            "1. Задумайте любое двухзначное число до 50 (например 44)\n"
            "2. Вычтите из него составляющие его цифры (Например 44 - 4 - 4 = 36)\n"
            "3. Найдите это число в таблице и символ , которому оно соответствует.\n"
            "4. <b>Вообразите мысленно себе этот значок и щелкните по кнопке ниже.</b> В нем появится этот значок."
        ),
        Button(
            Const("Щелкните сюда!"),
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
