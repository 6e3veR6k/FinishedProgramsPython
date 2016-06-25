"""Домашнее задание №2 к уроку №3 курса Python Essential"""
import datetime

# Минимально допустимый год
MINIMAL_YEAR = 2007


class Worker(object):
    """Класс работника"""

    def __init__(self, first_name, last_name, job_title, initial_year):
        if not first_name:
            raise ValueError('first name cannot be empty')
        if not last_name:
            raise ValueError('last name cannot be empty')
        if not job_title:
            raise ValueError('job title cannot be empty')
        if not is_year_correct(initial_year):
            raise ValueError('incorrect year: {}'.format(initial_year))

        self.first_name = first_name
        self.last_name = last_name
        self.job_title = job_title
        self.initial_year = initial_year

    def __repr__(self):
        return 'Worker({first_name!r}, {last_name!r}, ' \
               '{job_title!r}, {initial_year!r})'.format_map(self.__dict__)

    @staticmethod
    def read_worker():
        """Статический метод чтения нового сотрудника с клавиатуры"""
        first_name = input('Enter first name: ')
        last_name = input('Enter last name: ')
        job_title = input('Enter job title: ')
        year = read_year('Enter year when the worker began to work: ')
        return Worker(first_name, last_name, job_title, year)


def read_int(message, check_function=None):
    """Функция безопасного чтения числа с клавиатуры
    :param message:        поясняющее сообщение
    :param check_function: функция-предикат проверки корректности либо None
    :return:               введённое значение
    """

    while True:
        try:
            value = int(input(message))
            if check_function and not check_function(value):
                raise ValueError('incorrect value')
        except ValueError as error:
            print('Error:', error)
        else:
            return value


def is_year_correct(year):
    """Функция проверки корректности года.
    Возвращает True, если заданный год входит в диапазон от года основания
    компании до текущего года.
    """
    return MINIMAL_YEAR <= year <= datetime.date.today().year


def read_year(message):
    """Функция безопасного чтения года"""
    return read_int(message, is_year_correct)


def main():
    workers_count = read_int('Count of workers: ')
    workers = []

    while len(workers) < workers_count:
        try:
            worker = Worker.read_worker()
        except ValueError as error:
            print('Error:', error)
        else:
            workers.append(worker)
        finally:
            print()

    year = read_year('Enter a year: ')

    for worker in workers:
        if worker.initial_year >= year:
            print(worker)


if __name__ == '__main__':
    main()