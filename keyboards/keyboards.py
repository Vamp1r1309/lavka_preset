from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config.config import predmetPrice, zimaPrice, predmetNormalPrice

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
            InlineKeyboardButton(text=f'Набор из 5 пресетов🔥             {zimaPrice[0]}', callback_data='Зимнее combo', ),
        ],
        [
            InlineKeyboardButton(text=f'пресет "NEW YEAR"                     {zimaPrice[1]}', callback_data='newYear'),
        ],
        [
            InlineKeyboardButton(text=f'пресет "MAGIC MOMENT"         {zimaPrice[1]}', callback_data='magicMoment'),
        ],
        [
            InlineKeyboardButton(text=f'пресет "COLD WINTER"              {zimaPrice[1]}', callback_data='coldWinter'),
        ],
        [
            InlineKeyboardButton(text=f'пресет "COZY"                               {zimaPrice[1]}', callback_data='cozy'),
        ],
        [
            InlineKeyboardButton(text=f'пресет "CHRISTMAS MOOD"    {zimaPrice[1]}', callback_data='christmasMood'),
        ],
    ],
)
keyboard_menu_predmet = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text=f"Набор из 5 пресетов🔥        {predmetNormalPrice[0]}\t\t" + predmetPrice[0], callback_data='Предметные combo', ),
        ],
        [
            InlineKeyboardButton(text=f'пресет "Retro"                                      {predmetPrice[1]}', callback_data='retro'),
        ],
        [
            InlineKeyboardButton(text=f'пресет "Tasty"                                      {predmetPrice[1]}', callback_data='tasty'),
        ],
        [
            InlineKeyboardButton(text=f'пресет "Kodak"                                     {predmetPrice[1]}', callback_data='kodak'),
        ],
        [
            InlineKeyboardButton(text=f'пресет "Film"                                         {predmetPrice[1]}', callback_data='film'),
        ],
        [
            InlineKeyboardButton(text=f'пресет "Light"                                        {predmetPrice[1]}', callback_data='light'),
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
