"""
Генераторы во многих случаях позволяют просто и удобно создавать итераторы.

Функция-генератор (generator function) – это функция, которая возвращает
специальный итератор-генератор (generator iterator)  (также объект-генератор –
generator object). Она характеризуется наличием ключевого слова yield
внутри функции.

Термин генератор (generator), в зависимости от контекста, может означать
либо функцию-генератор, либо итератор-генератор (чаще всего, последнее).

Методы __iter__ и __next__ у генераторов создаются автоматически.

Этот пример является модифицированным примером 05-iterator.py, в котором
вместо явного описания итератора используется генератор.
"""


def my_range(first, second=None, step=1):
    """Функция-генератор, работающая подобно стандартному классу range"""

    if second is None:
        current = 0
        end = first
    else:
        current = first
        end = second

    if step == 0:
        raise ValueError('step must not be zero')

    while (step > 0 and current < end) or (step < 0 and current > end):
        # yield выдаёт текущее значение и приостанавливает работу генератора.
        # При следующем вызове next выполнение продолжится с этого места.
        yield current
        current += step


def test_iterator():
    """Функция тестирования итератора"""

    radius = 30

    try:
        for start in range(-radius, radius + 1):
            for end in range(-radius, radius + 1):
                for step in range(-radius, radius + 1):
                    if step == 0:
                        continue

                    gen_range = my_range(start, end, step)
                    std_range = range(start, end, step)

                    # Получение списков значений
                    gen_range_values = list(gen_range)
                    std_range_values = list(std_range)

                    assert gen_range_values == std_range_values
    except AssertionError:
        print('Test failed')
        print('start =', start)
        print('end =', end)
        print('step =', step)
        print('gen_range_values =', gen_range_values)
        print('std_range_values =', std_range_values)
        print()
    else:
        print('iter tests passed normally')


def main():
    # Простая проверка генератора
    for i in my_range(10):
        print(i)

    print()

    # Использование генератора напрямую
    generator = my_range(2, 8, 2)
    try:
        while True:
            print(next(generator))
    except StopIteration:
        print()

    # Тестирование генератора
    test_iterator()


if __name__ == '__main__':
    main()