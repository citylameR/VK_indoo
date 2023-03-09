import bot
import bot.keyboards as keys
import asyncio
from db import quick_commands


def mainmenu(user_id, vk_bot, info):
    botfunc = bot.funcs.Botfuncs(vk_bot)
    if info is None:
        bot.new_user.new_user(user_id, botfunc, vk_bot)
        loop = asyncio.get_event_loop()
        info = loop.run_until_complete(quick_commands.select_user(user_id))
    botfunc.write_msg_wk(user_id, f'Добро пожаловать, {info["first_name"]}', keys.menu_keys)
    req_menu = botfunc.listen()
    while True:
        if req_menu == "Начать поиск":
            bot.start_search.start_search(user_id, vk_bot, info)
            req_menu = ''
        elif req_menu == "Список избранных":
            bot.favorite.show(info, vk_bot)
            req_menu = ''
        elif req_menu == "Мой профиль":
            req_menu = ''
            bot.profile.show(info, vk_bot)
        else:
            if req_menu != '':
                botfunc.write_msg_wk(user_id, "Выберите действие:", keys.menu_keys)
            req_menu = botfunc.listen()
