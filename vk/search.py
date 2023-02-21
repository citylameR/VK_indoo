import requests
from tokens import token_vk

def search(city, sex, age_min, age_max):
    offer = []
    url = "https://api.vk.com/method/users.search"
    params = {
        "access_token": token_vk,
        "fields": "city, sex, can_write_private_message",
        "v": "5.131",
        "city": city,
        "age_from": age_min,
        "age_to": age_max,
        "has_photo": "1",
        "count": "1000",
        "sex": sex
    }
    response = requests.get(url, params=params)
    searched = response.json()['response']['items']
    for result in searched:
        if result['is_closed'] == False:
            offer.append({'id': result['id'], 'first_name': result['first_name'], 'last_name': result['last_name'],
                          'can_write':result['can_write_private_message'], 'href': f'vk.com/id{result["id"]}'})
    return offer