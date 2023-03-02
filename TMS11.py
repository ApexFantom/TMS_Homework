# Задание 1: фунцкия-генератор геометрической прогрессии
def genGeom(m, b=3, q=2):
    s = b
    for n in range(m):
        yield s
        s *= q





print([i for i in genGeom(100)])

# Задание 3: Функция для филтрация емейла
import re

def mailCorrection(m):
    correctedMail = re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$', m)
    return correctedMail.group(0)

print(mailCorrection(mailInput))
