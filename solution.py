# Решение:
import csv

indexes = set()
homes = set()
with open('pp-complete.csv') as in_f, open('sold.csv', 'w', newline='') as out_f:
    reader, writer = csv.reader(in_f), csv.writer(out_f, delimiter=' ')
    # почтовый индекс row[3] - уникальный идентификатор недвижимости
    for row in reader:
        index = row[3]
        # множества indexes и homes собирают идентификаторы недвижимости, которая встречалась (продавалась) более 1 раза
        if index not in indexes:
            indexes.add(index)
        else:
            homes.add(index)
        # записываем адреса и названия той недвижимости, что продавалась более 1 раза, в новый файл
        if index in homes:
            writer.writerow(row[7:10])

# Чтобы программа не считывала файл со списком транзакций целиком, произведено построчное чтение.
# Во избежание сравнения каждого идентификатора с каждым из общего файла, в качестве базы сравнения используется
# множество homes, где хранятся идентификаторы подходящей условию недвижимости.