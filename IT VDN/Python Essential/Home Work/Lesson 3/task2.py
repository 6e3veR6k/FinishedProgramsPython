"""Домашнее задание №2 к уроку №3 курса Python Essential"""


import operator  # модуль, в котором описаны функции различных операций


def input_operation():
    """Функция ввода операции. Возвращает фукнцию, которая принимает два аргумента"""
    operation = input('Enter operation (+, -, *, /, ^) or type "exit" to quit: ')
    if operation == 'exit':
        exit()
    elif operation == '+':
        return operator.add
    elif operation == '-':
        return operator.sub
    elif operation == '*':
        return operator.mul
    elif operation == '/':
        return operator.truediv
    elif operation == '^':
        return operator.pow
    else:
        raise NotImplementedError('unsupported operation')


def main():
    """Главная функция приложения"""
    while True:
        try:
            operation = input_operation()
            first_number = float(input('Enter first number: '))
            second_number = float(input('Enter second number: '))
            result = operation(first_number, second_number)
        except (ValueError, ArithmeticError, NotImplementedError) as error:
            print('Error:', error)
        else:
            print('Result:', result)
        finally:
            print()


if __name__ == '__main__':
    main()
