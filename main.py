from vk import vk
import json
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from data import config
import bot.keyboards as keys
from random import randrange
from db.dp_gino import db
import asyncio
from db import quick_commands
import db
from pprint import pprint
from vk import vk as vkfunc
import json

def write_msg_wk(user_id, message,my_keyboard=keys.hello_keyboard):
    vk_bot.method('messages.send', {'user_id': user_id,
                                    'message': message,
                                    'random_id': randrange(10 ** 7),
                                    'keyboard': my_keyboard.get_keyboard()})

def write_msg(user_id, message):
    vk_bot.method('messages.send', {'user_id': user_id,
                                'message': message,
                                'random_id': randrange(10 ** 7)})


def search_criteria():
    write_msg(event.user_id, '1) Введите минимальный возраст:')
    for event_min_age in longpoll.listen():
        if event_min_age.type == VkEventType.MESSAGE_NEW and event_min_age.to_me:

            try:
                min_age = int(event_min_age.text)
                if min_age < 0 or min_age > 99:
                    raise ValueError()
            except ValueError:
                write_msg(event.user_id, "Не число, или недопустимое число.")
            else:
                write_msg(event.user_id, '2) Введите максимальный возраст:')
                for event_max_age in longpoll.listen():
                    if event_max_age.type == VkEventType.MESSAGE_NEW and event_max_age.to_me:
                        try:
                            max_age = int(event_max_age.text)
                            if max_age < 0 or max_age > 99 or max_age < min_age:
                                raise ValueError
                        except ValueError:
                            write_msg(event.user_id, "Не число, или недопустимое число, или меньше минимального.")
                        else:
                            write_msg(event.user_id, '3) Введите пол:', my_keyboard=keys.keyboard_sex)
                            for event_sex in longpoll.listen():
                                if event_sex.type == VkEventType.MESSAGE_NEW and event_sex.to_me:
                                    sex = 2 if event_sex.text == 'мужской' else 1
                                    write_msg(event.user_id, '4) Город:')
                                    for event_city in longpoll.listen():
                                        if event_city.type == VkEventType.MESSAGE_NEW and event_city.to_me:
                                            city = vk.get_city_index(event_city.text)
                                            with open('criteria_file', 'w', encoding='UTF-8') as file:
                                                criteria_data = {'min_age': min_age, 'max_age': max_age, 'sex': sex, 'city': city}
                                                json.dump(criteria_data, file)

                                            return criteria_data


def new_user():
    pass

def suggest_person(user_id, message, my_keyboard=keys.p_keyboard):
    vk_bot.method('messages.send', {'user_id': user_id,
                                    'message': message,
                                    'random_id': randrange(10 ** 7),
                                    'attacment': vk.take_photo(user_id)[0],
                                    'keyboard': my_keyboard.get_keyboard()})

if __name__ == "__main__":
    vk_bot = vk_api.VkApi(token=config.token_bot)
    longpoll = VkLongPoll(vk_bot)
    print("Bot started succesfully")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(db.dp_gino.on_startup())
    print("Connected to database successfully")


    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                request = event.text
                # loop.run_until_complete(pprint(quick_commands.select_user(user_id=event.user_id)))
                if request.lower() == 'отсутствует':
                    info = (vkfunc.take_user_info(event.user_id))
                    pprint(info)
                    write_msg(event.user_id, f"Хай, {info['first_name']}!"
                                             f"Приветствую тебя в Vkinder! Давайте определим критерии выбора,"
                                             f"нажав на кнопку <Установить критерии поиска>")

                    loop.run_until_complete(quick_commands.add_user(user_id=event.user_id, first_name=info['first_name'],
                                                                 last_name=info['last_name'], city=str(info['city']), age=22,
                                                                 age_min=20, age_max=25, sex=str(info['sex'])))
                elif request == 'Установить критерии поиска':
                    suggest_person(event.user_id, vk.person_info(search_criteria()))

                elif request == 'Следующий':
                    with open('criteria_file', 'r', encoding='UTF-8') as file:
                        data_criteria = json.load(file)
                        suggest_person(event.user_id, vk.person_info(data_criteria))
                else:
                    write_msg(event.user_id, "Я Вас не понимаю :) Для начала напишите: Да")