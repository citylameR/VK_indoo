import requests
from tokens import token_vk
import datetime


def take_user_info(user_id):
    url_id_info = "https://api.vk.com/method/users.get"
    params_id_info = {
        "access_token": token_vk,
        "user_ids": user_id,
        "fields": "city, sex, bdate",
        "name_case": "nom",
        "v": "5.131",
    }
    response_id_info = requests.get(url_id_info, params=params_id_info)
    data_id_info = response_id_info.json()["response"][0]
    info = {
        "first_name": data_id_info["first_name"],
        "last_name": data_id_info["last_name"],
        "sex": data_id_info["sex"],
        "city": 1,
        "city_title": "Москва",
        "age": None
    }
    if "bdate" in data_id_info:
        try:
            delta = datetime.datetime.today() - datetime.datetime.strptime(
                data_id_info["bdate"], "%d.%m.%Y")
            info["age"] = delta.days // 365
        except:
            info["age"] = None
    if "city" in data_id_info:
        info["city"] = data_id_info["city"]["id"]
        info["city_title"] = data_id_info["city"]["title"]
    return info
