"""Модуль веб-сервера (для тех, кто разобрал соответствующую
реализацию в материалах к предыдущему уроку)
"""

from flask import Flask, abort, redirect
from flask import render_template, request
from links_db import LinksDB


links = LinksDB()  # создание глобального хранилища
app = Flask(__name__)  # создание объекта веб-приложения


@app.route('/', methods=['GET', 'POST'])
def create_link():
    """Контроллер создания новой ссылки"""

    error_message = None
    name = ''
    url = 'http://'
    success_message = None
    
    if request.method == 'POST':
        name = request.form['name']
        url = request.form['url']

        try:
            links.set_url(name, url)
        except (KeyError, ValueError) as error:
            error_message = error.args[0]
        else:
            success_message = 'Link added successfully'
    
    return render_template('add_link.html',
                           name=name, url=url,
                           error=error_message,
                           success=success_message)


@app.route('/<name>')
def go_to_link(name):
    """Контроллер перехода по ссылке"""

    try:
        url = links.get_url(name)
    except KeyError:
        abort(404)

    return redirect(url)


if __name__ == '__main__':
    app.run('0.0.0.0', 8000)
