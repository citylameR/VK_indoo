import bot
import vk
from db import quick_commands
import asyncio


def new_user(user_id, botfunc, vk_bot):
    botfunc.write_msg(
        user_id,
        "Добро пожаловать в наш сервис для знакомств!\n"
        "Но для начала, давайте познакомимся с вами!",
    )
    info = vk.user_info.take_user_info(user_id)
    register = bot.registration.Registration(user_id, info, vk_bot)
    info["first_name"] = register.getname()
    botfunc.write_msg(user_id, "Отлично! С именем определились!")
    city = register.getcity()
    info["city"] = city["id"]
    info["city_title"] = city["title"]
    botfunc.write_msg(user_id, "Замечательно! Продолжим!")
    info["age"] = int(register.getage())
    info["sex"] = register.getsex()
    botfunc.write_msg(user_id, "Осталось совсем чуть-чуть!")
    info["age_min"] = int(register.getage_min())
    info["age_max"] = int(register.getage_max(info["age_min"]))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        quick_commands.add_user(
            user_id=user_id,
            first_name=info["first_name"],
            last_name=info["last_name"],
            city=info["city"],
            city_title=info["city_title"],
            age=info["age"],
            age_min=info["age_min"],
            age_max=info["age_max"],
            sex=info["sex"]
        )
    )

    botfunc.write_msg(user_id, "Процесс регистрации, наконец-то, завершён! :)")
