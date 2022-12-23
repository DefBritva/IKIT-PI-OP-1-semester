def sort(init_arr):
    """Сортировка списка прямым обменом

    Функция сортирует список обменивая между собой переменные
    (переменная с большим значение встановится вперед)
    благодаря дополительной перемменой, которая сохраняет их.
    Изменяется текущий список.

    >>> sort([5, 1, 3, 2])
    [1, 2, 3, 5]

    >>> sort([213, 12, 41, 23, 51, 241])
    [12, 23, 41, 51, 213, 241]

    :param init_arr: int[] список чисел
    """
    arr = [*init_arr]
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                aid = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = aid
    return arr


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
