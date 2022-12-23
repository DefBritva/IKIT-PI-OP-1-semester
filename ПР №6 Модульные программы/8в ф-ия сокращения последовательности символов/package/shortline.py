def shortened_line(classic_line):
    """
    Сокращение строки

    :param classic_line: строка, которую нужно преобразовать
      в сокращённый вид
    :return result: сокращённая строка

    Пример: aaabbb
    -> a3b3

    >>> shortened_line('aaaaabbb')
    'a5b3'
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

    >>> line_classic('a3b3')
    'aaabbb'
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
                back_line += l_elem * (int(digit) - 1)
                l_elem = elem_j
                back_line += l_elem
                digit = ''
        if not elem_j.isalpha() and not elem_j.isdigit():
            if not digit:
                l_elem = elem_j
                back_line += l_elem
            if digit:
                back_line += l_elem * (int(digit) - 1)
                l_elem = elem_j
                back_line += l_elem
                digit = ''
    if digit:
        back_line += l_elem * (int(digit) - 1)
    return back_line





