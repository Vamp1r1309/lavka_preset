PAYMENT_TOKEN = 'live_BZGFoRB3_070p2NV0SqAZUMpcqfNJk8xhiN9zLWDMeg'
SHOP_ID = '963893'
# PAYMENT_TOKEN = 'test_b5Qx4NQ9xufGdn3bDYv6No4AZV_TGAPC1A29n9iL5Oo'#Lavkapresets
# SHOP_ID = '968439'#lavkapresetstest
BOT_TOKEN: str = '5981033563:AAFhE4GCHnV-wAkTjRRxdMvD12SchTaUueA'#Lavkapresets
# BOT_TOKEN: str = '5678361086:AAEsTwVgqOAll7EEA_J7sNosSXyGqRlFF80'#lavkapresetstest

ADMIN_ID = [696797613, 502602785]


MSG: dict[str, str] = {
    'start': 'Привет, я бот от @ketrin_info. Я помогу тебе с выбором пресета😊',
    'help': 'Какой у вас вопрос?',
    'helpPAY': 'Если возникли проблемы с оплатой или вы не получили пресет,свяжитесь со мной по почте: lavkapresetshelp@gmail.com',
    'settingsPresets': 'Высылаю тебе подробную инструкцию по использованию пресетов😉',
    'video': 'BAACAgIAAxkBAAIIj2Oi1wizZEv86hCoXv62y7mlGJfEAAK1JAACG2kYSRBZ3HCpYbNKLAQ',
    'preset': 'Выбери категорию',
    'successful': 'Платёж на сумму {} прошел успешно!\nНадеюсь, тебе понравится😉',
    'exitText': "Вы не завершили покупку, хотите продолжить?😊",
    'successfulMessage': 'Сообщения успешно разосланы'
}
predmetPrice = ["329₽", "109₽"]
predmetNormalPrice = ['\u0336'.join("449₽"), '\u0336'.join("149₽")]
zimaPrice = ["329₽", "109₽"]
PRICE_SPRING = ['\u0336'.join('490₽'), '\u0336'.join('179₽')]
PRICE_SPRING_COMBO = ['329', '329₽']
PRICE_SELL_SPRING = ['129', '129₽']

DICTIONARY_PRESET_ZIMA: dict = {
    'Зимнее combo': {
        'name': 'Combo',
        'striketh_text': '\u0336'.join('499₽'),
        'price_sell': ['329', '329₽'],
        'price': '499',
        'photo_url': 'https://i.postimg.cc/pVCB5xWx/combo.jpg',
        'photo_height': 800,
        'photo_width': 600,
        'photo_size': 125000,
        'file_name': ['BQACAgIAAxkBAAICrGOSCe_u8Jdkbj08x0GHnvxtwLtwAAJ9KAACThqRSKOPFfxArVCbKwQ', 'BQACAgIAAxkBAAICq2OSCPW7dj4cYjWt2eD_WWhf9kJyAAJpKAACThqRSE5I_yyGWp8QKwQ',
                      'BQACAgIAAxkBAAICrmOSC5mVK17bRdcZuV7RNZZuxOK1AAKTKAACThqRSN6qz0Gmc6kFKwQ', 'BQACAgIAAxkBAAICqGOSBScshpEctvF-SMcokZollMnCAAIsKAACThqRSN0gZfe__LIJKwQ',
                      'BQACAgIAAxkBAAICnWOSAgf-CZobanHgYcp5v8UUgUq5AAIBKAACThqRSLQBtuTbpJUBKwQ']
    },
    'newYear': {
        'name': 'New Year',
        'striketh_text': '\u0336'.join('199₽'),
        'price_sell': ['109', '109₽'],
        'price': '199',
        'photo_url': 'https://i.postimg.cc/J0fvkL8b/newYear.jpg',
        'photo_height': 720,
        'photo_width': 1280,
        'photo_size': 125000,
        'file_name': 'BQACAgIAAxkBAAICrGOSCe_u8Jdkbj08x0GHnvxtwLtwAAJ9KAACThqRSKOPFfxArVCbKwQ'
    },
    'magicMoment': {
        'name': 'Magic Moment',
        'striketh_text': '\u0336'.join('199₽'),
        'price_sell': ['109', '109₽'],
        'price': '199',
        'photo_url': 'https://i.postimg.cc/Kjf3KZBW/magic-Moment.jpg',
        'photo_height': 720,
        'photo_width': 1280,
        'photo_size': 125000,
        'file_name': 'BQACAgIAAxkBAAICq2OSCPW7dj4cYjWt2eD_WWhf9kJyAAJpKAACThqRSE5I_yyGWp8QKwQ'
    },
    'coldWinter': {
        'name': 'Cold Winter',
        'striketh_text': '\u0336'.join('199₽'),
        'price_sell': ['109', '109₽'],
        'price': '199',
        'photo_url': 'https://i.postimg.cc/9QJ9cDZg/cold-Winter.jpg',
        'photo_height': 720,
        'photo_width': 1280,
        'photo_size': 125000,
        'file_name': 'BQACAgIAAxkBAAICrmOSC5mVK17bRdcZuV7RNZZuxOK1AAKTKAACThqRSN6qz0Gmc6kFKwQ'
    },
    'cozy': {
        'name': 'Cozy',
        'striketh_text': '\u0336'.join('199₽'),
        'price_sell': ['109', '109₽'],
        'price': '199',
        'photo_url': 'https://i.postimg.cc/50GkhV6Z/cozy.jpg',
        'photo_height': 720,
        'photo_width': 1280,
        'photo_size': 125000,
        'file_name': 'BQACAgIAAxkBAAICqGOSBScshpEctvF-SMcokZollMnCAAIsKAACThqRSN0gZfe__LIJKwQ'
    },
    'christmasMood': {
        'name': 'Christmas Mood',
        'striketh_text': '\u0336'.join('199₽'),
        'price_sell': ['109', '109₽'],
        'price': '199',
        'photo_url': 'https://i.postimg.cc/Df9M57VG/cristmas-Mood.jpg',
        'photo_height': 720,
        'photo_width': 1280,
        'photo_size': 1250000,
        'file_name': 'BQACAgIAAxkBAAICnWOSAgf-CZobanHgYcp5v8UUgUq5AAIBKAACThqRSLQBtuTbpJUBKwQ'
    },
}
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

