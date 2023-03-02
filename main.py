import bot
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from data import config
from db.dp_gino import db
import asyncio
from db import quick_commands
import db


if __name__ == "__main__":
    vk_bot = vk_api.VkApi(token=config.token_bot)
    botfunc = bot.funcs.Botfuncs(vk_bot)
    print("Bot started succesfully")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(db.dp_gino.on_startup())
    print("Connected to database successfully")
    longpoll = VkLongPoll(vk_bot)
    active_session = []
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                if event.user_id not in active_session:
                    active_session.append(event.user_id)
                    info = loop.run_until_complete(
                        quick_commands.select_user(event.user_id)
                    )
                    bot.mainmenu.mainmenu(event.user_id, vk_bot, info)
