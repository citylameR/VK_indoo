import requests
import random
from heapq import nlargest
from tokens import token_vk
from pprint import pprint

def get_city_index(city: str):
    url = "https://api.vk.com/method/database.getCities"
    params = {"access_token": token_vk, "v": "5.131", "q": city, "count": "1"}
    response = requests.get(url, params=params)
    index = response.json()["response"]["items"][0]
    return index['id']

def search(criteria):
    offer = []
    url = "https://api.vk.com/method/users.search"
    params = {
        "access_token": token_vk,
        "fields": "city, sex, can_write_private_message",
        "v": "5.131",
        "city": get_city_index(criteria['city']),
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
                          'sex': result['sex'], 'can_write': result['can_write_private_message'],
                          'href': f'vk.com/id{result["id"]}',
                          })
    return offer

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
    data_id_photo = response_id_photo.json()["response"]
    max_likes = []
    data_top_photo = []
    if data_id_photo['count']>=3:
        for photo in data_id_photo['items']:
            max_likes.append(photo["likes"]["count"])
        for photo in data_id_photo['items']:
            if photo["likes"]["count"] in nlargest(3, max_likes):
                photo_info = 'photo{}_{}'.format(user_id, photo['id'])
                data_top_photo.append(photo_info)
        return data_top_photo
    else:
        for photo in data_id_photo['items']:
            photo_info = 'photo{}_{}'.format(user_id, photo['id'])
            data_top_photo.append(photo_info)
        return data_top_photo


def take_user_info(user_id):
    URL_id_info = "https://api.vk.com/method/users.get"
    params_id_info = {
        "access_token": token_vk,
        "user_ids": user_id,
        "fields": "city, sex, bdate",
        "name_case": "nom",
        "v": "5.131",
    }
    response_id_info = requests.get(URL_id_info, params=params_id_info)
    data_id_info = response_id_info.json()["response"][0]
    info = {"first_name": data_id_info['first_name'], "last_name": data_id_info['last_name'], "sex": data_id_info['sex'],
            "city": data_id_info['city']['id']}
    return info


def person_info(criteria):
    people_data = search(criteria)
    person = random.choice(people_data)
    return person

