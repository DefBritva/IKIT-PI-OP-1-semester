def add_row(matrix_row, n_row, k_row):
    """Добавление строки матрицы"""
    row = []
    for j in range(k_row):
        sum_column = 0
        for i in range(n_row):
            sum_column += matrix_row[i][j]
        row.append(sum_column)
    matrix_row.append(row)
    return matrix_row


def add_column(matrix_column, n_column, k_column):
    """Добавление столбца матрицы"""
    for i in range(n_column):
        sum_row = 0
        for j in range(k_column):
            sum_row += matrix_column[i][j]
        matrix_column[i].append(sum_row)
    return matrix_column


def add_all(matrix_all, n_all, k_all):
    """Добавление столбца и строки матрицы"""
    matrix_all = add_row(matrix_all, n_all, k_all)
    for i in range(n_all):
        sum_row = 0
        for j in range(k_all):
            sum_row += matrix_all[i][j]
        matrix_all[i].append(sum_row)
    matrix_all[-1].append(0)
    return matrix_all


"""Меню команд"""


menu = {'A': add_row, 'B': add_column, 'C': add_all}
print('Доступные команды: "A" - добавить строку;'
      ' "B" - добавить столбец; "C" - добавить строку и столбец')
while True:
    try:
        command = ''
        command_work = [str(i) for i in input("Введите размеры матрицы (1-5000) - число строк,"
                                              " (3-5000) - число столбцов, команду(если хотите),"
                                              "END (если хотите завершить)").split()]
        N = ''
        K = ''
        if not len(command_work):
            print("Вы ничего не ввели")
            continue
        if len(command_work) == 1:
            if command_work[0] == 'END':
                print('Вы завершили программу')
                break
            else:
                print("Вы ввели только одно число "
                      "и не завершили работу программу!")
                continue
        if len(command_work) == 2:
            N = int(command_work[0])
            K = int(command_work[1])
            if not N or not K:
                print("Число строк и матриц не должны быть равными нулю")
                continue
            if N < 1 or K < 3:
                print("Число строк матрицы должно быть 1 и более, "
                      "а стобцов 3 и более ")
                continue
            if N > 5000 or K > 5000:
                print("Введите числа поменьше,"
                      " иначе программа будет долго выполняться!")
                continue
        if len(command_work) == 3:
            N = int(command_work[0])
            K = int(command_work[1])
            command = command_work[2]
            if not N or not K:
                print("Число строк и матрицы не должны быть равными нулю!")
                continue
            if N < 1 or K < 3:
                print("Число строк должно быть 1 и более, "
                      "а столбцов 3 и более!")
                continue
            if N > 5000 or K > 5000:
                print("Введите числа поменьше,"
                      " иначе программа будет долго выполняться!")
                continue
        if len(command_work) >= 4:
            print("Вы ввели слишком много значений."
                  " Нужно ввести только 2-3 значения!")
            continue
        matrix = [[0] * K for i in range(N)]
        for n in range(1, N):
            for k in range(3, K):
                matrix[n][k] = int(0.5 * k * (n**2 + n) - n**2 + 2*n)
        if command != '':
            if command == 'A' or command == 'B' or command == 'C':
                matrix = menu[command](matrix, N, K)
            else:
                print("Неверная команда")
                continue
        for i, item in enumerate(matrix):
            print(item)
    except ValueError:
        print("Неверно введённые данные. "
              "Первые два числа должны быть целыми")
    except TypeError:
        print("Неверное имя команды")
