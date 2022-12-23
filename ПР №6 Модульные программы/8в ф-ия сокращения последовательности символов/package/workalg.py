def check_digits(check_line):
    """
    Проверка на строку,
    если она полностью состоит из цифр

    :param check_line: строка для проверки

    :return all(check_list): True/False
    для проверки условия в функции main()

    Пример: 228
    -> Вы ввели числа!

    >>> check_digits('123')
    True
    """
    check_list = list()
    for digit in check_line:
        check_list.append(digit.isdigit())
    return all(check_list)


def digit_begin(begin_line):
    """
    Проверка на строку,
    если она начинается с цифры

    :param begin_line: строка для проверки

    :return True: True,
     если строка начинается с цифры

    Пример: 1soft
    -> Строка начинается с цифры

    >>> digit_begin('1aab')
    True
    """
    if begin_line[0].isdigit():
        return True


def digit_zero(zero_line):
    """
    Проверка на строку,
    если в ней содержатся нули

    :param zero_line: строка для проверки

    :return True: True,
    если строка содержит 0

    Пример: compucter0
    -> Строка начинается с цифры

    >>> digit_zero('a0b')
    True
    """
    for elem_zero in zero_line:
        if  elem_zero == '0':
            return True





