"""
<<<<<<< HEAD
=======
Группа КИ22-17/2Б Гопиенко Александр
>>>>>>> 2a8c1789734272fcbfc17adf71b844b6a110e9ce
Вариант 8

Пример 1: Нечётное число Вольстенхольма 16843
-> Число 16843 является простым числом Вольстенхольма.
-> Число 16843 нечётное

Пример 2: Число 5
-> Число 5 не является простым числом Вольстенхольма
-> Число 5 нечётное

Пример 3: Число 100
-> Число 100 не является простым числом Вольстенхольма
-> Число 100 чётное

Пример 4: Строка str
-> Ошибка! Неверный формат ввода!
-> Введите start или END

Пример 5: strt
-> Вы не ввели start и не завершили программу
"""
from math import factorial


def parity(variable):
    """Функция проверки числа на чётность"""
    if variable % 2 == 0:
        print("Число", variable, "чётное")
    else:
        print("Число", variable, "нечётное")


while True:
    try:
        print("Введите start или END")
        work = input()
        if work == 'END':
            print('Вы завершили работу программы')
            break
        if work == 'start':
            parametr = int(input("Введите число "))
            if (factorial(2 * parametr) // (factorial(parametr) * factorial(parametr))) % (parametr**4) == 2:
                print("Число", parametr, "является простым числом Вольстенхольма")
                parity(parametr)
            else:
                print("Число", parametr, "не является простым числом Вольстенхольма")
                parity(parametr)
        else:
            print("Вы не ввели start и не завершили программу")
    except ValueError:
        print("Ошибка! Неверный формат ввода!")
