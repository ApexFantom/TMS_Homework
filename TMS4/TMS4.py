# Задание 1: Дан словарь, создать новый словарь, поменяв местами ключ и значение

sl = {"key1": "value1", "key2": "value2"}
def reverseDict(slovar):
    return {k: v for v, k in slovar.items()}
print(reverseDict(sl))

# Задание 2: Написать программу нахождения факториала. Факториал натурального числа n определяется как произведение всех натуральных чисел от 1 до n включительно. Реализацию выполнить в виде рекрсивной функции

def facto(n):
    if n == 1:
        return n
    else:
        return n * facto(n-1)
print(facto(6))

# Задание 3: Дан список чисел. Посчитать сколько раз встречается каждое число. Использовать для подсчета функцию



dNums = [1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 8, 9, 9, 0, 0, 9]

def counter(dictArgument):
    from collections import Counter
    return Counter(dictArgument)
print(counter(dNums))

# Задание 4: Функция-генератор списков отдает текущее время с задержкой в 1 сек.

def timecount(n):
    from datetime import datetime
    import time
    timeDict = []
    for i in range(n):
        timeDict.append([datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')])
        time.sleep(1)
    return timeDict

print(timecount(5))
