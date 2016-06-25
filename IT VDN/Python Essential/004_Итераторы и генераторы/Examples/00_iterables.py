"""
Примеры некоторых стандартных итерабельных объектов.
Пример 1: список
"""

# Список
my_list = [1, 2, 5, 7, 32, 148]

# Обход списка
for element in my_list:
    print(element)

# Функция enumerate возвращает итерабельный объект, который возвращает пары индекс-значение
for index, element in enumerate(my_list):
    print('my_list[{}] = {}'.format(index, element))
