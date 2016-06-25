"""Пример использования collections.Counter"""

from collections import Counter

# collections.Counter -- это подкласс dict, предназначенный для подсчёта
# хешируемых объектов.  Также его иногда называют мультимножеством.  Элементы
# сохраняются как ключи словаря, а их количество -- как значения.

counter = Counter()
counter[1] += 1
for i in range(3):
    print(counter[i])

print()

c = Counter('abcdeabcdabcaba')  # подсчитать количество каждого символа в строке

print(c.most_common(3))         # три наиболее частых элемента
print(sorted(c))                # все уникальные элементы
print(sorted(c.elements()))     # все элементы

print(sum(c.values()))          # сумма значений

print(c['a'] )                  # количество букв 'a'

for elem in 'shazam':           # добавить новые буквы
    c[elem] += 1

print(c['a'])                   # теперь в счётчике семь букв 'a'
del c['b']                      # удалить все 'b'
print(c['b'])

d = Counter('simsalabim')       # создать новый счётчик
c.update(d)                     # добавить его элементы в первый
print(c['a'])                   # теперь в нём девять 'a'

c.clear()                       # очистить счётчик
print(c)

# внимание: если счёт элемента установить или уменьшить до нуля, он останется в
# счётчике, пока не будет удалён явно
c = Counter('aaabbc')
c['b'] -= 2
print(c.most_common())
