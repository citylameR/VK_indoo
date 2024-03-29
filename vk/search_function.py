import requests
from data.config import token_vk
import asyncio
from db import quick_commands
import datetime


def search(criteria, offset):
    offer = []
    url = "https://api.vk.com/method/users.search"
    params = {
        "access_token": token_vk,
        "fields": "city, sex, can_write_private_message, bdate",
        "v": "5.131",
        "city": criteria["city"],
        "age_from": criteria["age_min"],
        "age_to": criteria["age_max"],
        "has_photo": "1",
        "count": "20",
        "sex": criteria["sex"],
        "offset": offset
    }
    response = requests.get(url, params=params)
    if response.json()["response"]["count"] == 0:
        return None
    searched = response.json()["response"]["items"]
    loop = asyncio.get_event_loop()
    offered_list = loop.run_until_complete(quick_commands.offers(criteria["id"]))
    for result in searched:
        if not result["is_closed"]:
            if result["id"] not in offered_list:
                bl = loop.run_until_complete(quick_commands.chk_bl(result["id"]))
                if not bl:
                    try:
                        delta = datetime.datetime.today() - datetime.datetime.strptime(
                            result["bdate"], "%d.%m.%Y"
                        )
                        age = delta.days // 365
                    except:
                        age = None
                    try:
                        city = result["city"]["title"]
                        if criteria['city_title'] == city:
                            offer.append(
                                {
                                    "id": result["id"],
                                    "first_name": result["first_name"],
                                    "last_name": result["last_name"],
                                    "sex": result["sex"],
                                    "can_write": result["can_write_private_message"],
                                    "href": f'vk.com/id{result["id"]}',
                                    "city": city,
                                    "age": age
                                }
                            )
                    except:
                        pass
    return offer
