import requests
from heapq import nlargest
from tokens import token_vk

user_id = "1"


def take_photo():
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


def take_user_info():
    URL_id_info = "https://api.vk.com/method/users.get"
    params_id_info = {
        "access_token": token_vk,
        "user_ids": user_id,
        "fields": "city, sex",
        "name_case": "nom",
        "v": "5.131",
    }
    response_id_info = requests.get(URL_id_info, params=params_id_info)
    data_id_info = response_id_info.json()["response"]
    for data in data_id_info:
        first_name = data["first_name"]
        last_name = data["last_name"]
        city = data["city"]["title"]  # Реализовать, если нет города
        sex = (
            "мужской" if data["sex"] == 2 else "женский"
        )  # Реализовать, если нет секса
        data_info = {
            "first_name": first_name,
            "last_name": last_name,
            "city": city,
            "sex": sex,
            "photo": take_photo(),
        }

    return data_info


# print(take_user_info())
