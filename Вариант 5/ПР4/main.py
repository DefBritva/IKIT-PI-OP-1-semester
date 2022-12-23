"""
Программа для поиска счастливых чисел.
Ожидаемый результат:
1)
  in: верхняя граница = 10
  out: [1, 7, 10]
2)
  in: верхняя граница = 80
  out: [1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79]
3)
  in: верхняя граница = b
  out: Введено некорректное значение! (n должно быть числом, n должно быть > 0)
4)
  in: верхняя граница = -4
  out: Введено некорректное значение! (n должно быть числом, n должно быть > 0)
5)
  in: верхняя граница = ""
  out: Введено некорректное значение! (n должно быть числом, n должно быть > 0)
"""

import os
import random


def get_sum(n):
    """
    get sum of squares of digits of a number

    :param n: integer
    :return: sum of squares of digits of a number
    """
    symbols = list(str(n))
    return sum([int(x) ** 2 for x in symbols])


def is_happy_number(n):
    """
    calculating, if the number is happy number

    :param n: integer
    :return: (flag, n):
        flag: bool, shows is the number is happy number,
        n: the number itself
    """
    arr_of_nums = []
    curr = n
    while True:
        summ = get_sum(curr)
        if summ in arr_of_nums:
            return False, n
        if summ == 1:
            return True, n
        else:
            arr_of_nums.append(summ)
        curr = summ


def validate_input(inp):
    """
    validating user input

    :param inp: user input
    :return: validated value
    """
    try:
        validated = int(inp)
        if validated <= 0:
            raise ValueError
    except ValueError:
        print("Введено некорректное значение! (n должно быть числом, n должно"
              " быть > 0)")
        start_menu()
        return False

    return validated


def calculate_happy_numbers(n=None, *args):
    """
    calculate how many happy numbers in
    list [0, n], where n is user input
    and shows this list

    :param: n: upper limit
    """

    if n == None:
        upper_limit = random.randint(10, 100)
        print(f"Тестовое значение n = {upper_limit}")
    else:
        upper_limit = validate_input(n)
        if not upper_limit: return

    arr_of_numbers = []
    for i in range(upper_limit + 1):
        result = is_happy_number(i)
        if result[0]:
            arr_of_numbers.append(result[1])

    print("Список 'счастливых' чисел: ", arr_of_numbers)

    command = input("""Повторить алгоритм
    yc (повторить + очистить консоль)
    y (повторить)
    n (выйти)
    """)

    if command == "yc":
        os.system("cls")
        start_menu()
        return
    elif command == "y":
        start_menu()
        return


def exit_program(*args):
    """
    exiting the program
    """
    print("Выходим из программы...")
    if "c" in args:
        os.system("cls")


def start_menu():
    """
    starting the menu
    """
    command_dict = {
        "start": calculate_happy_numbers,
        "test": calculate_happy_numbers,
        "ex": exit_program,
    }
    command, *args = input("""Введите опцию и по необходимости параметры: 
    Запустить алгоритм (start n (n: int))
    Провести тест (test)
    Выйти и очистить консоль (ex с (c: flag))
    Выйти (ex)
    """).split(" ")

    if command not in list(command_dict.keys()):
        print("Введена несуществующая команда!")
        start_menu()
        return

    command_dict[command](*args)


def main():
    start_menu()


if __name__ == "__main__":
    main()
