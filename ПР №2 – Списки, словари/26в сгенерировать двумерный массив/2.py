"""


Задание:

Сгенерировать двумерный массив размером N * N и заполнить его
целыми числами случайным образом.
Транспонировать матрицу.
Создать словарь, ключи которого – наименование характеристик
матрицы, а значения – значения этих характеристик.
Пример:
{
 ‘mean_row’: …, # среднее по строкам
 ‘mean_col’: …, # среднее по столбцам
}
Добавить поиск наиболее близкого к введенному пользователем числу
числа из матрицы и вывод его индексов и разницы этих чисел.


Примеры работы программы:

1) Вводим 'asdasdasdasd' : 'Для начала работы введите "start". Для завершения программы введите "stop" '

2) Вводим start, выбираем размер матрицы 3, получаем квадратичную матрицу A 3х3 и транспонированную A.


95 -71 -39
-26 -97 4
51 -32 49

95 -26 51
-71 -97 -32
-39 4 49

Вводим число -99: получаем -97 (Ближайшее число к введеному пользователем)

вводим 'stop' для завершения программы.


3) Вводим 'start'. Вводим размер квадратичной матрицы: razmer - получаем "Введите число!"
 Программа начинает работу заново. Выводится сообщение:
 Для начала работы введите "start". Для завершения программы введите "stop"

 4) Вводим 'start'. Выбираем размер 10. Получаем матрицу ниже, и вводим abcd:
                                                                                Выводится сообщение:
                                                                                "Введите число!". Программа начинает работу
                                                                                заново. Вводим "stop" завершаем работу.

 -97 -66 -7 10 56 -90 -91 53 100 -95
-37 1 88 41 -28 1 33 77 86 -6
66 5 90 21 82 93 56 70 -77 96
67 43 -11 67 5 -34 -89 -34 1 -61
73 -11 35 37 -75 -31 61 -58 12 -39
-81 17 65 -37 -51 45 46 18 29 48
9 28 79 12 19 97 -94 35 -26 -19
-24 63 8 -20 89 -35 20 96 -91 65
57 19 84 42 -34 -55 13 23 18 -37
57 -62 54 -49 98 63 -95 -46 72 63

-97 -37 66 67 73 -81 9 -24 57 57
-66 1 5 43 -11 17 28 63 19 -62
-7 88 90 -11 35 65 79 8 84 54
10 41 21 67 37 -37 12 -20 42 -49
56 -28 82 5 -75 -51 19 89 -34 98
-90 1 93 -34 -31 45 97 -35 -55 63
-91 33 56 -89 61 46 -94 20 13 -95
53 77 70 -34 -58 18 35 96 23 -46
100 86 -77 1 12 29 -26 -91 18 72
-95 -6 96 -61 -39 48 -19 65 -37 63


"""
from random import randint


def print_matrix(array):
    for i in array:
        for j in i:
            print(j, end=' ')
        print()


while True:
    start_stop = input('Для начала работы введите "start". Для завершения программы введите "stop" ')
    if start_stop == 'start':
        try:
            n = int(input('Введите размер квадратной матрицы '))
            arr = []
            for i in range(n):
                internal_ass = []
                for j in range(n):
                    internal_ass.append(randint(-10e1, 10e1))
                arr.append(internal_ass)
            transpose = [[row[i] for row in arr] for i in range(len(arr[0]))]

            print_matrix(arr)
            print()
            print_matrix(transpose)

            k = 0
            for i in arr:
                for j in i:
                    if j > k:
                        k = j
            max_num = k

            for i in arr:
                for j in i:
                    if j < k:
                        k = j
            min_num = k
            total_sum = 0
            count = 0
            for i in arr:
                for j in i:
                    total_sum += j
                    count += 1
            mean_num = total_sum / count

            for i in arr:
                for j in i:
                    k = j
                    if 0 < j < k:
                        k = j
            small_pos_num = k
            dict1 = {'Max num': max_num, 'Min num': min_num, 'Mean num': mean_num,
                     'smallest positive number': small_pos_num}

            arr1 = [i for item in arr for i in item]
            rast = 2 * 10e20
            numeric = 0
            n = int(input('Введите число '))

            for i in arr1:
                if abs(n - i) < rast:
                    numeric = i
                    rast = abs(n - i)
            print(f'Ближайшее число к n в матрице: {numeric}')
            ind2 = None
            for i in arr:
                for j in i:
                    if j == numeric:
                        print(f'Индекс [{arr.index(i)}][{i.index(j)}]')

            print(f'Разность чисел = {n - numeric}')



        except Exception:
            print('Введите число!')

    elif start_stop == 'stop':
        break
    else:
        continue
