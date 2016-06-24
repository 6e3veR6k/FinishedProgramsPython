#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime, date
import pyodbc
import os
import sys
from numbers import Number
from decimal import Decimal


class SQL(dict):
    def __init__(self, server, database, driver='{SQL Server Native Client 11.0}', charset='utf-8', tr_connect='YES'):
        dict.__init__({})
        self.server = server
        self.database = database
        self.driver = driver
        self.charset = charset
        self.tr_connect = tr_connect
        self['DRIVER'] = self.driver
        self['CHARSET'] = self.charset
        self['TRUSTED_CONNECTION'] = self.tr_connect
        self['SERVER'] = self.server
        self['DATABASE'] = self.database

    def sql_info(self):
        return ';'.join('%s=%s' % (k, v) for k, v in self.items())


class ActDate:
    def __init__(self, period, date_month_from, date_day_from):
        self.now_date = datetime.now()
        self.period = period
        self.date_month_from = date_month_from
        self.date_day_from = date_day_from
        self.get_act_closed_period()
        self.get_act_period()

    def get_act_closed_period(self):
        """ Return when acts were closed """
        date_from = datetime(self.now_date.year, self.date_month_from, self.date_day_from, 0, 5)
        return date_from

    def get_act_period(self):
        """ Return act's period """
        date_format = date(int(self.now_date.year), period, 1)
        return date_format


def get_commission_type_gid():
    """ Return commission type GID """
    comm_type = {'1': ('BEDED8D6-159C-4DEC-869C-25416FCAD1FF', 'IKP'),
                 '2': ('8CC6A11E-9E88-48A3-9C8C-3F3EC92E16AD', 'Agent'),
                 '3': ('307AE0E6-5D38-42B8-A576-6C9619837AF9', 'Agreement author')}

    com_id = str(raw_input('Enter commission ID: '))

    while com_id not in comm_type.keys():
        print 'You must chose between 1, 2 and 3'
        for elem in comm_type:
            print 'Commission type {0} has ID: {1}'.format(comm_type[elem][1], elem)
        com_id = str(raw_input('Enter commission ID: '))

    return comm_type[com_id][0]


def get_agent_chanel():
    chanel_list = ['11', '12', '13', '14', '15', '16', '17', '18', '19', '21', '22', '31', '32', '33']
    set_chanel = str((raw_input("Enter agent's chanel: ")))
    while set_chanel not in chanel_list:
        set_chanel = str(raw_input("Try to choose agent's chanel: "))
    return set_chanel


"""
@CommissionType   0
@Period           1
@StartDate        2
@EndDate          3
@StatusGID        4
@Chanel           5
branch            6
"""

if os.path.exists('sql_query_commission_4.txt'):
    sql_file = open('sql_query_commission_4.txt')
    tsql_query_fromfile = sql_file.read()

    comm_type = get_commission_type_gid()
    now_date = datetime.now()

    period = int(raw_input('Enter act\'s period: '))
    while period > now_date.month:
        print "Not right month, try input correct month"
        period = int(raw_input('Acts for the period: '))

    date_month_from = int(raw_input('Enter month when acts were closed: '))
    while date_month_from < period or date_month_from > now_date.month:
        print "Not right month, try input correct month"
        date_month_from = int(raw_input('Enter month when acts were closed: '))

    date_day_from = int(raw_input('Enter the date when the acts started to close '))

    while date_day_from not in xrange(now_date.day):
        print "Not right day, try input correct day"
        date_day_from = int(raw_input('Enter day before acts were closed: '))

    myActDate = ActDate(period, date_month_from, date_day_from)

    act_period = myActDate.get_act_period()
    act_closed_period_from = myActDate.get_act_closed_period()
    act_closed_period_to = datetime(now_date.year, now_date.month, now_date.day, now_date.hour, now_date.minute)
    status_gid = '22C7D1EF-CFCF-4F37-8959-003C6669830A'
    chanel = get_agent_chanel()

    branch_code_list = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16',
                        '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']

    branch_code = raw_input("Enter direction code separated by spaces :")
    while branch_code not in branch_code_list and len(branch_code.split()) == 0:
        print "We don't have such direction"
    user_branch_code = branch_code.split()
    user_branch = []
    [user_branch.append(code) for code in user_branch_code if code not in user_branch and code in branch_code_list]
    sql_query = " LEFT(B.BranchCode, 2)='100' "
    for code in sorted(user_branch):
        sql_query += "OR LEFT(B.BranchCode, 2)='{0}' ".format(code)

    result = 'part _{0}k_'.format(chanel)
    result_file_name = result + '_'.join(user_branch) + '.txt'
    print result_file_name
    tsql_query_formatted = tsql_query_fromfile.format(comm_type, act_period, act_closed_period_from,
                                                      act_closed_period_to, status_gid, chanel, sql_query)

    print tsql_query_formatted
    sql_file.close()

    # db05 = SQL('hq01db05', 'Callisto')
    conn = pyodbc.connect(SQL('hq01db05', 'Callisto').sql_info())
    cursor = conn.cursor()

    temp = sys.stdout
    sys.stdout = open(result_file_name, 'wb')

    cursor.execute(tsql_query_formatted)
    row = cursor.fetchone()
    while row:
        print '\t'.join([row[i].encode('utf-8') if not isinstance(row[i], Number) else ','.join(str(row[i]).split('.'))
                         for i in range(len(row))])
        row = cursor.fetchone()
    sys.stdout.close()

    conn.close()

