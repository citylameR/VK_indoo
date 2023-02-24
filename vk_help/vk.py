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
