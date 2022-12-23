from aiogram import types

from aiogram.dispatcher.filters import Command

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from aiogram import types





from keyboards.keyboards import keyboard_menu, keyboardReturnMenu, keyboardStart

from main import bot, dp
from config.config import MSG, DICTIONARY_PRESET, ADMIN_ID
from heandler.lp_dbUSER import DataBase
from heandler.tg_dbproducts import DataBaseProducts
from heandler.payments import payments, check_payment

dbUser = DataBase('../lavka_preset/lavka_presets.db')
product = DataBaseProducts('../lavka_preset/lavka_presets.db')



#----------------------------------------ADMIN--------------------------------------------------------
@dp.message_handler(Command('message'))
async def message_answer_check_admin(message: types.Message):
    if message.from_user.id in ADMIN_ID:
        # await bot.send_message(message.chat.id, 'Введите свое сообщение ниже')
        id_users = await dbUser.import_id_users()
        for item in id_users:
                try:
                    if item[0] not in ADMIN_ID:
                        await bot.send_message(chat_id=item[0], text=message.text[9:])
                        if int(item[1]) != 1:
                            await dbUser.activeusers(True, item[0])
                except:
                    await dbUser.activeusers(False, item[0])
        await bot.send_message(message.from_user.id, MSG['successfulMessage'])
#----------------------------------------USERS--------------------------------------------------------
@dp.message_handler(Command('start'))
async def show_shop(message: types.Message):
    try:
        await dbUser.add_users(message.chat.id, message.chat.first_name)
    except:
        pass
    finally:
        await message.answer(MSG['start'], reply_markup=keyboardStart)

@dp.callback_query_handler(text=['start','menu'])
async def show_shop(callback: types.CallbackQuery):
        await callback.message.answer(MSG['preset'], reply_markup=keyboard_menu)
        await callback.answer()

@dp.callback_query_handler(text=['helpPAY'])
async def helpPAY(callback: types.CallbackQuery):
        await bot.send_message(callback.message.chat.id,
                               MSG['helpPAY'],
                               reply_markup=keyboardStart)
        await callback.answer()

@dp.callback_query_handler(text=['settingsPresets'])
async def helpPAY(callback: types.CallbackQuery):
        await bot.send_video(callback.message.chat.id,
                             caption=MSG['settingsPresets'],
                             video=MSG['video'],
                             reply_markup=keyboardStart)
        await callback.answer()

@dp.message_handler(Command('help'))
async def help_shop(message: types.Message):
        await message.answer(MSG['help'],
                            reply_markup=keyboardReturnMenu
                            )

@dp.callback_query_handler(text=['help'])
async def help_shop(callback: types.CallbackQuery):
        await callback.message.answer(MSG['help'],
                                     reply_markup=keyboardReturnMenu
                                     )
        await callback.answer()
#-------------------------------------------------------------------------------------------------Начало--------------------------------------------------------------------------------------------------------------

@dp.callback_query_handler(text=['combo', 'newYear', 'magicMoment', 'coldWinter', 'cozy', 'christmasMood',])
async def byu_proccess(callback: types.CallbackQuery):

        await dbUser.add_presets(callback.message.chat.id, callback.data)
        payment_deatils = payments(callback.data, callback.message.chat.id)

        paymentsBTN = InlineKeyboardMarkup(
            row_width=2,
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='Оплатить ' + DICTIONARY_PRESET[callback.data]['price'] + ' р.', callback_data='pay', url=payment_deatils['confirmation']['confirmation_url']),
                ],
                [
                    InlineKeyboardButton(text='Вернуться в меню', callback_data='menu'),
                    InlineKeyboardButton(text='Помощь', callback_data='help'),
                ],
            ]
        )
        await bot.send_photo(callback.message.chat.id,
                            photo=DICTIONARY_PRESET[callback.data]['photo_url'],
                            caption=DICTIONARY_PRESET[callback.data]['name'] + ', отличный выбор😉',
                            reply_markup=paymentsBTN)
        await callback.answer()

        if await check_payment(payment_deatils['id'], callback.message.chat.id):
            data = await dbUser.check_presets(callback.message.chat.id)
            await bot.send_message(
                                callback.message.chat.id,
                                MSG['successful'].format(DICTIONARY_PRESET[callback.data]['price'])
                                )
            if type(DICTIONARY_PRESET[data[0]]['file_name']) == list:
                res = DICTIONARY_PRESET[data[0]]['file_name']
                for item in res:
                    await bot.send_document(
                                            callback.message.chat.id,
                                            document=item
                                        )
            else:
                await bot.send_document(
                                        callback.message.chat.id,
                                        document=DICTIONARY_PRESET[data[0]]['file_name']
                                    )

        else:
            await bot.send_message(callback.message.chat.id, text=MSG['exitText'])
