"""Модуль генерации и записи чисел"""

import random
import config


def generate_data():
    for _ in range(config.COUNT):
        yield random.random()


def write_data(data, filename):
    with open(filename, 'w') as file:
        for number in data:
            print(number, file=file)


if __name__ == '__main__':
    data = generate_data()
    write_data(data, config.FILENAME)
