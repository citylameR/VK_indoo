import requests
import random
from heapq import nlargest
from tokens import token_vk

def search(criteria):
    offer = []
    url = "https://api.vk.com/method/users.search"
    params = {
        "access_token": token_vk,
        "fields": "city, sex, can_write_private_message",
        "v": "5.131",
        "city": criteria['city'],
        "age_from": criteria['min_age'],
        "age_to": criteria['max_age'],
        "has_photo": "1",
        "count": "1000",
        "sex": criteria['sex']
    }
    response = requests.get(url, params=params)
    searched = response.json()['response']['items']
    for result in searched:
        if result['is_closed'] == False:
            offer.append({'id': result['id'], 'first_name': result['first_name'], 'last_name': result['last_name'],
                          'sex': result['sex'], 'can_write':result['can_write_private_message'], 'href': f'vk.com/id{result["id"]}',
                          })
    return offer

# # criteria_data = {'min_age': 15, 'max_age': 20, 'sex': 2, 'city': 'Москва'}
# def search_people(criteria):
#     URL_search_people = 'https://api.vk.com/method/users.search'
#     params_search_people = {
#         "access_token": token_vk,
#         'count': '1000',
#         'sex':criteria['sex'],
#         'age_from': criteria['min_age'],
#         'age_to': criteria['max_age'],
#         'has_photo':'1',
#         'is_closed': 'False',
#         # 'city': criteria['city'], #Не понимаю, как работать с идентификатором города
#         "v": "5.131"
#     }
#     response_search_people = requests.get(URL_search_people, params=params_search_people)
#     data_search_people = response_search_people.json()['response']['items']
#     list_id = []
#     for people in data_search_people:
#         list_id.append(people['id'])
#     person_id = random.choice(list_id)
#     return person_id

def take_photo(user_id):
    URL_id_photo = "https://api.vk.com/method/photos.get"
    params_id_photo = {
        "owner_id": user_id,
        "album_id": "profile",
        "access_token": token_vk,
        "v": "5.131",
        "extended": "1",
    }
    response_id_photo = requests.get(URL_id_photo, params=params_id_photo)
    data_id_photo = response_id_photo.json()["response"]["items"]
    max_likes = []
    data_top_photo = []
    for photo in data_id_photo:
        max_likes.append(photo["likes"]["count"])
    for photo in data_id_photo:
        if photo["likes"]["count"] in nlargest(3, max_likes):
            data_top_photo.append(photo["sizes"][-1]["url"])
    return data_top_photo


# def take_user_info(user_id):
#     URL_id_info = "https://api.vk.com/method/users.get"
#     params_id_info = {
#         "access_token": token_vk,
#         "user_ids": user_id,
#         "fields": "city, sex",
#         "name_case": "nom",
#         "v": "5.131",
#     }
#     response_id_info = requests.get(URL_id_info, params=params_id_info)
#     data_id_info = response_id_info.json()["response"]
#     for data in data_id_info:
#         first_name = data["first_name"]
#         last_name = data["last_name"]
#         city = data["city"]["title"]  # Реализовать, если нет города
#         sex = (
#             "мужской" if data["sex"] == 2 else "женский"
#         )  # Реализовать, если нет секса
#         data_info = {
#             "first_name": first_name,
#             "last_name": last_name,
#             "city": city,
#             "sex": sex,
#             "photo": take_photo(user_id),
#         }
#
#         return data_info

def person_info(criteria):
    people_data = search(criteria)
    person = random.choice(people_data)
    first_name = person['first_name']
    last_name = person['last_name']
    link = person['href']
    to_message = {'first_name': person['first_name'],
                  'last_name': person['last_name'],
                  'link': person['href'],
                  # 'city': person['city'],
                  'sex': 'мужской' if person['sex'] == 2 else 'женский',
                  'photo': take_photo(person['id'])}
    text = f'{first_name} {last_name} \n {link}'

    return text

# criteria_data = {'min_age': 15, 'max_age': 20, 'sex': 2, 'city': 1}
#
# print(person_info(criteria_data))
