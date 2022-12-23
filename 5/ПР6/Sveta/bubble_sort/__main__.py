import argparse
import pytest
from .bubble_sort import sort

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--test", dest="test_mod", action="store_true")
parser.add_argument("-d", "--doctest", dest="doctest_mod", action="store_true")
parser.add_argument("arr", nargs="?", default=False)

args = parser.parse_args()
help_text = """
Пузырьковая сортировка

Использование:
    bubble_sort int[] (Например: 2,3,4,5,1,2,3,6,12)
    bubble_sort -t [--test]
    bubble_sort -d [--doctest]
"""


def main():
    """
    Запуск алгортима в командной строке
    """
    if args.test_mod:
        retcode = pytest.main(["-v"])
        print(retcode)
        exit()
    if args.doctest_mod:
        import doctest
        doctest.testfile("bubble_sort.py")
        exit()
    if args.arr is False:
        print(help_text)
    arr = None
    try:
        arr = [int(x) for x in args.arr.split(",")]
    except IndexError:
        print("Необходимо указать значение")
        print(help_text)
        exit()
    except ValueError:
        print("Список должен состоять из цифр")
        exit()

    print(f"Сортировка массива {arr}]")

    print(sort(arr))

    print("Готово!")


if __name__ == "__main__":
    main()
