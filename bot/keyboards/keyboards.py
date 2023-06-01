from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot.config import (DICTIONARY_PRESET)

keyboardStart = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Перейти к выбору', callback_data='start', ),
        ],
    ]
)
keyboard_categories = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text=f'Пресеты', callback_data='one_combo'),
            InlineKeyboardButton(text=f'Английский', callback_data='Английский Язык'),
        ],
        [
            InlineKeyboardButton(text=f'Методичка по instagram', callback_data='Методичка'),
        ]
    ]
)
keyboard_menu = InlineKeyboardMarkup(
    row_width=2,
    resize_keyboard=True,
    inline_keyboard=[
        [
            InlineKeyboardButton(text=f'МегаПак {len(DICTIONARY_PRESET["Мегапак"]["file_name"])} пресетов🔥🔥🔥             {DICTIONARY_PRESET["Мегапак"]["price"]}₽', callback_data='Мегапак', )
        ],
        [
            InlineKeyboardButton(text=f'Зимний пак {len(DICTIONARY_PRESET["Зимний пак"]["file_name"])} пресетов🔥                     {DICTIONARY_PRESET["Зимний пак"]["price"]}₽', callback_data='Зимний пак', ),
        ],
        [
            InlineKeyboardButton(text=f'Весенний пак {len(DICTIONARY_PRESET["Весенний пак"]["file_name"])} пресетов🔥                 {DICTIONARY_PRESET["Весенний пак"]["price"]}₽', callback_data='Весенний пак'),
        ],
        [
            InlineKeyboardButton(text=f'Летний пак {len(DICTIONARY_PRESET["Летний пак"]["file_name"])} пресетов🔥                      {DICTIONARY_PRESET["Летний пак"]["price"]}₽', callback_data='Летний пак'),
        ],
        [
            InlineKeyboardButton(text=f'Предметный пак {len(DICTIONARY_PRESET["Предметный пак"]["file_name"])} пресетов🔥          {DICTIONARY_PRESET["Предметный пак"]["price"]}₽', callback_data='Предметный пак'),
        ],
    ]
)


keyboardReturnMenu = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Помощь с оплатой', callback_data='helpPAY'),
            InlineKeyboardButton(text='Исп-е пресета', callback_data='settingsPresets'),
        ],
        [
            InlineKeyboardButton(text='Вернуться в меню', callback_data='menu')
        ]
    ]
)
keyboardMenuAndHelp = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Оплатить', pay=True),
        ],
        [
            InlineKeyboardButton(text='Вернуться в меню', callback_data='menu'),
            InlineKeyboardButton(text='Помощь', callback_data='help'),
        ],
    ]
)
