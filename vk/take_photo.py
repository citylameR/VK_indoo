import requests
from heapq import nlargest
from data.config import token_vk


def take_photo(user_id):
    url_id_photo = "https://api.vk.com/method/photos.get"
    params_id_photo = {
        "owner_id": user_id,
        "album_id": "profile",
        "access_token": token_vk,
        "v": "5.131",
        "extended": "1",
    }
    response_id_photo = requests.get(url_id_photo, params=params_id_photo)
    data_id_photo = response_id_photo.json()["response"]
    max_likes = []
    data_top_photo = []
    if data_id_photo["count"] >= 3:
        for photo in data_id_photo["items"]:
            max_likes.append(photo["likes"]["count"])
        for photo in data_id_photo["items"]:
            if photo["likes"]["count"] in nlargest(3, max_likes):
                photo_info = "photo{}_{}".format(user_id, photo["id"])
                data_top_photo.append(photo_info)
        return data_top_photo
    else:
        for photo in data_id_photo["items"]:
            photo_info = "photo{}_{}".format(user_id, photo["id"])
            data_top_photo.append(photo_info)
        return data_top_photo
