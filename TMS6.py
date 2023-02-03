# Задание 1: байты в строку, затем снова а байт в кодировке "latin1" и затем снова в строку

byt_c = b'r\xc3\xa9sum\xc3\xa9'
str = byt_c.decode("utf-8")
print(str)
print(str.encode("latin-1"))
print(byt_c.decode("utf-8"))

# Задание 2: записать 4 строки и сохранить в созданный файл, открыть файл и дописать 2 строки

text1, text2, text3, text4 = [input(f'Введите текст #{num}: ') for num in range(1, 5)]

with open('test.txt', 'w') as file_w:
    file_w.writelines([text1 + '\n', text2 + '\n'])
    file_w.close()

with open('test.txt', 'a') as file_a:
    file_a.writelines([text3 + '\n', text4])
    file_a.close()

# Задание 3: создать словарь пользователей ключом которых является числовой код, сохранить словарь в  json

import json;

dikt = {
987345:("Vadim", "Mayach"),
125678:("Egor", "Sinok"),
784389:("Ilya", "Miron"),
287134:("Jamak", "Kerov"),
798735:("Evgeniy", "Popev"),
674534:("Nicole", "Gvardeeva"),
}

with open("dict_Students.json", "w") as f:
    json.dump(dikt, fp = f)

# Задание 4: прочитать json, сохранить в csv файл

import random
import csv
import json


with open('dict_Students.json', 'r') as f:
    dikt = json.load(f)

    data = [[f'#{num}', key, dikt[key][0], dikt[key][1],
             '{}{}{}-{}{}-{}{}'.format(*str(random.randint(1000000, 9999999)))]
            for num, key in enumerate(dikt, start=1)]

    f.close()

with open('dict_Students.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([' ', 'ID', 'NAME', 'AGE', 'PHONE'])

    for line in data:
        writer.writerow(line)

    csvfile.close()

# Задание 5: прочитать csv файл и сохранить в excel файл, кроме возраста.

print('\n5 задание:\n')

with open('dict_Students.csv', 'r') as f:

    data_l = csv.reader(f)
    data_s = dict()

    for x in data_l: data_s['' if x[0] == ' ' else 'Person ' + x[0][-1]] = x[1:3] + x[-1:]

data = pandas.DataFrame(data_s)
data.to_excel('temp.xlsx', index=False)