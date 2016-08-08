#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Попробовать сделать программу выполняемой в цыкле
# чтобы каждый раз не вводить заново значения даты и периода

from datetime import datetime
import os
import pymssql
import decimal

"""
@CommissionTypeGID  -   '{0}'   +
@Period             -   '{1}'
@StartDate          -   '{2}'
@EndDate            -   '{3}'
@StatusGID          -   '{4}'   +
@Chanel             -   '{5}'   +
@BranchCode : ({6})             +
"""

# @CommissionTypeGID
comm_type = {
    1: ('BEDED8D6-159C-4DEC-869C-25416FCAD1FF', "ІКП"),
    2: ('8CC6A11E-9E88-48A3-9C8C-3F3EC92E16AD', "Агент"),
    3: ('307AE0E6-5D38-42B8-A576-6C9619837AF9', "Автор угоди")
}

# @StatusGID
status_gid = {
    1: ("22C7D1EF-CFCF-4F37-8959-003C6669830A", "Затверджений"),
    2: ("6A328C2F-E582-4334-A6EA-57A1CE6E4D0F", "На узгодженні"),
    3: ("52AE0988-A1AA-4DDD-AF55-E10B7A067EEB", "Новий"),
    4: ("8E8AD750-E856-4CB6-B788-F9C0A8321EF9", "Сторно")
}

# @Chanel
chanel_list = (11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 31, 32, 33)

# @BranchCode
branch_code = {
    1: "Кримська республіканська дирекція НАСК \"Оранта\"",
    2: "Вінницька обласна дирекція НАСК \"Оранта\"",
    3: "Волинська обласна дирекція НАСК \"Оранта\"",
    4: "Дніпропетровська обласна дирекція НАСК \"Оранта\"",
    5: "Маріупольська дирекція НАСК \"Оранта\"",
    6: "Житомирська обласна дирекція НАСК \"Оранта\"",
    7: "Закарпатська обласна дирекція НАСК \"Оранта\"",
    8: "Запорізька обласна дирекція НАСК \"Оранта\"",
    9: "Івано-Франківська обласна дирекція НАСК \"Оранта\"",
    10: "Київська обласна дирекція НАСК \"Оранта\"",
    11: "Кіровоградська обласна дирекція НАСК \"Оранта\"",
    12: "Луганська обласна дирекція НАСК \"Оранта\"",
    13: "Львівська обласна дирекція НАСК \"Оранта\"",
    14: "Миколаївська обласна дирекція НАСК \"Оранта\"",
    15: "Одеська обласна дирекція НАСК \"Оранта\"",
    16: "Полтавська обласна дирекція НАСК \"Оранта\"",
    17: "Рівненська обласна дирекція НАСК \"Оранта\"",
    18: "Сумська обласна дирекція НАСК \"Оранта\"",
    19: "Тернопільська обласна дирекція НАСК \"Оранта\"",
    20: "Харківська обласна дирекція НАСК \"Оранта\"",
    21: "Херсонська обласна дирекція НАСК \"Оранта\"",
    22: "Хмельницька обласна дирекція НАСК \"Оранта\"",
    23: "Черкаська обласна дирекція НАСК \"Оранта\"",
    24: "Чернівецька обласна дирекція НАСК \"Оранта\"",
    25: "Чернігівська обласна дирекція НАСК \"Оранта\"",
    26: "Київська міська дирекція НАСК \"Оранта\"",
    27: "Севастопольська міська дирекція НАСК \"Оранта\"",
    28: "Донецька обласна дирекція НАСК \"Оранта\"",
    29: "Головний офіс",
    30: "ДБС НАСК \"Оранта\"",
    31: "Апарат дирекції"
}


def template(file_name):
    """ Read txt file in the same directory """
    try:
        with open(file_name, "r") as data_file:
            return data_file.read()
    except IOError as err:
        print("File error: " + str(err))


def get_gid(gid_dict, user_gid=None):
    """ Gets gid number depend user's choice """
    # user_gid = ''
    while user_gid not in gid_dict:
        print("Список доступных значений: ")
        for key, value in gid_dict.items():
            print(key, " - ", value[1])
        if user_gid:
            print("Значение не найдено. Выберите значение из списка: ")
            for key, value in gid_dict.items():
                print("{} - {}".format(key, value[1]))
        user_gid = int(input("Введите значение: "))
    return gid_dict[user_gid][0]


