PAYMENT_TOKEN = 'live_BZGFoRB3_070p2NV0SqAZUMpcqfNJk8xhiN9zLWDMeg'
SHOP_ID = '963893'
# PAYMENT_TOKEN = 'test_b5Qx4NQ9xufGdn3bDYv6No4AZV_TGAPC1A29n9iL5Oo'#Lavkapresets
# SHOP_ID = '968439'#lavkapresetstest
BOT_TOKEN: str = '5981033563:AAF0JKJOMp5LflGXK2Y7GTeYFeBXvXlSCZQ'#Lavkapresets
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
        'striketh_text': '\u0336'.join('199₽'),
        'price_sell': ['109₽'],
        'price': '449',
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
        'striketh_text': '\u0336'.join('199₽'),
        'price_sell': ['109₽'],
        'price': '149',
        'photo_url': 'https://i.postimg.cc/tJsQDSd3/retro.jpg',
        'photo_height': 720,
        'photo_width': 1280,
        'photo_size': 1250000,
        'file_name': 'BQACAgIAAxkBAAIPCWPT_ZHx2B9VV6r9_QeZLA5hFMPmAAKKJAACvjGgSqF9Yvta-jvMLQQ'
    },
    'tasty': {
        'name': 'Tasty',
        'striketh_text': '\u0336'.join('199₽'),
        'price_sell': ['109₽'],
        'price': '149',
        'photo_url': 'https://i.postimg.cc/cJd6cbTg/tasty.jpg',
        'photo_height': 720,
        'photo_width': 1280,
        'photo_size': 1250000,
        'file_name': 'BQACAgIAAxkBAAIPCGPT_Nr_UGolXlUXGrNMpilw8yx-AAKJJAACvjGgSl7IF6ZTH5V_LQQ'
    },
    'kodak': {
        'name': 'Kodak',
        'striketh_text': '\u0336'.join('199₽'),
        'price_sell': ['109₽'],
        'price': '149',
        'photo_url': 'https://i.postimg.cc/g0rj5ZFm/kodak.jpg',
        'photo_height': 720,
        'photo_width': 1280,
        'photo_size': 1250000,
        'file_name': 'BQACAgIAAxkBAAIPCmPT_gXxJavN_7SuM2i1ypGP8dMUAAKNJAACvjGgSlz-hvGzTUZLLQQ'
    },
    'film': {
        'name': 'Film',
        'striketh_text': '\u0336'.join('199₽'),
        'price_sell': ['109', '109₽'],
        'price': '149',
        'photo_url': 'https://i.postimg.cc/7LpHWtnn/film.jpg',
        'photo_height': 720,
        'photo_width': 1280,
        'photo_size': 1250000,
        'file_name': 'BQACAgIAAxkBAAIPC2PT_kMactjOgDNeijTSzL9zZqUfAAKPJAACvjGgSnD_7pg527ipLQQ'
    },
    'light': {
        'name': 'Light',
        'striketh_text': '\u0336'.join('199₽'),
        'price_sell': ['109', '109₽'],
        'price': '149',
        'photo_url': 'https://i.postimg.cc/J0FPNJL0/light.jpg',
        'photo_height': 720,
        'photo_width': 1280,
        'photo_size': 1250000,
        'file_name': 'BQACAgIAAxkBAAIPDGPT_o6Ur2SiVNpTVc6AOSjVkGo-AAKRJAACvjGgSg8Katvyngf0LQQ'
    },

}
