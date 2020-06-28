def decorator(func):
    import functools
    import datetime
    @functools.wraps(func)
    def wrapper(*args):
       
        if func.__name__ == 'add':
            operation_name = "Сложение"
        elif func.__name__ == 'diff':
            operation_name = "Вычитание"
        elif func.__name__ == 'mult':
            operation_name = "Умножение"
        elif func.__name__ == 'divis':
            operation_name = "Деление"
        else:
            operation_name = "Неизвестная операция"
        
        result = func(*args)
        
        # Сохранение в дукумент
        with open('Результат.txt', 'a') as f:
            f.write("\n")
            f.write("Функция: " + operation_name + "\n")
            f.write("Аргументы: " + str(args) + "\n")
            f.write("Результат: " + str(result) + "\n"+"\n")
        return result
        
    return wrapper


@decorator
def add(*args):
    res = 0
    for arg in args:
        res += arg
    return res

@decorator
def diff(*args):
    args = list(args)
    res = args.pop(0)
    for arg in args:
        res -= arg
    return res

@decorator
def mult(*args):
    res = 1
    for arg in args:
        res *= arg
    return res

@decorator
def divis(*args):
    args = list(args)
    res = args.pop(0)
    for arg in args:
        res /= arg
    return res


@decorator
def calc():

    choice = input(' =КАЛЬКУЛЯТОР=\n Выберите действие: \n 1 - Сложение \n 2 - Вычитание \n 3 - Умножение \n 4 - Деление \n')

    if choice == '1':
        print('Введите слагаемые (через пробел)')
        arr = input().split()
        arr = list(map(int, arr))
        result = add(*arr)
        print("Ответ:", result)
    elif choice == '2':
        print('Введите уменьшаемое и вычитаемые (через пробел)')
        arr = input().split()
        arr = list(map(int, arr))
        result = diff(*arr)
        print("Ответ:", result)
    elif choice == '3':
        print('Введите множители (через пробел)')
        arr = input().split()
        arr = list(map(int, arr))
        result = mult(*arr)
        print("Ответ:", result)
    elif choice == '4':
        print('Введите делимое и делители (через пробел)')
        arr = input().split()
        arr = list(map(int, arr))
        result = divis(*arr)
        print("Ответ:", result)
    else:
        print('Неверный ввод!!!')
calc()