DICTIONARY_PRESET_PREDMET: dict = {
    'Предметные combo': {
        'name': 'Combo',
        'price': '449',
        'price_sell': ['329', '329₽'],
        'photo_url': 'https://i.postimg.cc/J0jSzPJm/combo-Predmet.jpg',
        'photo_height': 800,
        'photo_width': 600,
        'photo_size': 1250000,
        'file_name': ['BQACAgIAAxkBAAIPCWPT_ZHx2B9VV6r9_QeZLA5hFMPmAAKKJAACvjGgSqF9Yvta-jvMLQQ', 'BQACAgIAAxkBAAIPCGPT_Nr_UGolXlUXGrNMpilw8yx-AAKJJAACvjGgSl7IF6ZTH5V_LQQ',
                      'BQACAgIAAxkBAAIPCmPT_gXxJavN_7SuM2i1ypGP8dMUAAKNJAACvjGgSlz-hvGzTUZLLQQ', 'BQACAgIAAxkBAAIPC2PT_kMactjOgDNeijTSzL9zZqUfAAKPJAACvjGgSnD_7pg527ipLQQ',
                      'BQACAgIAAxkBAAIPDGPT_o6Ur2SiVNpTVc6AOSjVkGo-AAKRJAACvjGgSg8Katvyngf0LQQ']
    },
    'retro': {
        'name': 'Retro',
        'price': '149',
        'price_sell': ['109', '109₽'],
        'photo_url': 'https://i.postimg.cc/tJsQDSd3/retro.jpg',
        'photo_height': 720,
        'photo_width': 1280,
        'photo_size': 1250000,
        'file_name': 'BQACAgIAAxkBAAIPCWPT_ZHx2B9VV6r9_QeZLA5hFMPmAAKKJAACvjGgSqF9Yvta-jvMLQQ'
    },
    'tasty': {
        'name': 'Tasty',
        'price': '149',
        'price_sell': ['109', '109₽'],
        'photo_url': 'https://i.postimg.cc/cJd6cbTg/tasty.jpg',
        'photo_height': 720,
        'photo_width': 1280,
        'photo_size': 1250000,
        'file_name': 'BQACAgIAAxkBAAIPCGPT_Nr_UGolXlUXGrNMpilw8yx-AAKJJAACvjGgSl7IF6ZTH5V_LQQ'
    },
    'kodak': {
        'name': 'Kodak',
        'price': '149',
        'price_sell': ['109', '109₽'],
        'photo_url': 'https://i.postimg.cc/g0rj5ZFm/kodak.jpg',
        'photo_height': 720,
        'photo_width': 1280,
        'photo_size': 1250000,
        'file_name': 'BQACAgIAAxkBAAIPCmPT_gXxJavN_7SuM2i1ypGP8dMUAAKNJAACvjGgSlz-hvGzTUZLLQQ'
    },
    'film': {
        'name': 'Film',
        'price': '149',
        'price_sell': ['109', '109₽'],
        'photo_url': 'https://i.postimg.cc/7LpHWtnn/film.jpg',
        'photo_height': 720,
        'photo_width': 1280,
        'photo_size': 1250000,
        'file_name': 'BQACAgIAAxkBAAIPC2PT_kMactjOgDNeijTSzL9zZqUfAAKPJAACvjGgSnD_7pg527ipLQQ'
    },
    'light': {
        'name': 'Light',
        'price': '149',
        'price_sell': ['109', '109₽'],
        'photo_url': 'https://i.postimg.cc/J0FPNJL0/light.jpg',
        'photo_height': 720,
        'photo_width': 1280,
        'photo_size': 1250000,
        'file_name': 'BQACAgIAAxkBAAIPDGPT_o6Ur2SiVNpTVc6AOSjVkGo-AAKRJAACvjGgSg8Katvyngf0LQQ'
    },

}


