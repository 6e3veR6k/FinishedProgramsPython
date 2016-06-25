"""Модуль генерации и записи чисел"""

import random
import pickle
import config


def generate_data():
    for _ in range(config.COUNT):
        yield random.random()


def write_data(data, filename):
    with open(filename, 'wb') as file:
        for number in data:
            pickle.dump(number, file)


if __name__ == '__main__':
    data = generate_data()
    write_data(data, config.FILENAME)
