from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


keyboardStart = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Перейти к выбору пресета', callback_data='start', ),
        ],
    ]
)
keyboard_categories = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Зимние', callback_data='zima'),
            InlineKeyboardButton(text='Предметные', callback_data='predmetny'),
        ],
    ]
)
keyboard_menu_zima = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Набор из 5 пресетов🔥', callback_data='Зимнее combo', ),
        ],
        [
            InlineKeyboardButton(text='пресет "NEW YEAR"', callback_data='newYear'),
        ],
        [
            InlineKeyboardButton(text='пресет "MAGIC MOMENT"', callback_data='magicMoment'),
        ],
        [
            InlineKeyboardButton(text='пресет "COLD WINTER"', callback_data='coldWinter'),
        ],
        [
            InlineKeyboardButton(text='пресет "COZY"', callback_data='cozy'),
        ],
        [
            InlineKeyboardButton(text='пресет "CHRISTMAS MOOD"', callback_data='christmasMood'),
        ],
    ],
)
keyboard_menu_predmet = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Набор из 5 пресетов🔥', callback_data='Предметные combo', ),
        ],
        [
            InlineKeyboardButton(text='пресет "Retro"', callback_data='retro'),
        ],
        [
            InlineKeyboardButton(text='пресет "Tasty"', callback_data='tasty'),
        ],
        [
            InlineKeyboardButton(text='пресет "Kodak"', callback_data='kodak'),
        ],
        [
            InlineKeyboardButton(text='пресет "Film"', callback_data='film'),
        ],
        [
            InlineKeyboardButton(text='пресет "Light"', callback_data='light'),
        ],
    ],
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