DICTIONARY_PRESET_SPRING: dict = {
    'Весеннее combo': {
        'name': 'Combo',
        'price': '490',
        'price_sell': ['329', '329₽'],
        'photo_url': 'https://i.postimg.cc/CKmbxDLQ/Combo.jpg',
        'photo_height': 800,
        'photo_width': 600,
        'photo_size': 1250000,
        'file_name': ['BQACAgIAAxkBAAIZpGQkr8xVbHze7uSLdkdtCAdeZ-VvAAJFLwACFpMgSXfuIg-U7Zu3LwQ', 'BQACAgIAAxkBAAIZpmQksDCeiTTQMx2u022uOQ5kYDjPAAJLLwACFpMgSXQYhAZ-1sHCLwQ',
                      'BQACAgIAAxkBAAIWemP-bG9N1PJn2Gnul-pbJdtfz455AAKcJgACH1P4SyZH_R1hiqfCLgQ', 'BQACAgIAAxkBAAIZpWQksAxQ7fT4ExvkQ1nJssiA48ReAAJJLwACFpMgSXZy8v_FJGN7LwQ',
                      'BQACAgIAAxkBAAIZqGQksG-wh3_VYNun_ttaV8p4WTqSAAJPLwACFpMgSQTcgdoj4YrALwQ']
    },
    'crocus': {
        'name': 'Crocus',
        'price': '179',
        'price_sell': ['129', '129₽'],
        'photo_url': 'https://i.postimg.cc/4y4MhpzH/crocus.jpg',
        'photo_height': 720,
        'photo_width': 1280,
        'photo_size': 1250000,
        'file_name': 'BQACAgIAAxkBAAIZpGQkr8xVbHze7uSLdkdtCAdeZ-VvAAJFLwACFpMgSXfuIg-U7Zu3LwQ'
    },
    'lily': {
        'name': 'Lily',
        'price': '179',
        'price_sell': ['129', '129₽'],
        'photo_url': 'https://i.postimg.cc/HkKgDvbZ/Lily.jpg',
        'photo_height': 720,
        'photo_width': 1280,
        'photo_size': 1250000,
        'file_name': 'BQACAgIAAxkBAAIZpmQksDCeiTTQMx2u022uOQ5kYDjPAAJLLwACFpMgSXQYhAZ-1sHCLwQ'
    },
    'viola': {
        'name': 'Viola',
        'price': '179',
        'price_sell': ['129', '129₽'],
        'photo_url': 'https://i.postimg.cc/1ztfMdsv/Viola.jpg',
        'photo_height': 720,
        'photo_width': 1280,
        'photo_size': 1250000,
        'file_name': 'BQACAgIAAxkBAAIWemP-bG9N1PJn2Gnul-pbJdtfz455AAKcJgACH1P4SyZH_R1hiqfCLgQ'
    },
    'freesia': {
        'name': 'Freesia',
        'price': '179',
        'price_sell': ['129', '129₽'],
        'photo_url': 'https://i.postimg.cc/TYN8gNNd/Freesia.jpg',
        'photo_height': 720,
        'photo_width': 1280,
        'photo_size': 1250000,
        'file_name': 'BQACAgIAAxkBAAIZpWQksAxQ7fT4ExvkQ1nJssiA48ReAAJJLwACFpMgSXZy8v_FJGN7LwQ'
    },
    'primula': {
        'name': 'Primula',
        'price': '179',
        'price_sell': ['129', '129₽'],
        'photo_url': 'https://i.postimg.cc/3RGrc56F/Primula.jpg',
        'photo_height': 720,
        'photo_width': 1280,
        'photo_size': 1250000,
        'file_name': 'BQACAgIAAxkBAAIZqGQksG-wh3_VYNun_ttaV8p4WTqSAAJPLwACFpMgSQTcgdoj4YrALwQ'
    },

}
