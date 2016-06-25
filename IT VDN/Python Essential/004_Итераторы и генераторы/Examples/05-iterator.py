"""
Пример создания итератора
"""


import math


class MyRange(object):
    """Итератор, который ведёт себя подобно встроенному классу range
    (за исключением того, что range является итерабельным объектом,
    а не итератором, и создаёт каждый раз новый итератор, так же как
    и список).
    """

    def __init__(self, first, second=None, step=1):
        if second is None:
            self.start = 0
            self.end = first
        else:
            self.start = first
            self.end = second

        if step == 0:
            raise ValueError('step must not be zero')
        else:
            self.step = step

        length = math.ceil((self.end - self.start) / self.step)
        self.length = length if length >= 0 else 0

        self.elements_returned = 0
        self.current = None

    def __len__(self):
        return self.length

    def __iter__(self):
        return self

    def __next__(self):
        if self.elements_returned >= self.length:
            raise StopIteration

        self.elements_returned += 1

        if self.current is None:
            self.current = self.start
        else:
            self.current += self.step

        return self.current

    def __repr__(self):
        if self.start == 0 and self.step == 1:
            fmt = '{end}'
        elif self.step == 1:
            fmt = '{start}, {end}'
        else:
            fmt = '{start}, {end}, {step}'
        return 'MyRange({})'.format(fmt).format(start=self.start,
                                                end=self.end,
                                                step=self.step)


def test_len():
    """Функция тестирования метода len"""

    radius = 30

    try:
        for start in range(-radius, radius + 1):
            for end in range(-radius, radius + 1):
                for step in range(-radius, radius + 1):
                    if step == 0:
                        continue

                    my_range = MyRange(start, end, step)
                    std_range = range(start, end, step)

                    # Оператор assert проверяет, что заданное выражение
                    # истинно, и если нет, выбрасывает исключение AssertionError
                    assert len(my_range) == len(std_range)
    except AssertionError:
        print('Test failed')
        print('start =', start)
        print('end =', end)
        print('step =', step)
        print('len(my_range) =', len(my_range))
        print('len(std_range) =', len(std_range))
        print()
    else:
        print('__len__ tests passed normally')


def test_iterator():
    """Функция тестирования итератора"""

    radius = 30

    try:
        for start in range(-radius, radius + 1):
            for end in range(-radius, radius + 1):
                for step in range(-radius, radius + 1):
                    if step == 0:
                        continue

                    my_range = MyRange(start, end, step)
                    std_range = range(start, end, step)

                    # Получение списков значений
                    my_range_values = list(my_range)
                    std_range_values = list(std_range)

                    assert my_range_values == std_range_values
    except AssertionError:
        print('Test failed')
        print('start =', start)
        print('end =', end)
        print('step =', step)
        print('my_range_values =', my_range_values)
        print('std_range_values =', std_range_values)
        print()
    else:
        print('iter tests passed normally')


def main():
    # Простая проверка итератора
    for i in MyRange(10):
        print(i)

    print()

    # Использование итератора напрямую
    iterator = MyRange(2, 8, 2)
    try:
        while True:
            print(next(iterator))
    except StopIteration:
        print()

    # Тестирование метода __len__
    test_len()

    # Тестирование итератора
    test_iterator()


if __name__ == '__main__':
    main()