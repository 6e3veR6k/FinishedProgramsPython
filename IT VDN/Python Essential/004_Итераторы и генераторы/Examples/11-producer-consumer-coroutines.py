"""
Сопрограмма (англ. coroutine) — компонент программы, обобщающий понятие
подпрограммы, который дополнительно поддерживает множество входных точек
(а не одну, как подпрограмма) и остановку и продолжение выполнения с
сохранением определённого положения.

Здесь показан пример такого шаблона использования сопрограмм, как
consumer-producer.
"""


import time
import random


def sleep(seconds):
    """Сопрограмма, которая приостанавливает сопрограмму,
    из которой была вызвана, на заданное количество секунд"""

    initial_time = time.time()
    while time.time() - initial_time < seconds:
        yield


def gen_data():
    """Функция генерации данных (например, показания с какого-то датчика)"""

    return random.randint(0, 100)


def consume():
    """Сопрограмма обработки данных"""

    running_sum = 0
    count = 0

    while True:
        data = yield
        running_sum += data
        count += 1
        print('Got data: {}\nTotal count: {}\nAverage: {}\n'.format(
            data, count, running_sum / count))


def produce(consumer):
    """Сопрограмма выдачи данных"""

    while True:
        yield from sleep(0.5)
        data = gen_data()
        consumer.send(data)
        yield


def main():
    # Создание обработчика данных
    consumer = consume()
    # Запуск сопрограммы
    consumer.send(None)

    # Создание производителя данных
    producer = produce(consumer)

    # Цикл событий (event loop)
    while True:
        next(producer)


if __name__ == '__main__':
    main()