"""
Модуль, проверяющий входные данные на корректность, а также приводящий их к нужному формату
"""


def is_valid(info):
    """
    Функция, проверки и редактирования данных
    :param info: Входные данные получаемые от пользователя
    :return: tuple, bool, входные данные для функции либо False
    """
    try:
        matrix, start_n, end_n = info.split(' ')
        with open(matrix, 'r', encoding='utf-8'):
            pass
    except FileNotFoundError as e:
        print(e)
        return False
    except ValueError as e:
        print(e)
        return False
    if not (start_n.isdigit() and end_n.isdigit()):
        return False
    return matrix, int(start_n), int(end_n)
