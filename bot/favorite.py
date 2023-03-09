import bot.keyboards as keys
import bot
from db import quick_commands
import asyncio


def delete(id, favs, vk_bot):
    botfuncs = bot.funcs.Botfuncs(vk_bot)
    loop = asyncio.get_event_loop()
    botfuncs.write_msg(id, "Введите номер избранного:")
    try:
        num = int(botfuncs.listen())-1
        loop.run_until_complete(quick_commands.delete_favorite(id, favs[num]["id"]))
        favs = loop.run_until_complete(quick_commands.list_favorites(id))
        message = ""
        counter = 1
        for person in favs:
            message += f"{counter}. vk.com/id{person['id']} | {person['name']}\n"
            counter += 1
        botfuncs.write_msg_wk(id, message, keys.favs_keys)
        return favs
    except:
        botfuncs.write_msg(id, "Пожалуйста, введите только цифру номера избранного!")
        favs = loop.run_until_complete(quick_commands.list_favorites(id))
        message = ""
        counter = 1
        for person in favs:
            message += f"{counter}. vk.com/id{person['id']} | {person['name']}\n"
            counter += 1
        botfuncs.write_msg_wk(id, message, keys.favs_keys)
        return favs


def show(info, vk_bot):
    botfuncs = bot.funcs.Botfuncs(vk_bot)
    loop = asyncio.get_event_loop()
    favs = loop.run_until_complete(quick_commands.list_favorites(info["id"]))
    message = ""
    counter = 1
    for person in favs:
        message += f"{counter}. vk.com/id{person['id']} | {person['name']}\n"
        counter += 1
    botfuncs.write_msg_wk(info["id"], message, keys.favs_keys)
    messa = ''
    while True:
        if messa == 'Назад':
            return
        elif messa == 'Удалить из избранного':
            favs = delete(info["id"], favs, vk_bot)
            messa = ''
        else:
            if messa != '':
                botfuncs.write_msg_wk(info["id"], 'Выберите действие:', keys.favs_keys)
            messa = botfuncs.listen()
