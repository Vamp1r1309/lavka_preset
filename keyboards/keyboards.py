from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config.config import (predmetPrice,
                           zimaPrice,
                           predmetNormalPrice,
                           DICTIONARY_PRESET_ZIMA,
                           DICTIONARY_PRESET_PREDMET,
                           PRICE_SPRING)

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
            InlineKeyboardButton(text='Весенние', callback_data='spring'),
        ],
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
            InlineKeyboardButton(text=f'Набор из 5 пресетов🔥               {predmetNormalPrice[0]}    {zimaPrice[0]}', callback_data='Зимнее combo', ),
        ],
        [
            InlineKeyboardButton(text=f'пресет "NEW YEAR"                       {predmetNormalPrice[1]}    {zimaPrice[1]}', callback_data='newYear'),
        ],
        [
            InlineKeyboardButton(text=f'пресет "MAGIC MOMENT"            {predmetNormalPrice[1]}    {zimaPrice[1]}', callback_data='magicMoment'),
        ],
        [
            InlineKeyboardButton(text=f'пресет "COLD WINTER"                {predmetNormalPrice[1]}    {zimaPrice[1]}', callback_data='coldWinter'),
        ],
        [
            InlineKeyboardButton(text=f'пресет "COZY"                                 {predmetNormalPrice[1]}    {zimaPrice[1]}', callback_data='cozy'),
        ],
        [
            InlineKeyboardButton(text=f'пресет "CHRISTMAS MOOD"       {predmetNormalPrice[1]}    {zimaPrice[1]}', callback_data='christmasMood'),
        ],
    ],
)
keyboard_menu_predmet = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text=f"Набор из 5 пресетов🔥            {predmetNormalPrice[0]}    {predmetPrice[0]}", callback_data='Предметные combo', ),
        ],
        [
            InlineKeyboardButton(text=f'пресет "Retro"                               {predmetNormalPrice[1]}    {predmetPrice[1]}', callback_data='retro'),
        ],
        [
            InlineKeyboardButton(text=f'пресет "Tasty"                               {predmetNormalPrice[1]}    {predmetPrice[1]}', callback_data='tasty'),
        ],
        [
            InlineKeyboardButton(text=f'пресет "Kodak"                              {predmetNormalPrice[1]}    {predmetPrice[1]}', callback_data='kodak'),
        ],
        [
            InlineKeyboardButton(text=f'пресет "Film"                                  {predmetNormalPrice[1]}    {predmetPrice[1]}', callback_data='film'),
        ],
        [
            InlineKeyboardButton(text=f'пресет "Light"                                {predmetNormalPrice[1]}    {predmetPrice[1]}', callback_data='light'),
        ],
    ],
)
keyboard_menu_spring = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text=f"Набор из 5 пресетов🔥       {PRICE_SPRING[0]}", callback_data='Весеннее combo', ),
        ],
        [
            InlineKeyboardButton(text=f'пресет "Crocus"                      {PRICE_SPRING[1]}', callback_data='crocus'),
        ],
        [
            InlineKeyboardButton(text=f'пресет "Lily"                             {PRICE_SPRING[1]}', callback_data='lily'),
        ],
        [
            InlineKeyboardButton(text=f'пресет "Viola"                          {PRICE_SPRING[1]}', callback_data='viola'),
        ],
        [
            InlineKeyboardButton(text=f'пресет "Freesia"                      {PRICE_SPRING[1]}', callback_data='freesia'),
        ],
        [
            InlineKeyboardButton(text=f'пресет "Primula"                     {PRICE_SPRING[1]}', callback_data='primula'),
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
