import vk
from pprint import pprint
import bot.keyboards as keys
from random import randrange
import bot
import asyncio
from db import quick_commands


def suggest_person(vk_bot, offer, user_id, my_keyboard=keys.p_keyboard):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(quick_commands.add_offer(user_id, offer["id"]))
    message = f'*id{offer["id"]}({offer["first_name"]} {offer["last_name"]})'
    if offer["age"] != None: message += f', {offer["age"]}'
    if offer["city"] != None: message += f'\n{offer["city"]}'
    pprint(offer)

    attachments = ",".join(vk.vk.take_photo(offer["id"]))
    if offer["can_write"] == 1:
        message += "\n\n!ЛИЧКА ОТКРЫТА!"
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
    botfuncs = bot.funcs.Botfuncs(vk_bot)
    botfuncs.write_msg(user_id, "Минуточку! Уже подбираю страницы!")
    offset = 0
    offer = vk.search_function.search(info, offset)
    while len(offer) == 0:
        offset += 20
        offer = vk.search_function.search(info, offset)
    counter = 0
    suggest_person(vk_bot, offer[counter], user_id)
    while True:
        req = botfuncs.listen()
        if req == "Следующий":
            counter += 1
            if counter == len(offer):
                offset += 20
                counter = 0
                offer = vk.search_function.search(info, offset)
            suggest_person(vk_bot, offer[counter], user_id)
        if req == "В избранное":
            loop = asyncio.get_event_loop()
            loop.run_until_complete(
                quick_commands.add_fav(user_id=user_id, favorite_id=offer[counter]["id"],
                                       name=f'{offer[counter]["first_name"]} {offer[counter]["last_name"]}')
            )
            botfuncs.write_msg_wk(
                user_id, "Пользователь успешно добавлен!", keys.p_keyboard
            )
            counter += 1
            if counter == len(offer):
                offset += 20
                counter = 0
                offer = vk.search_function.search(info, offset)
            suggest_person(vk_bot, offer[counter], user_id)

        if req == "Пожаловаться":
            botfuncs.write_msg(user_id, "Что-то не так? Расскажите нам, мы все проверим!")
            reason = botfuncs.listen()
            loop = asyncio.get_event_loop()
            loop.run_until_complete(quick_commands.add_bl(offer[counter]["id"], reason, "moderate"))
            botfuncs.write_msg(user_id, "Спасибо за обращение!")
            counter += 1
            if counter == len(offer):
                offset += 20
                counter = 0
                offer = vk.search_function.search(info, offset)
            suggest_person(vk_bot, offer[counter], user_id)

        if req == "Меню":
            botfuncs.write_msg_wk(user_id, "Выберите действие:", keys.menu_keys)
            break
