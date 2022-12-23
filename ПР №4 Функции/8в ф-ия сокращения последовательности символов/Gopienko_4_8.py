"""
Гопиенко Александр
КИ22-17/2Б

Пример 1: a8b10
-> Строка без сокращений - aaaaaaaabbbbbbbbbb

Пример 2: aaaaabbbcd
-> Сокращённая строка -  a5b3cd

Пример 3: 12345
-> Вы ввели числа!

Пример 4: 5ab
-> Строка начинается с цифры

Пример 5: fffiivvvee
-> f3i2v3e2
"""


def shortened_line(classic_line):
    """
    Сокращение строки
    :param classic_line: строка,
     которую нужно преобразовать
      в сокращённый вид
    :return result: сокращённая строка
    """

    list_line = list()
    start_elem = classic_line[0]
    s_elems = ''
    result = ''
    for elem_i in classic_line:
        if start_elem == elem_i:
            s_elems += elem_i
        else:
            start_elem = elem_i
            list_line.append(s_elems)
            s_elems = elem_i
    list_line.append(s_elems)
    for elem_j in list_line:
        if len(elem_j) > 1:
            result += (str(elem_j[0]) + str(len(elem_j)))
        else:
            result += str(elem_j[0])
    return result


def line_classic(short_line):
    """
    Преобразование сокращённой строки в обычную

    :param short_line: сокращённая строка,
     которую нужно преобразовать

    :return back_line: строка без сокращений

    Пример: a5bcde4
    -> Строка без сокращений -  aaaaabcdeeee
    """
    l_elem = ''
    back_line = ''
    digit = ''
    for elem_j in short_line:
        if elem_j.isdigit():
            digit += elem_j
        if elem_j.isalpha():
            if not digit:
                l_elem = elem_j
                back_line += l_elem
            if digit:
                back_line += l_elem\
                             * (int(digit) - 1)
                l_elem = elem_j
                back_line += l_elem
                digit = ''
    if digit:
        back_line += l_elem * (int(digit) - 1)
    return back_line


def check_digits(check_line):
    """
    Проверка на строку,
    если она полностью состоит из цифр

    :param check_line: строка для проверки

    :return all(check_list): True/False
    для проверки условия в функции main()

    Пример: 228
    -> Вы ввели числа!
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
    """
    for elem in zero_line:
        if elem == '0':
            return True


def main():
    """
    Основная функция

    В ней выполняются функции
    shortened_line(classic_line)
    line_classic(short_line)
    check_digits(check_line)
    digit_begin(begin_line)
    digit_zero(zero_line)

    В результате работы функции:
    "Вы завершили работу программы"
    "Вы ничего не ввели"
    "Вы ввели числа"
    "Строка начинается с цифры"
    "В строке присутствуют нули"
    "Сокращённая строка - " answer
    "Строка без сокращений - " answer

    Пример: hhhheeelllooo
    -> Сокращённая строка -  h4e3l3o3
    """
    while True:
        print("Введите произвольную строку")
        print("Вы можете ввести обычную строку"
              " или сокращённую")
        line = input()
        if line == 'END':
            print("Вы завершили работу программы")
            break
        elif not line:
            print("Вы ничего не ввели")
        elif check_digits(line):
            print("Вы ввели числа!")
        elif digit_begin(line):
            print("Строка начинается с цифры")
        elif digit_zero(line):
            print("В строке присутствуют нули")
        else:
            command = 'shortened_line'
            for elem in line:
                if elem.isdigit():
                    command = 'line_classic'
            if command == 'shortened_line':
                answer = shortened_line(line)
                print("Сокращённая строка - ", answer)
            else:
                answer = line_classic(line)
                print("Строка без сокращений - ", answer)


if __name__ == "__main__":
    """
    Точка входа функций
    """
    main()
