from vk_api.keyboard import VkKeyboard, VkKeyboardColor

hello_keyboard = VkKeyboard(one_time=True)
hello_keyboard.add_button('Установить критерии поиска', color=VkKeyboardColor.SECONDARY)

p_keyboard = VkKeyboard(one_time=False)
p_keyboard.add_button('В избранное', color=VkKeyboardColor.POSITIVE)
p_keyboard.add_button('Следующий', color=VkKeyboardColor.POSITIVE)
p_keyboard.add_line()
p_keyboard.add_button('В черный список', color=VkKeyboardColor.NEGATIVE)
p_keyboard.add_button('Список избранных', color=VkKeyboardColor.PRIMARY)
p_keyboard.add_line()
p_keyboard.add_button('Установить критерии поиска', color=VkKeyboardColor.SECONDARY)

keyboard_sex = VkKeyboard(one_time=False)
keyboard_sex.add_button('мужской', color=VkKeyboardColor.POSITIVE)
keyboard_sex.add_button('женский', color=VkKeyboardColor.NEGATIVE)