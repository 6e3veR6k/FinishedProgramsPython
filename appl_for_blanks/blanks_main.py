#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pyodbc


class SQL:
    def __init__(self, server, database):
        self.sql_info(server, database)

    def sql_info(self, server, database):
        self.serverInfo = dict()
        self.serverInfo['DRIVER'] = '{SQL Server Native Client 11.0}'
        self.serverInfo['CHARSET'] = 'utf-8'
        self.serverInfo['TRUSTED_CONNECTION'] = 'YES'
        self.serverInfo['SERVER'] = server
        self.serverInfo['DATABASE'] = database

        self.sqlInfo = ';'.join('%s=%s' % (k, v) for k, v in self.serverInfo.items())


db05 = SQL('hq01db05', 'DWH')


conn = pyodbc.connect(db05.sqlInfo)



file = open('blanks_branch.txt')
query = file.read()

str_period = '20160300'
int_blank_status = 8

# 8 – підписано (part(01)
# 1 – зіпсовано (part02)
# 6 – втрачено (part03)
# 3 – знищено (part04)

sql_query = query.format(str_period, int_blank_status)

cursor = conn.cursor()
cursor.execute(sql_query)

row = cursor.fetchone()

fileResult = open('result.txt', 'w')

while row:
    for i in range(len(row)):
        u = row[i]
        if isinstance(u, basestring):
            if type(u) == str:
                fileResult.write(u)
                fileResult.write('\t')
            else:
                fileResult.write(u.encode('utf-8'))
                fileResult.write('\t')
        elif u == None:
            fileResult.write('None')
            fileResult.write('\t')

    fileResult.write('\n')
    row = cursor.fetchone()

fileResult.close()