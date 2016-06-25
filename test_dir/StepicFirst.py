class EvenLengthMixin:
    def even_length(self):
        return len(self) % 2 == 0


class MyList(list, EvenLengthMixin):
    pass

x = MyList()
print x
x.extend([1, 2, 3, 9, 1, 10])
print x
print x.even_length()

# issubclass(A, D)
# check if first class is subclass second
# if A(B,C) and B(D, C) then A is subclass D

print MyList.mro()
