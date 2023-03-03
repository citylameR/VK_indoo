def check_min_age(min_age_):
    try:
        min_age = int(min_age_)
        raise ValueError()
    except ValueError:
        self.write_msg_wk(self.id, "Вы ввели не числовое значение.")
    try:
        min_age = int(min_age_)
        if min_age < 18:
            raise ValueError()
    except ValueError:
        self.write_msg_wk(
            self.id, "Вы пока что слишком молоды для нашего бота. До свидания!."
        )
    try:
        min_age = int(min_age_)
        if min_age > 99:
            raise ValueError()
    except ValueError:
        self.write_msg_wk(
            self.id, "Вам бы на покой уже, а не в боте сидеть. До свидания!."
        )

    return int(min_age_)


def check_max_age(max_age_, min_age_):
    try:
        max_age = int(max_age_)
        raise ValueError()
    except ValueError:
        self.write_msg_wk(self.id, "Вы ввели не числовое значение.")
    try:
        max_age = int(max_age_)
        if max_age < check_min_age(min_age_):
            raise ValueError()
    except ValueError:
        self.write_msg_wk(
            self.id,
            "Измените максимальный возраст. На данный момент значение меньше минимального.",
        )
    try:
        max_age = int(max_age_)
        if max_age > 99:
            raise ValueError()
    except ValueError:
        self.write_msg_wk(
            self.id, "Вам бы на покой уже, а не в боте сидеть. До свидания!."
        )
