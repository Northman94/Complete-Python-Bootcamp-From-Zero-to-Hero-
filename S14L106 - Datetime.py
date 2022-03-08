
import datetime

my_time = datetime.time(13,20,1,10) #24-hour Clock

print(my_time.minute)
# 20

print(my_time.hour)
# 13

print(my_time)
# 13:20:01.000010

print(my_time.microsecond)
# 10

type(my_time)
# datetime.time


# = - = - = - = - = - = - = - =
today = datetime.date.today()
print(today)
# 2022-03-08

print(today.year)
# 2022

print(today.month)
# 3

print(today.day)
# 8

print(today.ctime())
# Tue Mar  8 00:00:00 2022

# ∆∆∆ Notice clock time is empty ∆∆∆



# = - = - = - = - = - = - = - =
from datetime import datetime

my_daytime = datetime(2022,10,3,14,20,1)

print(my_daytime)
# 2022-10-03 14:20:01


# = - = - = - = - = - = - = - =
# Fixing mistake:

print(my_daytime.replace(year = 2023))
# 2023-10-03 14:20:01



# = - = - = - = - = - = - = - =
# (datetime.date) is the same as (from datetime import date)
from datetime import date

date1 = date(2022,3,8)
date2 = date(2021,3,8)

print(date1-date2)
# 365 days, 0:00:00

d_delta = date1-date2

# d_delta
# datetime.timedelta(days=365)

type(d_delta)
# datetime.timedelta



# = - = - = - = - = - = - = - =
d_time1 = datetime(2022,3,8,22,0)

d_time2 = datetime(2021,3,8,12,0)

delt = d_time1 - d_time2

print(delt)
# 365 days, 10:00:00

print(delt.seconds)
# 36000

print(delt.total_seconds())
# 31572000.0
