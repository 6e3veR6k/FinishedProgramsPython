"""Задание 1"""


def average(*numbers):
    """Среднее арифметическое заданных чисел"""
    return sum(numbers) / len(numbers)


def main():
    print(average(4, 8, 3))
    print(average(*range(10)))


if __name__ == '__main__':
    main()