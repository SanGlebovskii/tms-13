import csv
with open('weather.csv', 'r') as csvfile:
    data = csv.DictReader(csvfile)
    weather = [row for row in data]
    temp = 0
    s = 0
    d = []
    for i in weather:
        if i['Место'] == 'Минск':
            d.append(i)
    for i in d:
        temp += float(i['Градусы'])
        s += int(i['Скорость ветра'])
print('Средняя температура воздуха в Минске составляет:', round(temp/7, 1))
print('Средняя скорость ветра за последние 7 дней по Минску составила:', round(s/7, 1))