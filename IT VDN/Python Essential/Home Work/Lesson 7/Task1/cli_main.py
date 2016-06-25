"""Модуль консольного интерфейса приложения"""

from links_db import LinksDB


def add_link_to(links):
    """Функция добавления новой ссылки в хранилище links"""
    
    while True:
        short_name = input('Enter short name: ')
        original_url = input('Enter url: ')

        try:
            links.set_url(short_name, original_url)
        except (KeyError, ValueError) as error:
            print(error.args[0])
        else:
            break


def get_link_from(links):
    """Функция получения ссылки из хранилища links"""

    name = input('Enter link name: ')

    try:
        url = links.get_url(name)
    except KeyError:
        print('Link does not exist')
    else:
        print(url)


def main():
    """Главная функция приложения"""

    links = LinksDB()

    while True:
        print('1. Add link')
        print('2. Get link')
        print('3. Exit')

        choice = input('> ')
        if choice == '1':
            add_link_to(links)
        elif choice == '2':
            get_link_from(links)
        elif choice == '3':
            break
        else:
            print('Incorrect input')

        print()


if __name__ == '__main__':
    main()