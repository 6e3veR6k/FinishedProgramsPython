#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

number = list(range(10))
comp_number = random.sample(number, 4) # как работает random.sample(), какой обьект возвращает
print comp_number


def ch(string):
    for el in string:
        if string.count(el) not in (0, 1):
            return False
    return True


def user_number():
    user_choice = raw_input("Enter four-digits number: ")
    user_num = ''.join(user_choice.split())

    if len(user_num) == 4 and user_num.isdigit() and ch(user_num):
        return user_num
    else:
        print "Try something else"
        return user_number()



def compare(user_list, comp_list):
    id_num = 0
    count_num = 0
    for i in range(len(user_list)):
        if user_list[i] == comp_list[i]:
            id_num += 1
        if user_list[i] in comp_list and user_list[i] != comp_list[i]:
            count_num += 1
    return [id_num, count_num]

user_try = compare(user_number(), comp_number)
print user_try
while user_try != [4, 0]:
    user_try = compare(user_number(), comp_number)
    print user_try


print "You win!!!"


