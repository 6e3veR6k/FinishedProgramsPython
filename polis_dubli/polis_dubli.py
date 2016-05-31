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


db06 = SQL('hq01db06', 'Himalia')


conn = pyodbc.connect(db06.sqlInfo)



file = open('query_dubli.txt')

query = file.read()


cursor = conn.cursor()
cursor.execute(query)

row = cursor.fetchone()
while row:
    print '{0}\t{1}\t{2}'.format(row[0], row[1], row[2])
    row = cursor.fetchone()
