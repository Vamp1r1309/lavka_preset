from aiogram.dispatcher.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, BotCommand
from aiogram import types
from aiogram.dispatcher.filters import CommandHelp
from run import logger
import sqlite3
from bot.baseDir import DataBase
from bot.keyboards.keyboards import (
                                 keyboardReturnMenu,
                                 keyboardStart,
                                 keyboard_categories,
                                 keyboard_menu)
from run import bot, dp
from bot.config import (MSG,
                        ADMIN_ID,
                        DICTIONARY_PRESET)
from bot.payments.payments import (ym_payments,
                                   check_payment)


dbUser = DataBase('../lavka_preset/lavka_presets.db')

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

async def set_default_commands(bot: bot):
    return await bot.set_my_commands(
        commands=[
            BotCommand('start', 'Запуск бота'),
            BotCommand('help', 'Помощь')
        ]
    )
@dp.message_handler(commands='start')
async def show_shop(message: types.Message):
    try:
        await dbUser.add_users(message.chat.id, message.chat.first_name)
        await set_default_commands(bot)
        logger.info('Пользователь добавлен в базу данных')
    except sqlite3.IntegrityError as ex:
        logger.debug(f'Пользователь уже добавлен в базу данных')
    except Exception as ex:
        logger.error(f'Произошла ошибка при добавление в базу данных. Ошибка {ex}')
    finally:
        await message.answer(f"{MSG['start']}", reply_markup=keyboardStart)
#--------------------------------------------------------Меню пресетов----------------------------------------------------------
@dp.callback_query_handler(text=['start','menu'])
async def show_shop(callback: types.CallbackQuery):
    try:
        await callback.message.answer(MSG['preset'], reply_markup=keyboard_categories)
        logger.info('Пользователь перешел на уровень категорий')
        await callback.answer()
    except Exception:
        logger.error('Ошибка перехода в меню категорий')

#--------------------------------------------------------Выбор из двух меню-----------------------------------------------------
@dp.callback_query_handler(text=['one_combo'])
async def show_shop(callback: types.CallbackQuery):
    try:
        await callback.message.answer(MSG['preset'], reply_markup=keyboard_menu)
        logger.info('Пользователь перешел к выбору пресетов или английского')
        await callback.answer()
    except Exception:
        logger.error('Ошибка перехода к выбору пресетов или английского')



@dp.callback_query_handler(text=['helpPAY'])
async def helpPAY(callback: types.CallbackQuery):
    try:
        await bot.send_message(callback.message.chat.id,
                               MSG['helpPAY'],
                               reply_markup=keyboardStart)
        logger.info('Пользователь воспользовался помощью при оплате')
        await callback.answer()
    except Exception:
        logger.error('Ошибка при использование помощи при оплате')

@dp.callback_query_handler(text=['settingsPresets'])
async def helpPAY(callback: types.CallbackQuery):
    try:
        await bot.send_video(callback.message.chat.id,
                             caption=MSG['settingsPresets'],
                             video=MSG['video'],
                             reply_markup=keyboardStart)
        logger.info('Пользователь воспользовался помощью при выборе пресета')
        await callback.answer()
    except Exception:
        logger.error('Ошибка при использование помощи при выборе пресета')

@dp.message_handler(CommandHelp())
async def help_shop(message: types.Message):
    try:
        await message.answer(MSG['help'],
                             reply_markup=keyboardReturnMenu)
        logger.info('Пользователь зашел в меню')
    except Exception:
        logger.error('Ошибка при использование помощи')

@dp.callback_query_handler(text='help')
async def help_shop(callback: types.CallbackQuery):
    try:
        await callback.message.answer(MSG['help'],
                                      reply_markup=keyboardReturnMenu)
        logger.info('Пользователь зашел в меню')
        await callback.answer()
    except Exception:
        logger.error('Ошибка при использование помощи')
#-------------------------------------------------------------------------------------------------Начало---------------------------------------__------------------------------------------------------------------

@dp.callback_query_handler(text=[txt for txt in DICTIONARY_PRESET])
async def byu_proccess_sell(callback: types.CallbackQuery):
    try:
        await dbUser.add_presets(callback.message.chat.id, callback.data)
        payment_deatils = ym_payments(callback.data, callback.message.chat.id)

        paymentsBTN = InlineKeyboardMarkup(
            row_width=2,
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='Оплатить '
                                         + DICTIONARY_PRESET[callback.data]['price'] + '₽',
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
                            photo=DICTIONARY_PRESET[callback.data]['photo_url'],
                            caption=DICTIONARY_PRESET[callback.data]['name'] + ', отличный выбор😉',
                            reply_markup=paymentsBTN, parse_mode='HTML')
        logger.info(f'Пользователь проходит процедуру оплаты товара {DICTIONARY_PRESET[callback.data]["name"]}')
        await callback.answer()
        tmp = 0
        if await check_payment(payment_deatils['id'], callback.message.chat.id):
            data = await dbUser.check_presets(callback.message.chat.id)
            await bot.send_message(
                                callback.message.chat.id,
                                MSG['successful'].format(DICTIONARY_PRESET[callback.data]['price'])
                                )
            res = DICTIONARY_PRESET[data]['file_name']
            for item in res:
                await bot.send_document(
                                        callback.message.chat.id,
                                        document=item
                                        )
            logger.info('Пользователь получил свои прессеты')
        else:
            tmp += 1
            if tmp < 2:
                await bot.send_message(callback.message.chat.id, text=MSG['exitText'])
                logger.info('Пользователь отказался от покупки')
    except Exception:
        logger.error('При попытки оплаты произошла ошибка!!!')
