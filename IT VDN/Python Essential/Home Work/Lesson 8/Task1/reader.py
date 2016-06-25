"""Модуль чтения данных и подведения итогов"""

import config


def count_sum(filename):
    sum_ = 0
    with open(filename, 'r') as file:
        for line in file:
            sum_ += float(line)
    return sum_


if __name__ == '__main__':
    sum_ = count_sum(config.FILENAME)
    print('Sum =', sum_)
