import bot
import bot.keyboards as keys
import vk


class Registration:
    def __init__(self, id: int, info: dict, vk_bot):
        self.id = id
        self.info = info
        self.botfunc = bot.funcs.Botfuncs(vk_bot)

    def getname(self):
        self.botfunc.write_msg_wk(
            self.id, f'Вас зовут {self.info["first_name"]}?', keys.register_keys
        )
        req = self.botfunc.listen()
        while True:
            if req == "Поменять":
                self.botfunc.write_msg(self.id, "Как Вас зовут?")
                return self.botfunc.listen()
            elif req == "Да!":
                return self.info["first_name"]
            self.botfunc.write_msg_wk(
                self.id,
                "Я вас не понимаю :(\nДавайте попробуем ещё раз!",
                keys.register_keys,
            )
            req = self.botfunc.listen()

    def getcity(self):
        self.botfunc.write_msg_wk(
            self.id, f'Ваш город {self.info["city"]["title"]}?', keys.register_keys
        )
        req = self.botfunc.listen()
        while True:
            if req == "Поменять":
                self.botfunc.write_msg(self.id, "В каком городе будем искать?")
                city = vk.getcityindex.get_city_index(self.botfunc.listen())
                self.botfunc.write_msg(self.id, f'Установлен город {city["title"]}!')
                return city["id"]
            elif req == "Да!":
                return self.info["city"]["id"]
            self.botfunc.write_msg_wk(
                self.id,
                "Я вас не понимаю :(\nДавайте попробуем ещё раз!",
                keys.register_keys,
            )
            req = self.botfunc.listen()

    def getage(self):
        if self.info["age"] == None:
            self.botfunc.write_msg(
                self.id, "Мне не увидеть дату рождения :(\nСколько тебе лет?"
            )
            return self.botfunc.listen()
        self.botfunc.write_msg(
            self.id, f'Ваш возраст {self.info["age"]}?', keys.register_keys
        )
        req = self.botfunc.listen()
        while True:
            if req == "Поменять":
                self.botfunc.write_msg(self.id, "Сколько тебе лет?")
                return self.botfunc.listen()
            elif req == "Да!":
                return self.info["age"]
            self.botfunc.write_msg_wk(
                self.id,
                "Я вас не понимаю :(\nДавайте попробуем ещё раз!",
                keys.register_keys,
            )
            req = self.botfunc.listen()

    def getsex(self):
        self.botfunc.write_msg_wk(self.id, "Кого будем искать?)", keys.keyboard_sex)
        req = self.botfunc.listen()
        while True:
            if req == "Мужчин":
                return 2
            elif req == "Девушек":
                return 1
        self.botfunc.write_msg_wk(
            self.id,
            "Я вас не понимаю :(\nДавайте попробуем ещё раз!",
            keys.keyboard_sex,
        )
        req = self.botfunc.listen()

    def getage_min(self):
        self.botfunc.write_msg(self.id, "Введите минимальный возраст для поиска:")
        return self.botfunc.listen()

    def getage_max(self):
        self.botfunc.write_msg(
            self.id, "Теперь введите максимальный возраст для поиска:"
        )
        return self.botfunc.listen()
