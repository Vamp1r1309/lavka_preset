from aiogram import types

from aiogram.dispatcher.filters import Command

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from aiogram import types





from keyboards.keyboards import (
                                 keyboardReturnMenu,
                                 keyboardStart,
                                 keyboard_categories,
                                 keyboard_menu_predmet,
                                 keyboard_menu_zima,
                                 keyboard_menu_spring)

from main import bot, dp
from config.config import (MSG,
                           ADMIN_ID,
                           DICTIONARY_PRESET_ZIMA,
                           DICTIONARY_PRESET_PREDMET,
                           DICTIONARY_PRESET_SPRING,)
from heandler.lp_dbUSER import DataBase
from heandler.tg_dbproducts import DataBaseProducts
from heandler.payments import (payments_zima,
                               payments_predmet,
                               payments_spring,
                               check_payment)

dbUser = DataBase('../lavka_preset/lavka_presets.db')
product = DataBaseProducts('../lavka_preset/lavka_presets.db')



#----------------------------------------ADMIN--------------------------------------------------------
@dp.message_handler(Command('message'))
async def message_answer_check_admin(message: types.Message):
    if message.from_user.id in ADMIN_ID:
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
#--------------------------------------------------------Меню пресетов----------------------------------------------------------
@dp.callback_query_handler(text=['start','menu'])
async def show_shop(callback: types.CallbackQuery):
        await callback.message.answer(MSG['preset'], reply_markup=keyboard_categories)
        await callback.answer()

#--------------------------------------------------------Выбор из двух меню-----------------------------------------------------
@dp.callback_query_handler(text=['predmetny'])
async def show_shop(callback: types.CallbackQuery):
        await callback.message.answer(MSG['preset'], reply_markup=keyboard_menu_predmet)
        await callback.answer()

@dp.callback_query_handler(text=['zima'])
async def show_shop(callback: types.CallbackQuery):
        await callback.message.answer(MSG['preset'], reply_markup=keyboard_menu_zima)
        await callback.answer()

@dp.callback_query_handler(text=['spring'])
async def show_shop(callback: types.CallbackQuery):
        await callback.message.answer(MSG['preset'], reply_markup=keyboard_menu_spring)
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
                             reply_markup=keyboardReturnMenu)

@dp.callback_query_handler(text=['help'])
async def help_shop(callback: types.CallbackQuery):
        await callback.message.answer(MSG['help'],
                                      reply_markup=keyboardReturnMenu)
        await callback.answer()
#-------------------------------------------------------------------------------------------------Начало--------------------------------------------------------------------------------------------------------------

@dp.callback_query_handler(text=[txt for txt in DICTIONARY_PRESET_ZIMA])
async def byu_proccess_zima(callback: types.CallbackQuery):

        await dbUser.add_presets(callback.message.chat.id, callback.data)
        payment_deatils = payments_zima(callback.data, callback.message.chat.id)

        paymentsBTN = InlineKeyboardMarkup(
            row_width=2,
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='Оплатить '
                                         + DICTIONARY_PRESET_ZIMA[callback.data]['price_sell'][1] + '   '
                                         + DICTIONARY_PRESET_ZIMA[callback.data]['striketh_text'],
                                         callback_data='pay',
                                         parse_mode='HTML',
                                         url=payment_deatils['confirmation']['confirmation_url']
                                        ),
                ],
                [
                    InlineKeyboardButton(text='Вернуться в меню', callback_data='menu'),
                    InlineKeyboardButton(text='Помощь', callback_data='help'),
                ],
            ]
        )
        await bot.send_photo(callback.message.chat.id,
                            photo=DICTIONARY_PRESET_ZIMA[callback.data]['photo_url'],
                            caption=DICTIONARY_PRESET_ZIMA[callback.data]['name'] + ', отличный выбор😉',
                            reply_markup=paymentsBTN, parse_mode='HTML')
        await callback.answer()

        if await check_payment(payment_deatils['id'], callback.message.chat.id):
            data = await dbUser.check_presets(callback.message.chat.id)
            await bot.send_message(
                                callback.message.chat.id,
                                MSG['successful'].format(DICTIONARY_PRESET_ZIMA[callback.data]['price_sell'][1])
                                )
            if type(DICTIONARY_PRESET_ZIMA[data]['file_name']) == list:
                res = DICTIONARY_PRESET_ZIMA[data]['file_name']
                for item in res:
                    await bot.send_document(
                                            callback.message.chat.id,
                                            document=item
                                        )
            else:
                await bot.send_document(
                                        callback.message.chat.id,
                                        document=DICTIONARY_PRESET_ZIMA[data]['file_name']
                                    )
        else:
            await bot.send_message(callback.message.chat.id, text=MSG['exitText'])


