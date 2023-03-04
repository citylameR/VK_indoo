import bot
import bot.keyboards as keys
import asyncio
from db import quick_commands
from pprint import pprint


def mainmenu(user_id, vk_bot, info):
    botfunc = bot.funcs.Botfuncs(vk_bot)
    if info == None:
        bot.new_user.new_user(user_id, botfunc, vk_bot)
        loop = asyncio.get_event_loop()
        info = loop.run_until_complete(quick_commands.select_user(user_id))
        pprint(info)
    botfunc.write_msg_wk(user_id, f'Добро пожаловать, {info["first_name"]}', keys.menu_keys)

    while True:
        req = botfunc.listen()
        if req == "Начать поиск":
            bot.start_search.start_search(user_id, vk_bot, info)
        elif req == "Список избранных":
            loop = asyncio.get_event_loop()
            favs = loop.run_until_complete(quick_commands.list_favorites(user_id))
            message = ""
            counter = 1
            for person in favs:
                message += f"{counter}. vk.com/id{person['id']} | {person['name']}\n"
                counter += 1
            botfunc.write_msg_wk(user_id, message, keys.menu_keys)
        elif req == "Мой профиль":
            bot.profile.show(info, vk_bot)
        else:
            botfunc.write_msg_wk(user_id, "Выберите действие:", keys.menu_keys)