def get_unique(sequence, count=1):
    """ Collect unique items from sequence """
    user_list = []
    while len(user_list) != count:
        try:
            user_id = input(" ")
            if user_id and int(user_id) in sequence:
                if int(user_id) not in user_list and len(user_list) != count:
                    user_list.append(int(user_id))
                elif int(user_id) in user_list and len(user_list) != count:
                    print("Такое значение уже существует.")
                else:
                    break
            elif user_id and len(user_list) != count:
                print("Вашего значения нет в списке допустимых.")
                continue
            else:
                break
        except ValueError as Err:
            print("Введите число!!! ", Err)
            continue

    return user_list


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


if __name__ == '__main__':

    # commission type and acts' status
    comm_type_gid = get_gid(comm_type)
    comm_status_gid = get_gid(status_gid, 1)

    # period
    print("За какой месяц акты?: ", end='')
    month_period = check_user_date(1, now_datetime.month + 1)
    period = datetime(now_datetime.year, month_period, 1)

    # start date
    print("В каком месяце закрытыли акты?: ", end='')
    month_closed = check_user_date(period.month, now_datetime.month + 1)
    print("А день закрытия актов?: ", end='')
    day_closed = check_user_date(1, now_datetime.day)
    start_date = datetime(now_datetime.year, month_closed, day_closed, 0, 5)

    # end date
    end_date = formatted_now_datetime

    # channel
    # на самом деле тут херня, если поменяется тип возвращаемого значения с листа в инт получим ошибку
    print("Введите канал агента", end='')
    chanel = get_unique(chanel_list)[0]

    # branch
    print("Дирекция? ", end='')
    branch_code_lst = get_unique(branch_code, len(branch_code))

    # formatted query
    branch_text = " ".join(["OR LEFT(B.BranchCode, 2)='{:02}'".format(code) for code in sorted(branch_code_lst)])

    # query from file
    query_text = template("sql_query_commission_4.txt").format(comm_type_gid,
                                                               period.strftime("%Y-%m-%d"),
                                                               start_date.strftime("%Y-%m-%d %H:%M"),
                                                               end_date,
                                                               comm_status_gid,
                                                               chanel,
                                                               branch_text
                                                               )

    if chanel in [22, 18, 17, 15] and comm_type_gid == comm_type[1][0]:
        output_file = 'part_СПД_ІКП_{}дир_дострокова.txt'.format('_'.join(["{:02}".format(code) for code
                                                                           in sorted(branch_code_lst)]))
    elif chanel in [22, 18]:
        output_file = 'part_СПД_{}дир_дострокова.txt'.format('_'.join(["{:02}".format(code) for code
                                                                       in sorted(branch_code_lst)]))
    else:
        output_file = 'part_{}к_{}дир_дострокова.txt'.format(chanel, '_'.join(["{:02}".format(code) for code
                                                                               in sorted(branch_code_lst)]))

    parts = []
    sum_info = {}

    with open(output_file, "w") as outfile:
        conn = pymssql.connect(server='hq01db05', database='Callisto')
        cursor = conn.cursor()

        try:
            cursor.execute(query_text)
            row = cursor.fetchone()
            while row:
                # print("\t".join([col for col in row]))
                outfile.write('\t'.join([str(r) if not isinstance(r, decimal.Decimal) else str(r).replace('.', ',')
                                         for r in row]) + '\n')
                if row[0] not in sum_info:
                    sum_info[row[0]] = list(row)[1:]
                else:
                    sum_info[row[0]][2] += row[3]
                    sum_info[row[0]][3] += row[4]

                parts.append(row[1].split()[0])
                row = cursor.fetchone()
        except Exception as Err:
            print(Err)

    print('*' * 80)
    print('*' * 80)
    for el in sum_info:
        print("{2}\t{3}\t{0:16}\t{1}".format(sum_info[el][0], sum_info[el][3], sum_info[el][6], sum_info[el][7]))
    print('*' * 80)
    print('*' * 80)

    new_outFile = output_file.replace("part", "_".join(set(parts)))
    os.rename(output_file, new_outFile) if len(new_outFile) <= 200 else 0
