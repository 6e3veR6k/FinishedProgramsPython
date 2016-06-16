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


db05 = SQL('hq01db05', 'OrantaSch')
print db05.sql_info()
