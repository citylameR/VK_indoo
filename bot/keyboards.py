from vk_api.keyboard import VkKeyboard, VkKeyboardColor

hello_keyboard = VkKeyboard(one_time=True)
hello_keyboard.add_button("Регистрация", color=VkKeyboardColor.SECONDARY)

p_keyboard = VkKeyboard(one_time=True)
p_keyboard.add_button("В избранное", color=VkKeyboardColor.POSITIVE)
p_keyboard.add_button("Следующий", color=VkKeyboardColor.POSITIVE)
p_keyboard.add_line()
p_keyboard.add_button("В черный список", color=VkKeyboardColor.NEGATIVE)
p_keyboard.add_button("Меню", color=VkKeyboardColor.SECONDARY)

keyboard_sex = VkKeyboard(one_time=True)
keyboard_sex.add_button("Мужчин", color=VkKeyboardColor.POSITIVE)
keyboard_sex.add_button("Девушек", color=VkKeyboardColor.NEGATIVE)

register_keys = VkKeyboard(one_time=True)
register_keys.add_button("Да!", color=VkKeyboardColor.POSITIVE)
register_keys.add_button("Поменять", color=VkKeyboardColor.NEGATIVE)

menu_keys = VkKeyboard(one_time=True)
menu_keys.add_button("Начать поиск", color=VkKeyboardColor.SECONDARY)
menu_keys.add_line()
menu_keys.add_button("Настройки профиля", color=VkKeyboardColor.SECONDARY)
menu_keys.add_line()
menu_keys.add_button("Список избранных", color=VkKeyboardColor.SECONDARY)
