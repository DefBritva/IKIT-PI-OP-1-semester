"""

Пример 1: содержимое файла - alexgrimes30
encode
-> исходная строка - alexgrimes30
закодированная строка - nyrktevzrf30

Пример 2: содержимое файла - nyrktevzrf30
encode
-> исходная строка - nyrktevzrf30
закодированная строка - alexgrimes30

Пример 3: пустой файл
write
файл пустой
Строка может содержать буквы латинского алфавита
aboba
-> содержимое файла - aboba

Пример 4: содердимое файла - Hello world
clear
-> пустой файл

Пример 5: содержимое файла - abracadabra
encod
-> Вы ввели неверную команду
"""


import codecs


def instrunctions():
    """
    Инструкции для пользователя
    для работы с программой
    нет параметров и ничего не возвращает
    выводит инструкции пользователю
    """
    print('Введите команду для работы с файлом')
    print('возможные команды:')
    print('encode - кодирование строки')
    print('write - записать строку в файл')
    print('clear - очистить файл')
    print('END - завершить работу файла')


def check_line(checking_line):
    """
    Проверка строки на содержание других символов,
    помимо букв английского языка и цифр, которые 
    необходимо использовать по заданию

    :param checking_line: строка, которую необходимо проверить
        на содержание других символов

    :return True/False: для проверки на условие в 
        функциях encode() и write()

    Пример: здорова
    -> return False
    """
    eng = 'abcdefghijklmnopqrstuvwxyz'
    digits = '01234567890'
    check = list()
    for elem in checking_line:
        if elem in eng or elem in digits:
            check.append(True)
        else:
            check.append(False)
    if all(check):
        return True
    else:
        return False


def encode():
    """
    Кодирование и декодирование строки с помощью кодировки rot13

    в функции открывается файл Gopienko_8_Practice5_.txt
    с помощь менеджеров контекста
    
    Принимает функцию check_line()

    если функция проходит проверку
    на содержание других символов
    результатом функции является закодированная строка
    иначе выводит сообщение пользователю о том, что строка
    может состоять только из букв английского языка и цифр

    Пример: zdorova
    -> mqbebin

    """
    with open("Gopienko_8_Practice5_.txt", mode='r+') as file:
        line_start = file.readline()
        if check_line(line_start):
            print('исходная строка - ', line_start)
            line_result = codecs.encode(line_start, encoding='rot13')
            print('закодированная строка - ', line_result)
            file.seek(0)
            file.write(line_result)
        else:
            print('Ваша строка может состоять'
             'только из букв английского алфавита и цифр')


def write():
    """
    запись закодированной строки в файл

    в функции открывается файл Gopienko_8_Practice5_.txt
    с помощь менеджеров контекста

    содержит функцию check_line()

    Если файл пустой и строка содержит
    английские буквы и цифры, то строка 
    записывается в файл

    Пример: файл пустой
    -> файл пустой
        Строка может содержать буквы английского алфавита и цифры
        введённая строка - BODIbiulder777
        в файле хранится строка BODIbiulder777
    """
    with open("Gopienko_8_Practice5_.txt", mode='r+') as file:
        if not file.read():
            print('файл пустой')
            print('Строка может содержать буквы английского алфавита и цифры')
            line = input()
            if check_line(line):
                file.write(line)
            else:
                print('Вы можете ввести только буквы английского алфавита и цифры')
        else:
            print('В файле уже есть строка, сначала её очистите')


def clear():
    """
    очистка строки в файле

    в функции открывается файл Gopienko_8_Practice5_.txt
    с помощь менеджеров контекста

    Если файл пустой, то выводится сообщение
    Файл уже пустой
    Иначе очищается строка файле
    Пример: файл содержит строку i want 100
    -> Вы очистили строку в файле
        Можете ввести новую
    """
    with open("Gopienko_8_Practice5_.txt", mode='r+') as file:
        if file.read():
            file.truncate(0)
            print('Вы очистили строку в файле')
            print('Можете ввести новую')
        else:
            print('файл уже пустой')


def main():
    """
    Основная функция

    В ней выполняется функция instructions()

    В результате работы функции выполняются:
    "Вы завершили работу функции"
    "исходная строка - ", line_start"
    "закодированная строка - ", line_result"
    "файл пустой"
    "Строка может содержать буквы латинского алфавита"
    "В файле уже есть строка, сначала её очистите"
    "Вы очистили строку в файле"
    "Можете ввести новую"
    "файл уже пустой"
    "Вы ввели неверную команду"
    "Введите команду для работы с файлом"

    Пример: в файле содержится строка konyasharin061304
    encode
    -> исходная строка - konyasharin061304
    закодированная строка - xbalnfuneva061304
    """

    instrunctions()
    while True:
        try:
            command = input()
            if command == 'END':
                print('Вы завершили работу программы')
                break
            elif command == 'encode':
                encode()
            elif command == 'write':
                write()
            elif command == 'clear':
                clear()
            else:
                print('Вы ввели неверную команду')
                print('Введите команду для работы с файлом')
            print('команда для работы файла')
        except FileNotFoundError:
            print('Файл не найден')
            print('Создайте файл  с именем "Gopienko_8_Practice5_.txt"'
                  'и сохраните его в одном месте с файлом программы ')


if __name__ == '__main__':
    """
    Точка входа функции
    """
    main()
