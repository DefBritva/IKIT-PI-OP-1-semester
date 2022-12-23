def check_number(roll):
    """Проверка списка на числа

    Функция проверяет является ли элементы в списке типа строка в
    списке числом,если нет то идет замена на число, в противном
    случае переменная типа строка становится числом.
    Изменяется текущий список.
    :param roll: список строк
    """
    arr = [*roll]
    for i in range(len(arr)):
        while True:
            if arr[i].isdigit():
                break
            else:
                print('Исправте ошибку в ', arr[i])
                arr[i] = input()
        arr[i] = int(arr[i])
    return arr
