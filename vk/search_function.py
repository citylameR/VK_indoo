import requests
from data.config import token_vk


def search(criteria, offset):
    offer = []
    url = "https://api.vk.com/method/users.search"
    params = {
        "access_token": token_vk,
        "fields": "city, sex, can_write_private_message",
        "v": "5.131",
        "city": criteria["city"],
        "age_from": criteria["age_min"],
        "age_to": criteria["age_max"],
        "has_photo": "1",
        "count": "20",
        "sex": criteria["sex"],
        "offset": offset,
    }
    response = requests.get(url, params=params)
    searched = response.json()["response"]["items"]
    for result in searched:
        if result["is_closed"] == False:
            offer.append(
                {
                    "id": result["id"],
                    "first_name": result["first_name"],
                    "last_name": result["last_name"],
                    "sex": result["sex"],
                    "can_write": result["can_write_private_message"],
                    "href": f'vk.com/id{result["id"]}',
                }
            )
    return offer
