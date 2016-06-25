# -*- coding: utf-8 -*-

class Editor(object):
    """Базовый класс редактора"""

    def view_document(self):
        print('Viewing some document')

    def edit_document(self):
        print('Editing documents is unavailable in the free version')


class ProEditor(Editor):
    """Класс платной версии редактора"""

    def edit_document(self):
        print('Editing some document')


def main():
    key = input('Enter license key: ')
    if key == 'QA42FX-JXJ8':
        print('Product activated.')
        editor = ProEditor()
    else:
        print('Incorrect license key, reverting to the free version.')
        editor = Editor()

    editor.view_document()
    editor.edit_document()


if __name__ == '__main__':
    main()