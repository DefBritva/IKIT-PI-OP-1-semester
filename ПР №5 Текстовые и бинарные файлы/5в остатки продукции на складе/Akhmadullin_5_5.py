"""Ахмадуллин Рамиль
КИ22-16/1Б
вариант 5
Написать программу, реализующую хранение информации об остатках
продукции на складе (на основе списков и словарей).
4
Структура: наименование товара, цена, остаток, единица измерения.
Программа должна позволять:
а) загружать информацию из двоичного файла;
б) выполнять поиск товара по наименованию;
в) фильтровать товары по заданному остатку;
г) добавлять позиции;
д) удалять позиции;
е) сохранять данные в двоичном файле.
Для выполнения задания используйте стандартный модуль pickle.

Пример задан в функции create_file().
"""

import pickle


def main():
    products()


def create_file():  # Ф-ия, создающая файл для примера
    # Формат данных: 'наименование товара': [стоимость, остаток, единица измерения].
    list_of_products = {'laptop': [100000, 7, 'pieces'],
                        'mouse pad': [700, 14, 'pieces'],
                        'headphones': [5000, 10, 'pieces']}
    try:
        with open('test.bin', 'wb') as file:
            pickle.dump(list_of_products, file)
    except FileNotFoundError:
        print('Ошибка при нахождении файла\n')


def read_file():  # Ф-ия для вывода содержимого файла.
    try:
        with open('test.bin', 'rb') as file:
            data = pickle.load(file)
    except FileNotFoundError:
        print('Ошибка при нахождении файла\n')
    print(data)


def search():  # Ф-ия для поиска товара по наименованию
    try:
        with open('test.bin', 'rb') as file:
            data = pickle.load(file)
    except FileNotFoundError:
        print('Ошибка при нахождении файла\n')
    name = str(input('Введите наименование\n'))
    if name not in data:
        print('Такого наименования нет')
        return
    print(f'Наименование - {name}: Стоимость - {data[name][0]} RUB, Кол-во - {data[name][1]} {data[name][2]}')


def filter_data():  # Ф-ия для фильтрации товаров по остатку
    try:
        with open('test.bin', 'rb') as file:
            data = pickle.load(file)
    except FileNotFoundError:
        print('Ошибка при нахождении файла\n')
    pieces_data = dict()
    for item in data:
        pieces_data[item] = data[item][1]
    sorted_data = {}
    sorted_keys = sorted(pieces_data, key=pieces_data.get)
    for w in sorted_keys:
        sorted_data[w] = pieces_data[w]
    print(sorted_data)


def add_position():  # Ф-ия для добавления позиции
    try:
        with open('test.bin', 'rb') as file:
            data = pickle.load(file)
    except FileNotFoundError:
        print('Ошибка при нахождении файла\n')
    name = cost = quantity = unit = None
    try:
        name = str(input('Введите наименование позиции\n'))
        cost = int(input('Введите стоимость позиции\n'))
        quantity = int(input('Введите количество\n'))
        unit = str(input('Введите единицу измерения\n'))
    except ValueError:
        print('Некорректный тип данных\n')
    data[name] = [cost, quantity, unit]
    try:
        with open('test.bin', 'wb') as file:
            pickle.dump(data, file)
    except FileNotFoundError:
        print('Ошибка при нахождении файла\n')


def delete_element():  # Ф-ия для удаления позиции
    try:
        with open('test.bin', 'rb') as file:
            data = pickle.load(file)
    except FileNotFoundError:
        print('Ошибка при нахождении файла\n')
    element = None
    try:
        element = str(input('Введите наименование, которое необходимо удалить\n'))
    except ValueError:
        print('Некорректный тип данных\n')
    if element not in data:
        print('Такого наименования нет')
        return
    del data[element]
    try:
        with open('test.bin', 'wb') as file:
            pickle.dump(data, file)
    except FileNotFoundError:
        print('Ошибка при нахождении файла\n')


def products():  # Основная ф-ия, меню для выбора действий
    flag = True
    while flag:
        print("""\nВыберите действие (Введите номер):
    1 - Создать файл для примера
    2 - Вывести данные файла
    3 - Поиск по наименованию
    4 - Отфильтровать товары по заданному остатку
    5 - Добавить позицию
    6 - Удалить позицию
    7 - Завершить выполнение программы""")
        action = None
        try:
            action = int(input())
        except ValueError:
            print('Неверная команда')
        if action == 1:
            create_file()
        elif action == 2:
            read_file()
        elif action == 3:
            search()
        elif action == 4:
            filter_data()
        elif action == 5:
            add_position()
        elif action == 6:
            delete_element()
        elif action == 7:
            flag = False
        else:
            print('Неверная команда')


if __name__ == '__main__':
    main()
