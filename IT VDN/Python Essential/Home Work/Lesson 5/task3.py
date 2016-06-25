"""Задание 3"""


# Значительно эффективнее в данном случае было бы
# использовать set, что вы сможете сделать после
# следующего урока.
class WordSequence(list):
    """Класс, представляющий последовательность слов"""

    _delimiters = ('.', ',', ';', ':', ' -', '- ')

    def __init__(self, text):
        words = [word.casefold() for word in WordSequence._split(text)]
        for word in words:
            if word not in self:
                self.append(word)

    @staticmethod
    def _split(text):
        """Метод разбиения текста. Эффективнее было бы использовать
        модуль re и регулярные выражения, но здесь показано решение
        с использованием изученных средств. В реальном проекте такое
        решение использовать не следует, так как для каждого разделителя
        создаётся новая копия строки."""

        string = text
        for delimiter in WordSequence._delimiters:
            string = string.replace(delimiter, ' ')
        return string.split()


def main():
    text = '''Lorem ipsum dolor sit amet, consectetur adipisicing elit.
    Quam quidem, veniam dolor ipsum sapiente ullam mollitia molestias 
    repellendus nesciunt voluptas.'''

    words = WordSequence(text)
    for word in sorted(words):
        print(word)


if __name__ == '__main__':
    main()