import vk
import db
import vk_api
import json
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from random import randrange
from tokens import token_bot
from data import config
from db.dp_gino import db
import asyncio
from db import db_commands
from pprint import pprint


vk_bot = vk_api.VkApi(token=token_bot)
longpoll = VkLongPoll(vk_bot)
keyboard = VkKeyboard(one_time=False)
keyboard.add_button('В избранное', color=VkKeyboardColor.POSITIVE)
keyboard.add_button('Следующий', color=VkKeyboardColor.POSITIVE)
keyboard.add_line()
keyboard.add_button('В черный список', color=VkKeyboardColor.NEGATIVE)
keyboard.add_button('Список избранных', color=VkKeyboardColor.PRIMARY)
keyboard.add_line()
keyboard.add_button('Установить критерии поиска', color=VkKeyboardColor.SECONDARY)


def write_msg(user_id, message, my_keyboard=keyboard):
    vk_bot.method('messages.send', {'user_id': user_id,
                                'message': message,
                                'random_id': randrange(10 ** 7),
                                'keyboard': my_keyboard.get_keyboard()})


def search_criteria():
    write_msg(event.user_id, '1) Введите минимальный возраст:')
    for event_min_age in longpoll.listen():
        if event_min_age.type == VkEventType.MESSAGE_NEW and event_min_age.to_me:
            min_age = event_min_age.text
            write_msg(event_min_age.user_id, 'Успешно')
            write_msg(event.user_id, '2) Введите максимальный возраст:')
            for event_max_age in longpoll.listen():
                if event_max_age.type == VkEventType.MESSAGE_NEW and event_max_age.to_me:
                    max_age = event_max_age.text
                    keyboard_sex = VkKeyboard(one_time=False)
                    keyboard_sex.add_button('мужской', color=VkKeyboardColor.POSITIVE)
                    keyboard_sex.add_button('женский', color=VkKeyboardColor.NEGATIVE)
                    write_msg(event.user_id, '3) Введите пол:', my_keyboard=keyboard_sex)
                    for event_sex in longpoll.listen():
                        if event_sex.type == VkEventType.MESSAGE_NEW and event_sex.to_me:
                            sex = event_sex.text
                            write_msg(event.user_id, '4) Город:')
                            for event_city in longpoll.listen():
                                if event_city.type == VkEventType.MESSAGE_NEW and event_city.to_me:
                                    city = event_city.text
                                    criteria_data = {'min_age': min_age, 'max_age': max_age, 'sex': sex, 'city': city}
                                    return criteria_data


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:

        if event.to_me:
            request = event.text
            if request.lower() == 'да':
                write_msg(event.user_id, f"Хай, {event.user_id}! "
                                         f"Приветствую тебя в Vkinder! Давайте определим критерии выбора,"
                                         f"нажав на кнопку <Установить критерии поиска>")  #Поменять id на имя
            elif request == 'Установить критерии поиска':
                search_criteria()

            else:
                write_msg(event.user_id, "Я Вас не понимаю :) Для начала напишите: Да")


async def on_start_up():
    await db.set_bind(config.POSTGRES_URI)
    await db.gino.drop_all()
    await db.gino.create_all()
    await db_commands.add_user(user_id=28964076, first_name="Igor", last_name="Ter-pogosyan", city="Saint-P", age=22,
                               age_min=20, age_max=25, sex="Мужской")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(on_start_up())