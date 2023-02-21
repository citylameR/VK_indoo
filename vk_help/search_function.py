import requests
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
                          'sex': result['sex'], 'can_write':result['can_write_private_message'], 'href': f'vk_help.com/id{result["id"]}',
                          })
    return offer

# criteria_data = {'min_age': 15, 'max_age': 20, 'sex': 2, 'city': 1}
# print(search(criteria_data))