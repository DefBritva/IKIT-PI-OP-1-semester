import json
import datetime as dt


def check_name_surname(string):
    """
    Проверка ввода имени и фамилии.
    Длина имени и фамилии должна быть больше единицы и на русском языке. Присутствует поддержка двойных имен и фамилий.
    :param string: имя или фамилия
    :return: string: str
    """
    while True:
        string = string.lower()
        string = string.replace('ё', 'е')

        if '-' in string and string.find('-') == string.rfind('-'):  # Проверка на наличие одного дефиса(что допустимо)
            string1 = string.replace('-', '')  # Временная переменная без дефиса
        else:
            string1 = string

        for char in string1:
            if not 1072 <= ord(char) <= 1103:  # Буквы от "а" до "я"
                print('ФИО должно быть на русском языке')
                string = input('Введите корректное значение ')
                break
        else:
            string = string.capitalize()
            if string1.isalpha() and len(string1) >= 2:  # Проверка на наличие только букв и длину
                break
            string = input('Введите корректное значение ')
    return string


def check_num(string):
    """
    Проверка ввода номера зачетной книжки.
    Номер зачетной книжки должен состоять только из цифр.
    :param string: номер зачетной книжки
    :return: string: str
    """
    while True:
        if string.isdigit():
            int(string)
            break
        string = input('Введите корректное значение ')
    return string


def check_birth_date(date):
    """
    Проверка ввода даты рождения.
    Дата рождения должны быть вида ДД.ММ.ГГГГ и не противоречить календарной системе исчисления даты.
    :param date: дата рождения
    :return: date: str
    """
    while True:
        try:
            dt_lst = date.split('.')
            if len(dt_lst) > 3:
                date = input('Введите корректный формат даты ')
                continue
            date = dt.date(int(dt_lst[2]), int(dt_lst[1]), int(dt_lst[0]))
            return date.isoformat()
        except (TypeError, ValueError, IndexError):
            date = input('Введите корректный формат даты ')


def check_mark(mark):
    """
    Проверка ввода среднего балла.
    Средний балл должен состоять из цифр и быть в диапозоне от 0 до ста включительно.
    :param mark: средний балл
    :return: mark: float
    """
    while True:
        try:
            mark = float(mark)
            if 0 <= mark <= 100:
                break
        except ValueError:
            pass
        mark = input('Введите корректный балл ')
    return mark


def input_nat(name=''):
    """
    Ввод числа с клавиатуры и проверка на то, является ли оно натуральным.
    :param name: сообщение, выводимое пользователю во время приглашения ко вводу
    :type name: str
    :return: number: int, введеное пользователем число
    """
    while True:
        number = input(name)
        try:
            int(number)
            if int(number) <= 0:
                print('Число должно быть положительным')
            else:
                number = int(number)
                break
        except ValueError:
            print('Неверный тип данных')
    return number


def check_middle_name(string):
    """
    Проверка ввода отчества.
    Отчество должно состоять из букв русского алфавита, быть больше 5 и заканчиваться на -вич или -вна.
    :param string: отчество
    :return: string: str
    """
    while True:
        if string == '0':  # Отсутствие отчества автоматически проходит проверку
            break

        string = string.lower()
        string = string.replace('ё', 'е')

        for char in string:
            if not 1072 <= ord(char) <= 1103:  # Буквы от "а" до "я"
                print('ФИО должно быть на русском языке')
                string = input('Введите корректное значение ')
                break
        else:
            string = string.capitalize()
            if string.isalpha() and len(string) >= 6:
                if string[-3:] in ['вич', 'вна']:  # Проверка окончаний отчеств
                    break
            string = input('Введите корректное значение ')
    return string


def check_path(path, key):
    """
    Проверка введенного пользователем пути к файлу.
    Путь должен быть вида C:/folder/something.txt.
    :param path: путь к файлу
    :param key: 'r' для проверки чтения из файла, 'w' для проверки записи в файл
    :type key: str
    :return: path: str
    """
    while True:
        try:
            if len(path) == 1:  # Если путь не будет содержать :/, то будут использоваться файлы из директории
                path = input('Введите существующий путь к файлу ')  # программы, что не айс
                continue
            elif path[1:3] != ':/':
                path = input('Введите существующий путь к файлу ')
                continue

            if key == 'w':  # Проверка возможности записи
                with open(path, 'w') as detect:
                    detect.write('')
            elif key == 'r':  # Проверка возможности чтения
                with open(path, 'r') as detect:
                    detect.read()
            break
        except (FileNotFoundError, TypeError, PermissionError):
            path = input('Введите существующий путь к файлу ')
    return path


def check_json_file(path, key):
    """
    Проверка json файла.
    Проверка на то, является ли данный файл расширения .json и исполняем ли он.
    :param path: путь к фалу
    :type path: str
    :param key: 'r' для проверки чтения из файла, 'w' для проверки записи в файл
    :type key: str
    :return: checker: bool, True, если файл формата .json, False, если нет
    """
    checker = True
    try:
        if key == 'w':  # Проверка возможности записи
            with open(path, 'w') as detect:
                json.dump('', detect)
        elif key == 'r':  # Проверка возможности чтения
            with open(path, 'r') as detect:
                json.load(detect)

    except json.decoder.JSONDecodeError:
        checker = False
        print('Указанный файл либо не формата .json, либо пуст')
    return checker
