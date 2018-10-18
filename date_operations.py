import datetime as dt
import calendar
from math import ceil
import pandas as pd


def week_of_month(date):
    """ Returns the week of the month for the specified date.
    """
    first_day = date.replace(day=1)
    dom = date.day
    adjusted_dom = dom + first_day.weekday()
    return int(ceil(adjusted_dom / 7.0))


def get_season(date):
    return (date.month % 12 + 3) // 3


def is_start_of_month(date):
    return int(date.day == 1)


def is_end_of_month(date):
    return int(calendar.monthrange((date.year, date.month)[1]) == date.day)


def is_weekend(date):
    return int(date.isoweekday() > 5)


def is_first_working_day_of_month(date):
    firstdayofmonth = dt.date(date.year, date.month, 1)
    lastdayofmonth = dt.date(date.year, date.month, calendar.monthrange(date.year, date.month)[1])
    first_working_day_of_month = pd.date_range(firstdayofmonth, lastdayofmonth, freq='BMS').date[0]
    return int(date == first_working_day_of_month)


def is_last_working_day_of_month(date):
    firstdayofmonth = dt.date(date.year, date.month, 1)
    lastdayofmonth = dt.date(date.year, date.month, calendar.monthrange(date.year, date.month)[1])
    first_working_day_of_month = pd.date_range(firstdayofmonth, lastdayofmonth, freq='BM').date[0]
    return int(date == first_working_day_of_month)

def is_semi_month_ending_date(date):
    firstdayofmonth = dt.date(date.year, date.month, 1)
    lastdayofmonth = dt.date(date.year, date.month, calendar.monthrange(date.year, date.month)[1])
    first_working_day_of_month = pd.date_range(firstdayofmonth, lastdayofmonth, freq='BM').date[0]
    return int(date == first_working_day_of_month)


def convert_to_vector(date: dt.date):
    date_vector = [date.day,
                   date.month,
                   date.isoweekday(),
                   week_of_month(date),
                   date.isocalendar()[1],
                   get_season(date),
                   is_first_working_day_of_month(date),
                   is_last_working_day_of_month(date),
                   is_weekend(),

                   ]


data = pd.read_csv("data/ts.csv")
today = dt.date.today().replace(day=29)
#
# print(today)
#
# print("day of month", today.day)
# print("month of year", today.month)
# print("day of week", today.isoweekday())
# print("week of the month", week_of_month(today))
# print("week of the year", today.isocalendar()[1])
# print("season", (today.month % 12 + 3) // 3)
# print("is start of the month", int(today.day == 1))
# print("is end of the month", int(calendar.monthrange(today.year, today.month)[1] == today.day))
# print("is weekend", int(today.isoweekday() > 5))

# day of month
# month of year
# day of week
# week of month
# week of year
# season
# is start of month
# is end of month
# is weekend
# is holiday

print(pd.date_range('1/1/2000', '2/1/2000', freq='BMS'))

date = dt.date(2018, 9, 28)
print(is_first_working_day_of_month(date))
print(is_last_working_day_of_month(date))
