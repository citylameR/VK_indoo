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
                return city
            elif req == "Да!":
                return self.info["city"]
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
            check = ''
            while True:
                if check == 'pass':
                    return age
                elif check == 'young':
                    self.botfunc.write_msg(self.id, "Вы пока что слишком молоды для нашего бота :(")
                elif check == 'old':
                    self.botfunc.write_msg(self.id, "Вам бы на покой уже, а не в боте сидеть :)")
                elif check == 'error':
                    self.botfunc.write_msg(self.id, "Я Вас не понимаю :(\nПопробуйте ещё раз!")
                age = self.botfunc.listen()
                check = bot.age_check.chk_min(age)
        self.botfunc.write_msg_wk(
            self.id, f'Ваш возраст {self.info["age"]}?', keys.register_keys
        )
        req = self.botfunc.listen()
        while True:
            if req == "Поменять":
                self.botfunc.write_msg(self.id, "Сколько тебе лет?")
                check = ''
                while True:
                    if check == 'pass':
                        return age
                    elif check == 'young':
                        self.botfunc.write_msg(self.id, "Вы пока что слишком молоды для нашего бота :(")
                    elif check == 'old':
                        self.botfunc.write_msg(self.id, "Вам бы на покой уже, а не в боте сидеть :)")
                    elif check == 'error':
                        self.botfunc.write_msg(self.id, "Я Вас не понимаю :(\nПопробуйте ещё раз!")
                    age = self.botfunc.listen()
                    check = bot.age_check.chk_min(age)
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
        check = ''
        while True:
            if check == 'pass':
                return min_age
            elif check == 'young':
                self.botfunc.write_msg(self.id, "Это  слишком маленький возраст :(\n"
                                                "Давайте попробуем поискать кого-нибудь постарше")
            elif check == 'old':
                self.botfunc.write_msg(self.id, "У нас таких нет :(\nПопробуйте помладше :)")
            elif check == 'error':
                self.botfunc.write_msg(self.id, "Я Вас не понимаю :(\nПопробуйте ещё раз!")
            min_age = self.botfunc.listen()
            check = bot.age_check.chk_min(min_age)
        return min_age

    def getage_max(self, age_min):
        self.botfunc.write_msg(
            self.id, "Теперь введите максимальный возраст для поиска:"
        )
        check = ''
        while True:
            if check == 'pass':
                return max_age
            elif check == 'smaller':
                self.botfunc.write_msg(self.id, "Максимальный возраст не может быть меньше минимального :)")
            elif check == 'old':
                self.botfunc.write_msg(self.id, "У нас таких нет :(\nПопробуйте помладше :)")
            elif check == 'error':
                self.botfunc.write_msg(self.id, "Я Вас не понимаю :(\nПопробуйте ещё раз!")
            max_age = self.botfunc.listen()
            check = bot.age_check.chk_max(age_min, max_age)
        return max_age
