"""


Пример 1: 20 1 10 source_print
-> 6 10 9 8 10 3 5 2 7 6 9 8 7 2 9 4 5 3 5 3

Пример 2: 20 1 10 result_print
->  Результат программы -  1 2 3 5 6 7 8 9 10
    Удалённые элементы и их число
    Число 1 удалилось 2 раз
    Число 2 удалилось 1 раз
    Число 3 удалилось 1 раз
    Число 5 удалилось 1 раз
    Число 6 удалилось 1 раз
    Число 7 удалилось 1 раз
    Число 9 удалилось 1 раз
    Число 10 удалилось 3 раз

Пример 3:
->  Исходный набор данных -  4 2 10 4 9 1 2 9 2 6 8 8 5 9 5 2 4 8 2 7
    Результат работы программы -  1 2 4 5 6 7 8 9 10
    Удалённые элементы и их число
    Число 2 удалилось 4 раз
    Число 4 удалилось 2 раз
    Число 5 удалилось 1 раз
    Число 8 удалилось 2 раз
    Число 9 удалилось 2 раз

Пример 4: 10 1 10
->  Вы не указали команду, которую хотите выполнить

Пример 5: 10 10 1 source_print result_print
->  Начальное число диапазона не может быть меньше либо равняться конечному!
    Поменяем эти числа местами
    Исходный набор данных -  4 10 6 6 2 3 8 7 10 4
    Результат работы программы -  2 3 4 6 7 8 10
    Удалённые элементы и их число
    Число 4 удалилось 1 раз
    Число 6 удалилось 1 раз
    Число 10 удалилось 1 раз

"""
from random import randint
from collections import Counter


while True:
    print("Введите длину списка (первое число)")
    print("Введите диапазон рандомных значений "
          "для заполнения списка (второе и третье числа)")
    print("Введите команду (source_print - вывод исходного списка "
          "или result_print - конечный результат)")
    print("Вы можете ввести вторую команду")
    command_works = (str(j) for j in input().split())
    command_works = tuple(command_works)
    command = ''
    N, *borders = command_works
    if N == 'END':
        break
    elif not borders:
        print("Вы не ввели диапазон рандомных чисел. "
              "А также не вводите первым числом имя команды")
    else:
        if len(borders) == 2:
            print("Вы не указали команду, которую хотите выполнить")
        if len(borders) == 3:
            try:
                begin, end, command = borders
                begin, end, N = int(begin), int(end), int(N)
                if N > 10000000:
                    print("Введите число поменьше, "
                          "иначе программа будет долго выполняться")
                    continue
                if begin >= end:
                    print("Начальное число диапазона не может быть меньше "
                          "либо равняться конечному!")
                    print("Поменяем эти числа местами")
                    begin, end = end, begin
                N_list = []
                for i in range(N):
                    N_list.append(randint(begin, end))
                N_set = set(N_list)
                elem_count = Counter(N_list)
                elem_count = dict(elem_count)
                if command == "source_print":
                    print("Исходный набор данных - ", *N_list)
                elif command == "result_print":
                    print("Результат работы программы - ", *N_set)
                    print("Удалённые элементы и их число")
                    for key, value in sorted(elem_count.items()):
                        if value-1 != 0:
                            print("Число", key, "удалилось", value - 1, "раз", sep=' ')
                else:
                    print("Вы ввели неверную команду")
                    print("Вы можете ввести только source_print или result_print")
                    print("Вы также можете ввести обе команды")
            except ValueError:
                print("Вы неверно ввели данные")
                print("Первые три числа - целые числа!")
        if len(borders) == 4:
            try:
                begin, end, command_1, command_2 = borders
                begin, end, N = int(begin), int(end), int(N)
                if N >= 10000000:
                    print("Введите число поменьше, "
                          "иначе программа будет долго выполняться")
                    continue
                if begin >= end:
                    print("Начальное число диапазона не может быть меньше "
                          "либо равняться конечному!")
                    print("Поменяем эти числа местами")
                    begin, end = end, begin
                N_list = []
                for i in range(N):
                    N_list.append(randint(begin, end))
                N_set = set(N_list)
                elem_count = Counter(N_list)
                elem_count = dict(elem_count)
                if (command_1 == "source_print" and command_2 == 'result_print') \
                        or (command_1 == 'result_print' and command_2 == 'source_print'):
                    print("Исходный набор данных - ", *N_list)
                    print("Результат работы программы - ", *N_set)
                    print("Удалённые элементы и их число")
                    for key, value in sorted(elem_count.items()):
                        if value - 1 != 0:
                            print("Число", key, "удалилось", value - 1, "раз", sep=' ')
                else:
                    if command_1 != 'source_print' and command_1 != 'result_print':
                        print("Вы неверно ввели имя первой команды")
                        print("Вы можете ввести source_print или result_print")
                    elif command_2 != 'source_print' and command_2 != 'result_print':
                        print("Вы неверно ввели имя второй команды")
                        print("Вы можете ввести source_print или result_print")
                    elif command_1 == command_2:
                        print("Команда", command_1, "введена два раза!", sep=' ')
            except ValueError:
                print("Вы неверно ввели данные")
                print("Первые три числа - целые числа!")
        if len(borders) >= 5:
            print("Вы ввели слишком много значений")
