from vk_api.longpoll import VkLongPoll, VkEventType
from random import randrange


class Botfuncs:
    def __init__(self, vk_bot):
        self.vk_bot = vk_bot
        self.longpoll = VkLongPoll(vk_bot)

    def write_msg(self, user_id, message):
        self.vk_bot.method('messages.send', {'user_id': user_id,
                                        'message': message,
                                        'random_id': randrange(10 ** 7)})

    def write_msg_wk(self, user_id, message, my_keyboard):
        self.vk_bot.method('messages.send', {'user_id': user_id,
                                        'message': message,
                                        'random_id': randrange(10 ** 7),
                                        'keyboard': my_keyboard.get_keyboard()})

    def listen(self):
        for event in self.longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                if event.to_me:
                    request = event.text
                    return request
