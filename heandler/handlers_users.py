from aiogram import types
from aiogram.types.message import ContentType
from aiogram.dispatcher.filters import Command


from aiogram import types





from keyboards.keyboards import keyboard_menu, keyboardMenuAndHelp, keyboardReturnMenu, keyboardStart

from main import bot, dp
from config.config import MSG, DICTIONARY_PRESET, PAYMENT_TOKEN
from heandler.lp_dbUSER import DataBase
from heandler.tg_dbproducts import DataBaseProducts
from FSM.shop import Shop

dbUser = DataBase('lavka_preset/lavka_presets.db')
product = DataBaseProducts('lavka_preset/lavka_presets.db')


price = {
    'combo': [types.LabeledPrice(label='Пак из 5 пресетов', amount=87*100),],
    'coldWinter': [types.LabeledPrice(label='Пресет "COLDWINTER"', amount=87*100)],
    'cozy': [types.LabeledPrice(label='Пресет "COZY"', amount=87*100)],
    'christmasMood': [types.LabeledPrice(label='CRISTMAS MODOD"', amount=87*100)],
    'magicMoment': [types.LabeledPrice(label='Пресет "MAGIC MOMENT"', amount=87*100)],
    'newYear': [types.LabeledPrice(label='Пресет "NEW YEAR"', amount=87*100)],
}

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
    await bot.delete_message(
                            chat_id=callback.from_user.id,
                            message_id=callback.message.message_id
                            )
    await callback.message.answer(MSG['preset'], reply_markup=keyboard_menu)



@dp.message_handler(Command('help'))
async def help_shop(message: types.Message):
    await message.answer(MSG['help'],
                        reply_markup=keyboardReturnMenu
                        )

@dp.callback_query_handler(text=['help'])
async def help_shop(callback: types.CallbackQuery):
    await bot.delete_message(chat_id=callback.from_user.id,
                            message_id=callback.message.message_id
                            )
    await callback.message.answer(MSG['help'],
                                 reply_markup=keyboardReturnMenu
                                 )


# Оплата
@dp.callback_query_handler(text=[item[0] for item in DICTIONARY_PRESET.items()])
async def buy_process(callback: types.CallbackQuery):
    await dbUser.add_presets(callback.message.chat.id, callback.data)
    await bot.delete_message(chat_id=callback.from_user.id,
                            message_id=callback.message.message_id
                            )
    item = callback.data
    await bot.send_invoice(
                            callback.message.chat.id,
                            title='Пресет ' + DICTIONARY_PRESET[item]['name'],
                            description=DICTIONARY_PRESET[item]['name'] + ', отличный выбор😉',
                            provider_token=PAYMENT_TOKEN,
                            currency='rub',
                            photo_url=DICTIONARY_PRESET[item]['photo_url'],
                            photo_height=DICTIONARY_PRESET[item]['photo_height'],
                            photo_width=DICTIONARY_PRESET[item]['photo_width'],
                            photo_size=DICTIONARY_PRESET[item]['photo_size'],
                            is_flexible=False,
                            prices=price[item],
                            start_parameter='example',
                            payload='some_invoise',
                            reply_markup=keyboardMenuAndHelp
                        )
    await callback.answer()

@dp.pre_checkout_query_handler(lambda query: True)
async def checkout_procces(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(
                                        pre_checkout_query.id,
                                        ok=True
                                       )



@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def succesful_payment(message: types.Message):
    data = await dbUser.check_presets(message.chat.id)
    await bot.send_message(
                           message.chat.id,
                           MSG['successful'].format(message.successful_payment.total_amount // 100)
                          )

    if type(DICTIONARY_PRESET[data[0]]['file_name']) == list:
        res = DICTIONARY_PRESET[data[0]]['file_name']
        for item in res:
            await bot.send_document(
                                    message.chat.id,
                                    document=item
                                   )
    else:
        await bot.send_document(
                                message.chat.id,
                                document=DICTIONARY_PRESET[data[0]]['file_name']
                               )