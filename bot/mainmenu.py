import bot
import bot.keyboards as keys
import asyncio
from db import quick_commands

def mainmenu(user_id, vk_bot, info):
    botfunc = bot.funcs.Botfuncs(vk_bot)
    if info == None:
        bot.new_user.new_user(user_id, botfunc, vk_bot)
        loop = asyncio.get_event_loop()
        info = loop.run_until_complete(quick_commands.select_user(user_id))
    botfunc.write_msg_wk(user_id, f'Добро пожаловать, {info["first_name"]}\n'
                               f'Выберите действие!', keys.menu_keys)
