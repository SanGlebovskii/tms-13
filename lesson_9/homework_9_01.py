import csv
rows = [['Имя', 'Фамилия','Возраст'], ['Владислав', 'Топалов', '41'], ['Тилль', 'Линдеманн', '45'],
        ['Клара', 'Цеткин', '34'], ['Михаил', 'Романов', '10'], ['Александр', 'Македонский', '22'],
        ['Алексей', 'Бруй', '26'], ['Григорий', 'Распутин', '15'], ['Георгий', 'Жуков', '19'],
        ['Леонид', 'Гайдай', '30']]
with open('humans.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(rows)
with open('humans.csv', 'r') as csvfile2:
    csvreader = csv.DictReader(csvfile2)
    age_group_1, age_group_2, age_group_3, age_group_4, age_group_5 = 0, 0, 0, 0, 0
    humans = [row for row in csvreader]
    print(humans)
    for i in humans:
        if int(i['Возраст']) <= 12:
            age_group_1 += 1
        elif int(i['Возраст']) <= 18:
            age_group_2 += 1
        elif int(i['Возраст']) <= 25:
            age_group_3 += 1
        elif int(i['Возраст']) <= 40:
            age_group_4 += 1
        elif int(i['Возраст']) > 40:
            age_group_5 += 1
fields = ['Возрастные группы', 'Количество людей']
rows_2 = [['1-12', age_group_1], ['13-18', age_group_2], ['19-25', age_group_3],
          ['26-40', age_group_4], ['40+', age_group_5]]
with open('account.csv', 'w') as csvfile3:
    csvwriter_2 = csv.writer(csvfile3)
    csvwriter_2.writerow(fields)
    csvwriter_2.writerows(rows_2)




