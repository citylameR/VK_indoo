from vk_api.keyboard import VkKeyboard, VkKeyboardColor

hello_keyboard = VkKeyboard(one_time=True)
hello_keyboard.add_button("Регистрация", color=VkKeyboardColor.SECONDARY)

p_keyboard = VkKeyboard(one_time=True)
p_keyboard.add_button("В избранное", color=VkKeyboardColor.POSITIVE)
p_keyboard.add_button("Следующий", color=VkKeyboardColor.PRIMARY)
p_keyboard.add_line()
p_keyboard.add_button("Пожаловаться", color=VkKeyboardColor.NEGATIVE)
p_keyboard.add_button("Меню", color=VkKeyboardColor.SECONDARY)

keyboard_sex = VkKeyboard(one_time=True)
keyboard_sex.add_button("Мужчин", color=VkKeyboardColor.PRIMARY)
keyboard_sex.add_button("Девушек", color=VkKeyboardColor.NEGATIVE)

register_keys = VkKeyboard(one_time=True)
register_keys.add_button("Да!", color=VkKeyboardColor.POSITIVE)
register_keys.add_button("Поменять", color=VkKeyboardColor.SECONDARY)

menu_keys = VkKeyboard(one_time=True)
menu_keys.add_button("Начать поиск", color=VkKeyboardColor.POSITIVE)
menu_keys.add_line()
menu_keys.add_button("Мой профиль", color=VkKeyboardColor.SECONDARY)
menu_keys.add_line()
menu_keys.add_button("Список избранных", color=VkKeyboardColor.PRIMARY)

profile_keys = VkKeyboard(one_time=True)
profile_keys.add_button("Имя", color=VkKeyboardColor.PRIMARY)
profile_keys.add_button("Город", color=VkKeyboardColor.POSITIVE)
profile_keys.add_line()
profile_keys.add_button("Возраст", color=VkKeyboardColor.PRIMARY)
profile_keys.add_button("Диапазон", color=VkKeyboardColor.POSITIVE)
profile_keys.add_line()
profile_keys.add_button("Пол", color=VkKeyboardColor.PRIMARY)
profile_keys.add_button("Назад", color=VkKeyboardColor.POSITIVE)

favs_keys = VkKeyboard(one_time=True)
favs_keys.add_button("Удалить из избранного", color=VkKeyboardColor.NEGATIVE)
favs_keys.add_button("Назад", color=VkKeyboardColor.SECONDARY)