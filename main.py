import csv
'''импортируем модуль csv'''
#Задание №1
with open('space (1).txt', encoding='utf8') as file, open('space_new.txt', 'w', encoding='utf8', newline="") as file_new: '''открываем и создаем новый файл'''
    reader = csv.DictReader(file, delimiter='*')
    writer_new = csv.DictWriter(file_new, ['ShipName','planet','coord_place','direction'], delimiter="*" )"""заполняем в наш новый файл заголовки"""
    writer_new.writeheader()
    for row in reader:
        n = int(row['ShipName'][5])
        m = int(row['ShipName'][6])
        k = row['coord_place'].split(" ")
        t = len(row['planet'])
        xd = int(k[0])
        yd = int(k[1])
        if n > 5:
            x = n + xd
        else:
            x =-(n + xd) * 4 + t
        if m > 3:
            y = m + t + yd
        else:
            y = -(n +yd) * m
        row['coord_place'] = str(x) + '' + str(y)
        if row['ShipName'][3] == 'V':
            print(row['ShipName'] + '' + ' - (' + str(x) + '' + str(y) + ')')
            writer_new.writerow(row)
# Задание №2
s = []
with open('space (1).txt', encoding='utf8') as file:
    reader = csv.DictReader(file, delimiter="*")
    for row in reader:
        s.append(row['ShipName'])
N = len(s)
i = 0
while i < N - 1:
    m = i
    j = i + 1
    while j < N:
        if s[j][5:] < s[m][5:]:
            m = j
        j += 1
    s[i], s[m] = s[m], s[i]
    i += 1
for i in range(10):
    print(s[i])
