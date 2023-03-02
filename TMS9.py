class Human():
    def __init__(self):
        print('я Аянами Рей')

    @classmethod
    def evaClassMethod(cls):
        return print('Я истинная Аянами Рей')

    @staticmethod
    def evaStatic(self):
        return print('я тоже Аянами Рей')

class Evangelion(type):
    def __new__(cls, clsname, superclasses, attributedict):
        return type(clsname, superclasses, attributedict)


a = Human()
b = Human.evaClassMethod()
c = a.evaStatic(a)