@dp.callback_query_handler(text=[txt for txt in DICTIONARY_PRESET_PREDMET])
async def byu_proccess_predmet(callback: types.CallbackQuery):

        await dbUser.add_presets(callback.message.chat.id, callback.data)
        payment_deatils = payments_predmet(callback.data, callback.message.chat.id)

        paymentsBTN = InlineKeyboardMarkup(
            row_width=2,
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='Оплатить '
                                         + DICTIONARY_PRESET_PREDMET[callback.data]['price_sell'][0] + '₽',
                                         callback_data='pay',
                                         parse_mode='HTML',
                                         url=payment_deatils['confirmation']['confirmation_url']
                                        ),
                ],
                [
                    InlineKeyboardButton(text='Вернуться в меню', callback_data='menu'),
                    InlineKeyboardButton(text='Помощь', callback_data='help'),
                ],
            ]
        )
        await bot.send_photo(chat_id=callback.message.chat.id,
                            photo=DICTIONARY_PRESET_PREDMET[callback.data]['photo_url'],
                            caption=DICTIONARY_PRESET_PREDMET[callback.data]['name'] + ', отличный выбор😉',
                            reply_markup=paymentsBTN, parse_mode='HTML')
        await callback.answer()

        if await check_payment(payment_deatils['id'], callback.message.chat.id):
            data = await dbUser.check_presets(callback.message.chat.id)
            await bot.send_message(
                                callback.message.chat.id,
                                MSG['successful'].format(DICTIONARY_PRESET_PREDMET[callback.data]['price_sell'][0] + '₽')
                                )
            if type(DICTIONARY_PRESET_PREDMET[data]['file_name']) == list:
                res = DICTIONARY_PRESET_PREDMET[data]['file_name']
                for item in res:
                    await bot.send_document(
                                            callback.message.chat.id,
                                            document=item
                                        )
            else:
                await bot.send_document(
                                        callback.message.chat.id,
                                        document=DICTIONARY_PRESET_PREDMET[data]['file_name']
                                    )
        else:
            await bot.send_message(callback.message.chat.id, text=MSG['exitText'])


@dp.callback_query_handler(text=[txt for txt in DICTIONARY_PRESET_SPRING])
async def byu_proccess_spring(callback: types.CallbackQuery):

        await dbUser.add_presets(callback.message.chat.id, callback.data)
        payment_deatils = payments_spring(callback.data, callback.message.chat.id)

        paymentsBTN = InlineKeyboardMarkup(
            row_width=2,
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='Оплатить '
                                         + DICTIONARY_PRESET_SPRING[callback.data]['price_sell'][0] + '₽',
                                         callback_data='pay',
                                         parse_mode='HTML',
                                         url=payment_deatils['confirmation']['confirmation_url']
                                        ),
                ],
                [
                    InlineKeyboardButton(text='Вернуться в меню', callback_data='menu'),
                    InlineKeyboardButton(text='Помощь', callback_data='help'),
                ],
            ]
        )
        await bot.send_photo(chat_id=callback.message.chat.id,
                            photo=DICTIONARY_PRESET_SPRING[callback.data]['photo_url'],
                            caption=DICTIONARY_PRESET_SPRING[callback.data]['name'] + ', отличный выбор😉',
                            reply_markup=paymentsBTN, parse_mode='HTML')
        await callback.answer()

        if await check_payment(payment_deatils['id'], callback.message.chat.id):
            data = await dbUser.check_presets(callback.message.chat.id)
            await bot.send_message(
                                callback.message.chat.id,
                                MSG['successful'].format(DICTIONARY_PRESET_SPRING[callback.data]['price_sell'][0] + '₽')
                                )
            if type(DICTIONARY_PRESET_SPRING[data]['file_name']) == list:
                res = DICTIONARY_PRESET_SPRING[data]['file_name']
                for item in res:
                    await bot.send_document(
                                            callback.message.chat.id,
                                            document=item
                                        )
            else:
                await bot.send_document(
                                        callback.message.chat.id,
                                        document=DICTIONARY_PRESET_SPRING[data]['file_name']
                                    )
        else:
            await bot.send_message(callback.message.chat.id, text=MSG['exitText'])
