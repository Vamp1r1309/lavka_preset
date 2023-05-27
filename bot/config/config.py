import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN_LavkaPresets')
SHOP_ID = os.getenv('SHOP_ID')
PAYMENT_TOKEN = os.getenv('PAYMENT_TOKEN')
ADMIN_ID = [696797613, 502602785]


DICTIONARY_PRESET: dict = {
    'Зимний пак': {
        'name': 'Зимний пак',
        'price': '109',
        'photo_url': 'https://i.postimg.cc/pVCB5xWx/winter-Combo.jpg',
        'photo_height': 800,
        'photo_width': 600,
        'photo_size': 125000,
        'file_name': ['BQACAgIAAxkBAAICrGOSCe_u8Jdkbj08x0GHnvxtwLtwAAJ9KAACThqRSKOPFfxArVCbKwQ', 'BQACAgIAAxkBAAICq2OSCPW7dj4cYjWt2eD_WWhf9kJyAAJpKAACThqRSE5I_yyGWp8QKwQ',
                      'BQACAgIAAxkBAAICrmOSC5mVK17bRdcZuV7RNZZuxOK1AAKTKAACThqRSN6qz0Gmc6kFKwQ', 'BQACAgIAAxkBAAICqGOSBScshpEctvF-SMcokZollMnCAAIsKAACThqRSN0gZfe__LIJKwQ',
                      'BQACAgIAAxkBAAICnWOSAgf-CZobanHgYcp5v8UUgUq5AAIBKAACThqRSLQBtuTbpJUBKwQ']
    },
    'Весенний пак': {
        'name': 'Весенний пак',
        'price': '109',
        'photo_url': 'https://i.postimg.cc/CKmbxDLQ/spring-Combo.jpg',
        'photo_height': 800,
        'photo_width': 600,
        'photo_size': 1250000,
        'file_name': ['BQACAgIAAxkBAAIZpGQkr8xVbHze7uSLdkdtCAdeZ-VvAAJFLwACFpMgSXfuIg-U7Zu3LwQ', 'BQACAgIAAxkBAAIZpmQksDCeiTTQMx2u022uOQ5kYDjPAAJLLwACFpMgSXQYhAZ-1sHCLwQ',
                      'BQACAgIAAxkBAAIWemP-bG9N1PJn2Gnul-pbJdtfz455AAKcJgACH1P4SyZH_R1hiqfCLgQ', 'BQACAgIAAxkBAAIZpWQksAxQ7fT4ExvkQ1nJssiA48ReAAJJLwACFpMgSXZy8v_FJGN7LwQ',
                      'BQACAgIAAxkBAAIZzmQkvDgwDvf46YvwgSBHSBk9An0OAAJfLwACFpMgScECJ_fzdmAbLwQ'],
    },
    'Летний пак': {
        'name': 'Летний пак',
        'price': '109',
        'photo_url': 'https://i.postimg.cc/L4w8cjrL/summer-Combo.jpg',
        'photo_height': 800,
        'photo_width': 600,
        'photo_size': 1250000,
        'file_name': ['BQACAgIAAxkBAAIdrmRxOXOfjAABLyznYF-yMKOcAxA07AAC2SgAAqhLkUs-8elcuAt5iS8E', 'BQACAgIAAxkBAAIdr2RxOaCxoaj0GxSYAxeg7TO4ewpDAALbKAACqEuRS1qr8C-7fXBbLwQ',
                      'BQACAgIAAxkBAAIdsGRxOc6Bx75jwb4XxcDPPmNTqRP7AALcKAACqEuRSxif_YykwwkzLwQ', 'BQACAgIAAxkBAAIdsWRxOfqyr98366KmgYEDPptZ6Sn-AALdKAACqEuRS319ZJpCQYqsLwQ',
                      'BQACAgIAAxkBAAIdsmRxOh7okQ-d2gdJq7yL9-51EtH1AALeKAACqEuRS6QrsH4U8c-iLwQ'],
    },
    'Предметный пак': {
        'name': 'Предметный пак',
        'price': '109',
        'photo_url': 'https://i.postimg.cc/J0jSzPJm/Item-Combo.jpg',
        'photo_height': 800,
        'photo_width': 600,
        'photo_size': 1250000,
        'file_name': ['BQACAgIAAxkBAAIPCWPT_ZHx2B9VV6r9_QeZLA5hFMPmAAKKJAACvjGgSqF9Yvta-jvMLQQ', 'BQACAgIAAxkBAAIPCGPT_Nr_UGolXlUXGrNMpilw8yx-AAKJJAACvjGgSl7IF6ZTH5V_LQQ',
                      'BQACAgIAAxkBAAIPCmPT_gXxJavN_7SuM2i1ypGP8dMUAAKNJAACvjGgSlz-hvGzTUZLLQQ', 'BQACAgIAAxkBAAIPC2PT_kMactjOgDNeijTSzL9zZqUfAAKPJAACvjGgSnD_7pg527ipLQQ',
                      'BQACAgIAAxkBAAIPDGPT_o6Ur2SiVNpTVc6AOSjVkGo-AAKRJAACvjGgSg8Katvyngf0LQQ']
    },
    'Мегапак': {
            'name': 'Мегапак',
            'price': '399',
            'photo_url': 'https://i.postimg.cc/pL023bNd/combo-Presets.jpg',
            'photo_height': 800,
            'photo_width': 600,
            'photo_size': 1250000,
            'file_name': ['BQACAgIAAxkBAAIPCWPT_ZHx2B9VV6r9_QeZLA5hFMPmAAKKJAACvjGgSqF9Yvta-jvMLQQ', 'BQACAgIAAxkBAAIPCGPT_Nr_UGolXlUXGrNMpilw8yx-AAKJJAACvjGgSl7IF6ZTH5V_LQQ',
                          'BQACAgIAAxkBAAIPCmPT_gXxJavN_7SuM2i1ypGP8dMUAAKNJAACvjGgSlz-hvGzTUZLLQQ', 'BQACAgIAAxkBAAIPC2PT_kMactjOgDNeijTSzL9zZqUfAAKPJAACvjGgSnD_7pg527ipLQQ',
                          'BQACAgIAAxkBAAIPDGPT_o6Ur2SiVNpTVc6AOSjVkGo-AAKRJAACvjGgSg8Katvyngf0LQQ', 'BQACAgIAAxkBAAIdrmRxOXOfjAABLyznYF-yMKOcAxA07AAC2SgAAqhLkUs-8elcuAt5iS8E',
                          'BQACAgIAAxkBAAIdr2RxOaCxoaj0GxSYAxeg7TO4ewpDAALbKAACqEuRS1qr8C-7fXBbLwQ', 'BQACAgIAAxkBAAIdsGRxOc6Bx75jwb4XxcDPPmNTqRP7AALcKAACqEuRSxif_YykwwkzLwQ',
                          'BQACAgIAAxkBAAIdsWRxOfqyr98366KmgYEDPptZ6Sn-AALdKAACqEuRS319ZJpCQYqsLwQ', 'BQACAgIAAxkBAAIdsmRxOh7okQ-d2gdJq7yL9-51EtH1AALeKAACqEuRS6QrsH4U8c-iLwQ',
                          'BQACAgIAAxkBAAIZpGQkr8xVbHze7uSLdkdtCAdeZ-VvAAJFLwACFpMgSXfuIg-U7Zu3LwQ', 'BQACAgIAAxkBAAIZpmQksDCeiTTQMx2u022uOQ5kYDjPAAJLLwACFpMgSXQYhAZ-1sHCLwQ',
                          'BQACAgIAAxkBAAIWemP-bG9N1PJn2Gnul-pbJdtfz455AAKcJgACH1P4SyZH_R1hiqfCLgQ', 'BQACAgIAAxkBAAIZpWQksAxQ7fT4ExvkQ1nJssiA48ReAAJJLwACFpMgSXZy8v_FJGN7LwQ',
                          'BQACAgIAAxkBAAIZzmQkvDgwDvf46YvwgSBHSBk9An0OAAJfLwACFpMgScECJ_fzdmAbLwQ', 'BQACAgIAAxkBAAICrGOSCe_u8Jdkbj08x0GHnvxtwLtwAAJ9KAACThqRSKOPFfxArVCbKwQ',
                          'BQACAgIAAxkBAAICq2OSCPW7dj4cYjWt2eD_WWhf9kJyAAJpKAACThqRSE5I_yyGWp8QKwQ', 'BQACAgIAAxkBAAICrmOSC5mVK17bRdcZuV7RNZZuxOK1AAKTKAACThqRSN6qz0Gmc6kFKwQ',
                          'BQACAgIAAxkBAAICqGOSBScshpEctvF-SMcokZollMnCAAIsKAACThqRSN0gZfe__LIJKwQ', 'BQACAgIAAxkBAAICnWOSAgf-CZobanHgYcp5v8UUgUq5AAIBKAACThqRSLQBtuTbpJUBKwQ',
                          ]
    },
    'Английский Язык': {
        'name': 'Ресурсы по английскому',
        'price': '149',
        'photo_url': 'https://i.postimg.cc/tT2sVKgJ/English.jpg',
        'photo_height': 800,
        'photo_width': 600,
        'photo_size': 1250000,
        'file_name': ['BQACAgIAAxkBAAIds2RxOoRZV1iUZCrOtjwVsCCVd4ZTAALgKAACqEuRSz8B-tAe7PCILwQ',]
    },
}