import bot
from vk import vk as vkfunc
from db import quick_commands
import asyncio


def new_user(user_id, botfunc, vk_bot):
    botfunc.write_msg(
        user_id,
        "Добро пожаловать в наш сервис для знакомств!"
        "Но для начала, давайте познакомимся с вами!",
    )
    info = vkfunc.take_user_info(user_id)
    register = bot.registration.Registration(user_id, info, vk_bot)
    info["first_name"] = register.getname()
    botfunc.write_msg(user_id, "Отлично! С именем определились!")
    info["city"] = register.getcity()
    botfunc.write_msg(user_id, "Замечательно! Продолжим!")
    info["age"] = int(register.getage())
    info["sex"] = register.getsex()
    botfunc.write_msg(user_id, "Осталось совсем чуть-чуть!")
    info["age_min"] = int(register.getage_min())
    info["age_max"] = int(register.getage_max())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        quick_commands.add_user(
            user_id=user_id,
            first_name=info["first_name"],
            last_name=info["last_name"],
            city=info["city"],
            age=info["age"],
            age_min=info["age_min"],
            age_max=info["age_max"],
            sex=info["sex"],
        )
    )
    botfunc.write_msg(user_id, "Процесс регистрации наконец-то завершён")
