import datetime

def print_days():

    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=1)
    thirty_days_ago = today - datetime.timedelta(days=30)

    print('Сегодня:', today.strftime('%Y-%m-%d'))
    print('Вчера', yesterday.strftime('%Y-%m-%d'))
    print('30 дней назад:', thirty_days_ago.strftime('%Y-%m-%d'))

def str_2_datetime(date_string):
    return datetime.datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')

if __name__ == '__main__':
    print_days()
    print(str_2_datetime('01/01/20 12:10:03.234567'))
