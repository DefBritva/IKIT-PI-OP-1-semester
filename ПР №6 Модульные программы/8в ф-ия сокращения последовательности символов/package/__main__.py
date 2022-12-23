from . import shortline
from . import workalg
from . import tests
import argparse
import pytest
import doctest


def main():
    """
    Основая функция

    Принимает модули shortline (line_classic, shortened_line),
    workalg (check_digits, digit_begin, digit_zero) и tests

    Пример: a3b5
    -> Строка без сокращений - aaabbbbb

    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--line', type=str, help='введите произвольную'
                                                 ' или сокращённую строку')
    parser.add_argument('--test', action='store_true')
    parser.add_argument('--doctest', action='store_true')
    args = parser.parse_args()
    if args.test:
        pytest.main(["-v", "package/tests.py"])
    elif args.doctest:
        doctest.testmod(m=shortline, verbose=True)
        doctest.testmod(m=workalg, verbose=True)
    else:
        line = args.line
        if not line:
            print("Вы ничего не ввели")
        elif workalg.check_digits(line):
            print("Вы ввели числа!")
        elif workalg.digit_begin(line):
            print("Строка начинается с цифры")
        elif workalg.digit_zero(line):
            print("В строке присутствуют нули")
        else:
            command = 'shortened_line'
            for elem in line:
                if elem.isdigit():
                    command = 'line_classic'
            if command == 'shortened_line':
                answer = shortline.shortened_line(line)
                print("Сокращённая строка - ", answer)
            else:
                answer = shortline.line_classic(line)
                print("Строка без сокращений - ", answer)


if __name__ == "__main__":
    """
    Точка входа функций
    """
    main()
