import json
from yookassa import Configuration,Payment
from config.config import DICTIONARY_PRESET, SHOP_ID, PAYMENT_TOKEN
import asyncio

Configuration.account_id = SHOP_ID
Configuration.secret_key = PAYMENT_TOKEN

def payments(item, chat_id):

    payment = Payment.create({
    "amount": {
        "value": DICTIONARY_PRESET[item]['price_sell'][0],
        "currency": "RUB"
    },
    "payment_method_data": {
        "type": "bank_card"
    },
    "confirmation": {
        "type": "redirect",
        "return_url": "https://t.me/lavkaPresets_bot"
    },
    "metadata": {"chat_id": chat_id},
    "capture": True,
    "description": "Оплата пресета " + DICTIONARY_PRESET[item]['name']
    })

    return json.loads(payment.json())


async def check_payment(payment_id, chat_id):
    payment = json.loads((Payment.find_one(payment_id)).json())

    while payment['status'] == 'pending':
        payment = json.loads((Payment.find_one(payment_id)).json())
        await asyncio.sleep(3)

    if payment['status']=='succeeded':
        return True
    else:
        return False
