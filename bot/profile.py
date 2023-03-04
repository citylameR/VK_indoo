import vk
from pprint import pprint
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
                                                    city=info["city"]))

def show(info, vk_bot):
    pprint(info)
    botfunc = bot.funcs.Botfuncs(vk_bot)
    botfunc.write_msg_wk(info["id"], f'Ваше имя: {info["first_name"]}\n'
                                     f'Ваш город: {info["city"]}\n'
                                     f'Вы ищете: {info["sex"]}\n'
                                     f'От {info["age_min"]} до {info["age_max"]} лет\n\n'
                                     f'Хотите ли что-нибудь поменять?', keys.profile_keys)
    mess = botfunc.listen()
    change = bot.registration.Registration(info["id"], info, vk_bot)
    while True:
        if mess == 'Назад':
            botfunc.write_msg_wk(info["id"], "Выберите действие:", keys.menu_keys)
            break

        elif mess == 'Имя':
            info["first_name"] = change.getname()
            rewrite(info)
            mess = ''

        else:
            botfunc.write_msg_wk(info["id"], 'Хотите ли что-нибудь поменять?', keys.profile_keys)
            mess = botfunc.listen()
