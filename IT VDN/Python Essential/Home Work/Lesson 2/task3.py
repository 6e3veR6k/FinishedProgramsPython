# -*- coding: utf-8 -*-

class GraphicalObject(object):
    pass


class Rectangle(GraphicalObject):
    pass


class Clickable(object):
    pass


class Button(Rectangle, Clickable):
    pass


def main():
    print(GraphicalObject.mro())
    print(Rectangle.mro())
    print(Clickable.mro())
    print(Button.mro())

if __name__ == '__main__':
    main()
