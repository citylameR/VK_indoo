import bot.keyboards as keys
import bot
from db import quick_commands
import asyncio


def rewrite(info):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(quick_commands.upd_user(user_id=info["id"],
                                                    first_name=info["first_name"],
                                                    last_name=info["last_name"],
                                                    age=info["age"],
                                                    age_min=info["age_min"],
                                                    age_max=info["age_max"],
                                                    sex=info["sex"],
                                                    city=info["city"],
                                                    city_title=info["city_title"]))


def show(info, vk_bot):
    botfunc = bot.funcs.Botfuncs(vk_bot)
    if info["sex"] == 1:
        sex = 'девушек'
    else:
        sex = 'мужчин'
    botfunc.write_msg_wk(info["id"], f'Ваше имя: {info["first_name"]}\n'
                                     f'Ваш город: {info["city_title"]}\n'
                                     f'Ваш возраст: {info["age"]}\n'
                                     f'Вы ищете: {sex}\n'
                                     f'от {info["age_min"]} до {info["age_max"]} лет\n\n'
                                     f'Хотите ли что-нибудь поменять?', keys.profile_keys)
    req_profile = botfunc.listen()
    change = bot.registration.Registration(info["id"], info, vk_bot)
    while True:
        if req_profile == 'Назад':
            return

        elif req_profile == 'Имя':
            info["first_name"] = change.getname()
            rewrite(info)
            req_profile = ''

        elif req_profile == 'Город':
            city = change.getcity()
            info["city"] = city["id"]
            info["city_title"] = city["title"]
            rewrite(info)
            req_profile = ''

        elif req_profile == 'Пол':
            info["sex"] = change.getsex()
            rewrite(info)
            req_profile = ''

        elif req_profile == 'Возраст':
            info["age"] = int(change.getage())
            rewrite(info)
            req_profile = ''

        elif req_profile == 'Диапазон':
            info["age_min"] = int(change.getage_min())
            info["age_max"] = int(change.getage_max(info["age_min"]))
            rewrite(info)
            req_profile = ''

        else:
            if req_profile != '':
                botfunc.write_msg_wk(info["id"], 'Хотите ли что-нибудь поменять?', keys.profile_keys)
            req_profile = botfunc.listen()
