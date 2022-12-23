"""Никитин Александр, КИ19-17/1Б, реализация хранения базы данных студентов"""

import json
import argparse
from Check import *
from pprint import PrettyPrinter


def add_information(all_students, path):
    """
    Добавление информации о студенте
    :param all_students: база данных со всеми студентами
    :type all_students: dict
    :param path: путь к файлу базы данных
    :type path: str
    :return: None
    """
    nickname = check_name_surname(input('Введите фамилию '))
    name = check_name_surname(input('Введите имя '))
    middle_name = check_middle_name(input('Введите отчество. Если отчество отсутствует, введите 0 '))
    record_book = check_num(input('Введите номер зачетной книжки '))
    birth = check_birth_date(input('Введите дату рождения (в формате ЧЧ.ММ.ГГГГ) '))
    mark = check_mark(input('Введите средний балл '))

    if middle_name != '0':
        full_name = {'Nickname': nickname, 'Name': name, 'Middle name': middle_name}
    else:
        full_name = {'Nickname': nickname, 'Name': name}

    basic_information = {'Full Name': full_name, 'Date of Birth': birth, 'mark': mark}
    all_students[record_book] = basic_information
    with open(path, 'w') as add:
        json.dump(all_students, add)


def delete_information(all_students, key, path):
    """
    Удаление информации о студенте.
    :param all_students: база данных со всеми студентами
    :type all_students: dict
    :param key: ключ (номер зачеткной книжки) для поиска студента
    :type key: int
    :param path: путь к файлу базы данных
    :type path: str
    :return: None
    """
    for key_one_student in all_students:
        if key == key_one_student:  # Проверка ключа каждого студента и заданного пользователем ключа
            all_students.pop(key)
            print('Студент успешно удален')
            break
    else:
        print('Такого студента нет')

    with open(path, 'w') as remove:
        json.dump(all_students, remove)


def find_student(all_students, full_name):
    """
    Поиск студента по ФИО
    :param all_students: база данных со всеми студентами
    :type all_students: dict
    :param full_name: ФИО студента
    :type full_name: str
    :return: None
    """
    checker = True
    for key in all_students:
        if len(all_students[key]['Full Name']) == 3:  # Люди с отчеством
            if all_students[key]['Full Name']['Nickname'] + ' ' \
                    + all_students[key]['Full Name']['Name'] \
                    + ' ' + all_students[key]['Full Name']['Middle name'] == full_name:  # Распаковка вложенных
                PrettyPrinter().pprint(all_students[key])   # словарей до переменных ФИО и их конкатенация
                checker = False

        else:  # Люди без отчества
            if all_students[key]['Full Name']['Nickname'] + ' ' + all_students[key]['Full Name']['Name'] == full_name:
                PrettyPrinter.pprint(all_students[key])
                checker = False

    if checker:
        print('Такого студента нет')


def highest_mark(all_students, limit):
    """
    Вывод заданного количества студентов с самой высокой оценкой.
    :param all_students: база данных со всеми студентами
    :type all_students: dict
    :param limit: количество выводимых студентов
    :return: None
    """
    limit = int(limit)
    all_students_list = list(all_students.items())
    all_students_list.sort(key=lambda student: student[1]['mark'], reverse=True)  # Сортировка студентов по
    sorted_students = all_students_list[0:limit]  # убыванию среднего балла

    PrettyPrinter().pprint(sorted_students)


def copy_file(all_students, path):
    """
    Копирование базы данных в отдельный файл формата .json
    :param all_students: база данных со всеми студентами
    :type all_students: dict
    :param path: путь, в который копируется файл
    :type path: str
    :return: None
    """
    if check_json_file(path, 'w'):
        with open(path, 'w') as locate:
            json.dump(all_students, locate)


def use_user_file(path):
    """
    Использование базы данных, введеной пользователем.
    :param path: путь к базе данных
    :type path: str
    :return: выход из программы
    """
    with open(path, 'r') as file:
        all_students = json.load(file)
    return all_students


def main():
    with open('Data_Base.json', 'r') as read:
        list_of_student = json.load(read)

    user_path = 'Data_Base.json'
    parser = argparse.ArgumentParser(description='Возможные ключи')
    parser.add_argument('-f', '--key_f', action="store_true", help='Использование своей базы данных')
    parser.add_argument('-s', '--key_s', action="store_true", help='Копия файла')
    parser.add_argument('-p', '--key_p', action="store_true", help='Показ базы данных')
    par_keys = parser.parse_args()

    if par_keys.key_f:  # Использование своей базы данных
        user_path = check_path(input('Введите абсолютный путь к файлу '), 'r')
        list_of_student = use_user_file(user_path)

    if par_keys.key_s:  # Копия файла
        user_path = check_path(input('Введите абсолютный путь к файлу '), 'w')
        copy_file(list_of_student, user_path)
        exit(1)

    if par_keys.key_p:  # Показ базы данных
        PrettyPrinter().pprint(list_of_student)
        exit(1)

    while True:
        print('Введите номер интересуещей вас функции\n1. Добавление студента\n2. Удаление студента\n''3. Поиск'
              ' студента по ФИО\n4. Вывод n количества студентов с самым высоким баллом\n5. Закончить программу\n')
        user_choice = input()

        while True:  # Проверка ввода выбора пользователя
            if user_choice in ['1', '2', '3', '4', '5']:
                break
            user_choice = input('Введите значение от 1 до 5 ')

        if user_choice == '1':  # Добавление студента
            add_information(list_of_student, user_path)

        if user_choice == '2':  # Удаление студента
            number_of_book = check_num(input('Введите номер зачетной книжки студента '))
            delete_information(list_of_student, number_of_book, user_path)

        if user_choice == '3':  # Поиск студента
            name_student = input('Введите ФИО студента ')
            find_student(list_of_student, name_student)

        if user_choice == '4':  # Студенты с высоким баллом
            number_of_students = input_nat('Введите предельное количество студентов ')
            highest_mark(list_of_student, number_of_students)

        if user_choice == '5':  # Выход
            break


if __name__ == '__main__':
    main()
# -f - собственный файл, -p - показ базы данных, -s копия файля(путь)
