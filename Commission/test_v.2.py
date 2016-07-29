#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime

now_datetime = datetime.now()
formatted_now_datetime = now_datetime.strftime("%Y-%m-%d %H:%M")


def check_user_date(value_start, value_end):
    while True:
        try:
            user_int_value = int(input(" "))
            if user_int_value in range(value_start, value_end):
                break
            else:
                print("Не верное значение.")
                continue
        except ValueError as Err:
            print("Введите число!!! ", Err)
            continue
    return user_int_value

# period
print("Введите период актов: ", end='')
month_period = check_user_date(1, now_datetime.month + 1)
period = datetime(now_datetime.year, month_period, 1)

# start date
print("Введите месяц закрытия актов: ", end='')
month_closed = check_user_date(period.month, now_datetime.month + 1)
print("Введите день закрытия актов: ", end=''),
day_closed = check_user_date(1, now_datetime.day)
start_date = datetime(now_datetime.year, month_closed, day_closed)

# end date
end_date = formatted_now_datetime
print("Период закрытия актов между {0} и {1}. За период {2}".format(start_date, end_date, period.strftime("%Y-%m-%d")))




"""
tmp = "%m-%y"
datetamplate = "{d}-{m}-{y}"
datetmplt = "%d-%m-%y"


user_month = input("Enter act\'s month ")
user_year = input("Enter act\'s year ")

act_date = "{m}-{y}".format(m=user_month, y=user_year)



date_time_obj = datetime.strptime(act_date, tmp)

print("Act\'s month", date_time_obj.strftime(tmpf))
print("Now date and time", date_time_now.strftime(tmpf))

act_closed_month = input("Enter month when acts were closed \t")
act_closed_day = input("Enter day acts were closed \t")


act_closed_date_format = datetamplate.format(d=act_closed_day, m=act_closed_month, y=user_year)

act_closed_date_obj = datetime.strptime(act_closed_date_format, datetmplt)

print("Acts were closed", act_closed_date_obj.strftime(tmpf))
print(act_closed_date_obj > date_time_obj)
"""
