class MyException(Exception):
    def __init__(self, *args):
        self.message = args[0] if args else None
    def __str__(self):
        return f"X> ошибка определенного класса {self.message}"


cont = True
while(cont):
    prompt = input("Введите числовое выражение:\n")
    try:
        if prompt == 'NaN' :
            raise MyException(prompt)
        print(eval(prompt))
    except MyException:
        print(MyException(prompt))
    except SyntaxError:
        print("X> синтаксическая ошибка")
    except NameError:
        print("X> калькулятор не принимает переменные")
    except:
        print("X> ошибка при выполнении вычислений")
    finally:
        prompt = input('продолжить? [y] [n]')
        cont = True if (prompt == 'y') else False