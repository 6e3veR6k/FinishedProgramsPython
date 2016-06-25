"""Модуль основной логики приложения.
Предоставляет класс LinksDB -- хранилище ссылок.
"""

from urllib.parse import urlparse
import os.path
import shelve

class LinksDB(object):
    """Хранилище ссылок"""

    def __init__(self):
        """Конструктор класса"""

        self._db_name = os.path.join('database', 'links_db')

    def get_url(self, name):
        """Метод получения ссылки по имени.
        Выбрасывает KeyError, если имя не найдено."""

        with shelve.open(self._db_name) as db:
            return db[name]

    def set_url(self, name, url):
        """Метод добавления новой ссылки.
        Выбрасывает KeyError, если имя уже существует или пустое.
        Выбрасывает ValueError, если URL пустой или некорректный."""

        url = self.normalize_url(url)

        if not name:
            raise KeyError('Link name cannot be empty', name)
        if not url:
            raise ValueError('Invalid link URL', url)

        with shelve.open(self._db_name) as db:
            if name in db:
                raise KeyError('Link already exists', name)
            db[name] = url

    def normalize_url(self, url):
        """Метод, который добавляет протокол, если он отсутствует,
        и возвращает исправленный или исходный URL, если он корректный,
        или None в ином случае."""

        if not urlparse(url).scheme:
            url = 'http://' + url
        if urlparse(url).netloc:
            return url
        else:
            return None
