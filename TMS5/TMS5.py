# Задание 1: лямбда функция, определяющая четно/нечетное

x = int(input("x: "))
b = lambda x: print("Четное") if x % 2 == 0 else print("Нечетное")
b(x)

# Задание 2: список чисел, каждое число которого перевести в строку через лямбду

arr = [1,2,3,5,6,7,4,6,8,3]
arr = map(lambda i: str(i), arr)
print(list(arr))

# Задание 3: отфильровать полиндромы в кортеже

tup = ("snins", "AXE", "xelex", "poottis", "invert")
tup = filter(lambda i: True if i[::-1] == i[::1] else False, tup)
print(list(tup))

# Задание 4: Зафиксировать время выполнения функции через декоратор

from datetime import datetime
def genThousand():
    [i for i in range(1000000)]
def iterThousand():
    a = 0
    for i in range(1000000):
        a += i


def wrapper(dorontok):
    time = datetime.now()
    dorontok()
    time = datetime.now() - time
    return time
print(wrapper(genThousand))
print(wrapper(iterThousand))

# Задание 5: функция, возвращающая числа, если проходит проверку isdigit()

def get_digit(x):

    if (x[0:2] == '-.' or x[0:2] == '-,') and (x.count('.') or x.count(',')) < 2 and x.count('-') < 2: x = '-0.' + x[2:]
    elif (x[0] == '.' or x[0] == ',') and (x.count('.') or x.count(',')) < 2: x = '0' + x
    elif (x[-1] == '.' or x[-1] == '.') and (x.count('.') or x.count(',')) < 2: x += '0'


    if x.count('-') > 1 or x.count('.') > 1 \
            or not x.replace('-', '').replace('.', '').isdigit():
        return "NaN"

    if not (x.count(".") or x.count(",")): return int(x)
    else: return float(x)


for x in ['-1.00', '.2.', '323', '.214', '3a3', '-8', '--.34', '-,3']: print(get_digit(x))
