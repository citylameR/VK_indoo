import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from data import config
import bot.keyboards as keys
from random import randrange
from db.dp_gino import db
import asyncio
from db import db_commands
import db
from pprint import pprint
from vk import vk as vkfunc

def write_msg(user_id, message, my_keyboard=keys.p_keyboard):
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
                    write_msg(event.user_id, '3) Введите пол:', my_keyboard=keys.keyboard_sex)
                    for event_sex in longpoll.listen():
                        if event_sex.type == VkEventType.MESSAGE_NEW and event_sex.to_me:
                            sex = event_sex.text
                            write_msg(event.user_id, '4) Город:')
                            for event_city in longpoll.listen():
                                if event_city.type == VkEventType.MESSAGE_NEW and event_city.to_me:
                                    city = event_city.text
                                    criteria_data = {'min_age': min_age, 'max_age': max_age, 'sex': sex, 'city': city}
                                    return criteria_data


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
            if request.lower() == 'отсутствует':
                info = (vkfunc.take_user_info(event.user_id))
                pprint(info)
                write_msg(event.user_id, f"Хай, {info['first_name']}!"
                                         f"Приветствую тебя в Vkinder! Давайте определим критерии выбора,"
                                         f"нажав на кнопку <Установить критерии поиска>")
                loop.run_until_complete(db_commands.add_user(user_id=event.user_id, first_name=info['first_name'],
                                                             last_name=info['last_name'], city=str(info['city']), age=22,
                                                             age_min=20, age_max=25, sex=str(info['sex'])))
            elif request == 'Установить критерии поиска':
                search_criteria()

            else:
                write_msg(event.user_id, "Я Вас не понимаю :) Для начала напишите: Да")