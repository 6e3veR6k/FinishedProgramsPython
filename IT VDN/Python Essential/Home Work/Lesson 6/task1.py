"""Задание 1.
Даны две строки. Выведите на экран символы, которые есть в обоих строках.
"""

def main():
    first_string = input('Enter the first string: ')
    second_string = input('Enter the second string: ')
    print(''.join(set(first_string) & set(second_string)))


if __name__ == '__main__':
    main()
