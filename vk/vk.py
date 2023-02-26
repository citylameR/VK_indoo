import requests
import random
from heapq import nlargest
from tokens import token_vk
from pprint import pprint

def search_people(criteria):
    URL_search_people = 'https://api.vk.com/method/users.search'
    params_search_people = {
        "access_token": token_vk,
        'count': '1000',
        'sex': criteria['sex'],
        'age_from': criteria['min_age'],
        'age_to': criteria['max_age'],
        'has_photo': '1',
        'is_closed': 'False',
        'city': criteria['city'],
        "v": "5.131"
    }
    response_search_people = requests.get(URL_search_people, params=params_search_people)
    data_search_people = response_search_people.json()['response']['items']
    list_id = []
    for people in data_search_people:
        list_id.append(people['id'])
    person_id = random.choice(list_id)
    return person_id


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
                data_top_photo.append(photo["sizes"][-1]["url"])
        return data_top_photo
    else:
        for photo in data_id_photo['items']:
            data_top_photo.append(photo["sizes"][-1]["url"])
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


def person_info(people_data):
    person = random.choice(people_data)
    to_message = {'first_name': person['first_name'],
                  'last_name': person['last_name'],
                  'link': person['href'],
                  'city': person['city'],
                  'sex': person['sex'],
                  'photo': take_photo(person['id'])}
    return to_message

def get_city_index(city: str):
    url = 'https://api.vk.com/method/database.getCities'
    params = {
        "access_token": token_vk,
        "v": "5.131",
        "q": city,
        "count": "1"
    }
    response = requests.get(url, params=params)
    index = response.json()['response']['items'][0]
    return index