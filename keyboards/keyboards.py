from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



keyboardStart = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Перейти к выбору пресета', callback_data='start', ),
        ],
    ]
)

keyboard_menu = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Набор из 5 пресетов🔥', callback_data='combo', ),
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
keyboardReturnMenu = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Вернуться в меню', callback_data='menu'),
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
