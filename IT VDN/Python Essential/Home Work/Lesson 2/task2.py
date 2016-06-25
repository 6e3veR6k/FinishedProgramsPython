# -*- coding: utf-8 -*-

class GraphicalObject(object):
    """ Класс графического объекта
    """

    def click(self):
        try:
            self.on_click()
        except AttributeError:
            print(self.__class__.__name__, 'is not clickable')

class Rectangle(GraphicalObject):
    """ Класс прямоугольника с опциональным текстом
    """

    def __init__(self, width, height, text=''):
        super().__init__()

        self.width = width
        self.height = height
        self.text = text

    def draw(self):
        if self.text:
            padded_text = ' ' + self.text + ' '
        else:
            padded_text = self.text
        padded_text_len = len(padded_text)

        left_padding = round((self.width - padded_text_len) / 2)
        left = '*' * left_padding
        right = '*' * (self.width - left_padding - padded_text_len)

        for i in range(self.height):
            if i == round(self.height / 2):
                print(left, padded_text, right, sep='')
            else:
                print('*' * self.width)


class Clickable(object):
    """ Класс объекта - обработчика нажатия мыши
    """

    def on_click(self):
        print(self.__class__.__name__, 'clicked')


class Button(Rectangle, Clickable):
    """ Класс кнопки
    """
    def __init__(self, width=25, height=5, text=None):
        if text is None:
            text = self.__class__.__name__
        super().__init__(width, height, text)


def main():
    rect = Rectangle(20, 5)
    rect.draw()
    rect.click()

    print()

    button = Button()
    button.draw()
    button.click()

if __name__ == '__main__':
    main()