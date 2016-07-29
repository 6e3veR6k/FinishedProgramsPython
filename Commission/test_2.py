#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime


class AgentsAct(datetime):
    def getdate(self):
        """ Returns now datetime format %m-%d-%Y %H:%M for SQL query """
        get_date_obj = self.now()
        return get_date_obj.strftime("%m-%d-%Y %H:%M")

    def get_user_date(self, user_day=1):
        """ Return user act date """
        now = self.now()

        while True:
            try:
                user_month_int = int(input("Ведите месяц: "))
                if user_month_int in range(1, now.month + 1):
                    break
            except ValueError as Err:
                print("Введите число!!! ", Err)
                continue
        user_date = self(now.year, user_month_int, user_day)
        return user_date.strftime("%m-%d-%Y %H:%M")


date = AgentsAct()
print(date.getdate())
print(date.get_user_date())
print(date.get_user_date(10))