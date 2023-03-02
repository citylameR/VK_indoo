import vk
from pprint import pprint
import bot.keyboards as keys
from random import randrange
import bot
import asyncio
from db import quick_commands


def suggest_person(vk_bot, offer, user_id, my_keyboard=keys.p_keyboard):
    pprint(offer)
    message = "{} {} \n{}".format(
        offer["first_name"], offer["last_name"], offer["href"]
    )
    attachments = ",".join(vk.vk.take_photo(offer["id"]))
    if offer["can_write"] == 1:
        message += "\n\nЛИЧКА ОТКРЫТА"
    vk_bot.method(
        "messages.send",
        {
            "user_id": user_id,
            "message": message,
            "random_id": randrange(10**7),
            "attachment": attachments,
            "keyboard": my_keyboard.get_keyboard(),
        },
    )


def start_search(user_id, vk_bot, info):
    offset = 0
    offer = vk.search_function.search(info, offset)
    botfuncs = bot.funcs.Botfuncs(vk_bot)
    counter = 0
    suggest_person(vk_bot, offer[counter], user_id)
    while True:
        req = botfuncs.listen()
        if req == "Следующий":
            counter += 1
            suggest_person(vk_bot, offer[counter], user_id)
            if counter == len(offer) - 1:
                offset += 20
                counter = 0
                offer = vk.search_function.search(info, offset)
        if req == "В избранное":
            loop = asyncio.get_event_loop()
            loop.run_until_complete(
                quick_commands.add_fav(user_id=user_id, fav_id=offer[counter]["id"])
            )
            botfuncs.write_msg_wk(
                user_id, "Пользователь успешно добавлен!", keys.p_keyboard
            )
            counter += 1
            suggest_person(vk_bot, offer[counter], user_id)
            if counter == len(offer) - 1:
                offset += 20
                counter = 0
                offer = vk.search_function.search(info, offset)
        if req == "Меню":
            botfuncs.write_msg_wk(user_id, "Выберите действие:", keys.menu_keys)
            break
