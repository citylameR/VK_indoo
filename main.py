
import vk_help
import db
import vk_api
from vk import vk
import json

from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from random import randrange
from tokens import token_bot


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
        if event_min_age.type == VkEventType.MESSAGE_NEW and event_min_age.to_me: # Сделать проверку на интегер
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
                            sex = 2 if event_sex.text == 'мужской' else 1
                            write_msg(event.user_id, '4) Город:')
                            for event_city in longpoll.listen():
                                if event_city.type == VkEventType.MESSAGE_NEW and event_city.to_me:
                                    city = event_city.text
                                    with open('criteria_file', 'w', encoding='UTF-8') as file:
                                        criteria_data = {'min_age': min_age, 'max_age': max_age, 'sex': sex, 'city': city}
                                        json.dump(criteria_data, file)

                                    return criteria_data



def suggest_person(user_id, message, my_keyboard=keyboard):
    vk_bot.method('messages.send', {'user_id': user_id,
                                    'message': message,
                                    'random_id': randrange(10 ** 7),
                                    'attacment': vk_help.vk.take_photo(user_id)[0],
                                    'keyboard': my_keyboard.get_keyboard()})

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:

        if event.to_me:
            request = event.text
            if request.lower() == 'да':
                write_msg(event.user_id, f"Хай, {event.user_id}! "
                                         f"Приветствую тебя в Vkinder! Давайте определим критерии выбора,"
                                         f"нажав на кнопку <Установить критерии поиска>")  #Поменять id на имя
            elif request == 'Установить критерии поиска':
                suggest_person(event.user_id, vk_help.vk.person_info(search_criteria()))

            elif request == 'Следующий':
                with open('criteria_file', 'r', encoding='UTF-8') as file:
                    data_criteria = json.load(file)
                    suggest_person(event.user_id, vk_help.vk.person_info(data_criteria))
            else:
                write_msg(event.user_id, "Я Вас не понимаю :) Для начала напишите: Да")