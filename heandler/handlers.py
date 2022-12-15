from aiogram import types
from aiogram.types.message import ContentType
from aiogram.dispatcher.filters import Command


from aiogram import types



from aiogram.dispatcher import FSMContext


from keyboards.keyboards import keyboard_menu, keyboardMenuAndHelp, keyboardReturnMenu, keyboardStart

from main import bot, dp
from config.config import MSG, DICTIONARY_PRESET, PAYMENT_TOKEN
from FSM.shop import Shop




price = {
    'combo': [types.LabeledPrice(label='Пак из 5 пресетов', amount=499*100),],
    'coldWinter': [types.LabeledPrice(label='Пресет "COLDWINTER"', amount=199*100)],
    'cozy': [types.LabeledPrice(label='Пресет "COZY"', amount=199*100)],
    'christmasMood': [types.LabeledPrice(label='CRISTMAS MODOD"', amount=199*100)],
    'magicMoment': [types.LabeledPrice(label='Пресет "MAGIC MOMENT"', amount=199*100)],
    'newYear': [types.LabeledPrice(label='Пресет "NEW YEAR"', amount=199*100)],
}

@dp.message_handler(Command('start'))
async def show_shop(message: types.Message):
    await message.answer(MSG['start'], reply_markup=keyboardStart)

@dp.callback_query_handler(text=['menu', 'start'], state='*')
async def show_shop(callback: types.CallbackQuery):
    await bot.delete_message(
                            chat_id=callback.from_user.id,
                            message_id=callback.message.message_id
                            )
    await callback.message.answer(MSG['preset'], reply_markup=keyboard_menu)
    await Shop.step1.set()


@dp.message_handler(Command('help'), state='*')
async def help_shop(message: types.Message, state: FSMContext):
    await message.answer(MSG['help'],
                        reply_markup=keyboardReturnMenu
                        )
    await state.finish()

@dp.callback_query_handler(text=['help'], state="*")
async def help_shop(callback: types.CallbackQuery, state: FSMContext):
    await bot.delete_message(chat_id=callback.from_user.id,
                            message_id=callback.message.message_id
                            )
    await callback.message.answer(MSG['help'],
                                 reply_markup=keyboardReturnMenu
                                 )
    await state.finish()

# Оплата
@dp.callback_query_handler(state=Shop.step1)
async def buy_process(callback: types.CallbackQuery, state: FSMContext):
    await bot.delete_message(chat_id=callback.from_user.id,
                            message_id=callback.message.message_id
                            )
    item = callback.data
    await state.update_data(
        {
            'item': item
        }
    )
    await bot.send_invoice(
                            callback.message.chat.id,
                            title='Пресет ' + DICTIONARY_PRESET[item]['name'],
                            description=DICTIONARY_PRESET[item]['name'] + ', отличный выбор😉',
                            provider_token='381764678:TEST:46558',
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
    await Shop.next()

@dp.pre_checkout_query_handler(lambda query: True, state=Shop.step2)
async def checkout_procces(pre_checkout_query: types.PreCheckoutQuery, state: FSMContext):
    await bot.answer_pre_checkout_query(
                                        pre_checkout_query.id,
                                        ok=True
                                       )
    await Shop.next()

@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT, state=Shop.step3)
async def succesful_payment(message: types.Message, state: FSMContext):
    await bot.send_message(
                           message.chat.id,
                           MSG['successful'].format(message.successful_payment.total_amount // 100)
                          )
    data = await state.get_data()
    if type(DICTIONARY_PRESET[data['item']]['file_name']) == list:
        res = DICTIONARY_PRESET[data['item']]['file_name']
        for item in res:
            await bot.send_document(
                                    message.chat.id,
                                    document=item
                                   )
    else:
        await bot.send_document(
                                message.chat.id,
                                document=DICTIONARY_PRESET[data['item']]['file_name']
                               )
    await state.finish()
