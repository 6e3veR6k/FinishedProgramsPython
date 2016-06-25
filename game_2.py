#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

digits_number = 4
rand_digits_list = random.sample(list(range(10)), digits_number)
print rand_digits_list

check_func = lambda number_digits: True if len(set(number_digits)) == len(number_digits) else False


def get_user_digits(number=4):
    user_str = ""
    while not (user_str.isdigit() and len(user_str) == number and check_func(user_str)):
        if len(user_str) != 0 and not user_str.isdigit():
            print "You must input digits!"
        elif len(user_str) != 0 and len(user_str) != number:
            print "You must input {} of digits!".format(number)
        elif len(user_str) != 0 and not check_func(user_str):
            print "You must input no-repeated digits!"

        user_str = "".join(raw_input("Enter your digits: ").split())
    return user_str


def compare_set(user_list, comp_list):
    number_matching_ids = 0
    number_matching_digits = 0
    for i in range(len(user_list)):
        if user_list[i] == comp_list[i]:
            number_matching_ids += 1
        elif user_list[i] in comp_list and user_list[i] != comp_list[i]:
            number_matching_digits += 1
    return [number_matching_ids, number_matching_digits]


print "Let start the game!"
print "Try to guess my 4-digits number"
score = (0, 0)

while score != (4, 0):
    score_list = compare_set(list(get_user_digits()), map(str, rand_digits_list))
    score = tuple(score_list)
    print score_list

    if score == (2, 0):
        print "You almost there!!! Keep on!"
        continue

    if score == (3, 0):
        print "Ha! You have three digits, one left!"
        continue

print "Yahoo! You win!!!"






