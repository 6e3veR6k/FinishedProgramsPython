#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta, date

birthday = date(1986, 4, 9)
now = date.today()
diff = int(str(abs(now-birthday)).split()[0])
print(date.fromordinal(diff))