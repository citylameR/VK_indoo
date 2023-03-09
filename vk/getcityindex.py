import requests
from data.config import token_vk


def get_city_index(city: str):
    url = "https://api.vk.com/method/database.getCities"
    params = {"access_token": token_vk, "v": "5.131", "q": city, "count": "1"}
    response = requests.get(url, params=params)
    try:
        index = response.json()["response"]["items"][0]
        return index
    except:
        return None
