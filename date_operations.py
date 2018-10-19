import datetime as dt
import calendar
from math import ceil
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import minmax_scale


def day_of_year(date):
    return date.timetuple().tm_yday


def week_of_month(date):
    """ Returns the week of the month for the specified date.
    """
    first_day = date.replace(day=1)
    dom = date.day
    adjusted_dom = dom + first_day.weekday()
    return int(ceil(adjusted_dom / 7.0))


def week_of_year(date):
    return date.isocalendar()[1]


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


def is_middle_of_month(date):
    return int(date.day == 15)


def convert_to_vector(date: dt.date):
    # day of month
    # month of year
    # day of week
    # week of month
    # week of year
    # season
    # is start of month
    # is end of month
    # is weekend
    # is middle of the day
    date_vector = [date.day,
                   date.month,
                   date.isoweekday(),
                   week_of_month(date),
                   week_of_year(date),
                   get_season(date),
                   is_first_working_day_of_month(date),
                   is_last_working_day_of_month(date),
                   is_weekend(date),
                   is_middle_of_month(date)
                   ]
    return date_vector


def create_date_frame(data):
    # convert string to date
    dates = [dt.datetime.strptime(x, '%d-%b-%y') for x in data['Date']]
    # convert date to array
    vector_dates = [convert_to_vector(d) for d in dates]
    df = pd.DataFrame(vector_dates, columns=['day', 'month', 'dayofweek', 'weekofmonth', 'weekofyear', 'season',
                                             'isfirstworkingday', 'islastworkingday', 'isweekend', 'ismiddleofmonth'])
    df['Price'] = data['Price']
    df.to_csv('data/converted.csv')
    return df


def normalize_features(data: pd.DataFrame):
    df = pd.DataFrame(data)
    df = df.drop('Price', axis=1)
    df_norm = (df - df.min()) / (df.max() - df.min())
    df_norm['Price'] = data['Price']
    df_norm.to_csv('data/normalized.csv')
    return df_norm


def plot_tests():
    series = pd.Series.from_csv('data/ts.csv', header=0)
    print(series.head())
    series.plot()
    plt.show()


if __name__ == '__main__':
    today = dt.date.today()
    data = pd.read_csv("data/ts.csv")
    data = create_date_frame(data)
    data = normalize_features(data)
    print(data)
