import csv
import datetime
with open('date.csv', 'r') as file:
    date = csv.reader(file)
    list_date = []
    for row in date:
        date_time = datetime.datetime.strptime(*row, '%d.%m.%Y')
        list_date.append(date_time)
    print(min(list_date))