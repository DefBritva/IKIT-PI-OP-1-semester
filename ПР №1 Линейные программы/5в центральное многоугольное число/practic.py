"""
КИ22-16/1Б
Ахмадуллин Рамиль
Вариант 5
Написать программу, вычисляющую n-е центральное многоугольное
число
И определить, является ли оно четным.
Входные данные: число n.
Выходные данные: n-е центральное многоугольное число, сообщение
о том, является ли полученное число четным
"""

n = 0
flag = True
while flag:
    try:
        n = int(input('Введите n  '))
    except ValueError:
        print('ЭТО НЕ ЧИСЛО')
        continue
    x = (n * (n + 1)) // 2 + 1
    if not x % 2:
        print(x, 'Чётное')
    else:
        print(x, 'Нечётное')
    print()
    flag = input('Начать заново? (ДА/НЕТ)  ') in 'ДАYESYesДадаyes'
