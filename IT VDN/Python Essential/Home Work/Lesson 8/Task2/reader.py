"""Модуль чтения данных и подведения итогов"""

import pickle
import config


def count_sum(filename):
    sum_ = 0
    with open(filename, 'rb') as file:
        try:
            while True:
                sum_ += pickle.load(file)
        except EOFError:
            pass
    return sum_


if __name__ == '__main__':
    sum_ = count_sum(config.FILENAME)
    print('Sum =', sum_)
