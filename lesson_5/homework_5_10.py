from datetime import datetime, timedelta

time_delta = timedelta(hours=7, minutes=20)
train_list = [
    {
        'train_num': '134',
        'arriv_stat': 'Warsaw',
        'arriv_time': datetime(2021, 7, 23, 22, 35),
        'depurt_stat': 'Minsk',
        'depurt_time': datetime(2021, 7, 23, 9, 20)
    },
    {
        'train_num': '1006',
        'arriv_stat': 'Berlin',
        'arriv_time': datetime(2021, 7, 22, 6, 10),
        'depurt_stat': 'Frankfurt',
        'depurt_time': datetime(2021, 7, 22, 2, 10)
    },
    {
        'train_num': 'k19',
        'arriv_stat': 'Paris',
        'arriv_time': datetime(2021, 7, 21, 23, 7),
        'depurt_stat': 'Minsk',
        'depurt_time': datetime(2021, 7, 21, 6, 17)
    },
    {
        'train_num': 'E1980',
        'arriv_stat': 'London',
        'arriv_time': datetime(2021, 7, 20, 20, 49),
        'depurt_stat': 'Paris',
        'depurt_time': datetime(2021, 7, 20, 19, 6)
    }
]

for train in train_list:
    if train['arriv_time'] - train['depurt_time'] > time_delta:
        print(train)

