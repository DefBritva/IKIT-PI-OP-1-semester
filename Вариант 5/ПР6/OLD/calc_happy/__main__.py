import argparse
import pytest
from .calc_happy_numbers import calculate_happy_numbers

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--test", dest="test_mod", action="store_true")
parser.add_argument("-d", "--doctest", dest="doctest_mod", action="store_true")
parser.add_argument("value", nargs="?", default=False)

args = parser.parse_args()
help_text = """
Calculate happy numbers script

Usage:
    calc_happy [upper_limit]
    calc_happy -t [--test]
    calc_happy -d [--doctest]

"""


def main():
    """
    startup function for running a calc_happy as a script
    """
    if args.test_mod:
        retcode = pytest.main(["-v"])
        print(retcode)
        exit()
    if args.doctest_mod:
        import doctest
        doctest.testfile("calc_happy_numbers.py")
        exit()
    if args.value is False:
        print(help_text)
    upper_limit = None
    try:
        upper_limit = int(args.value)
        if upper_limit < 1:
            print("Value must be > 0")
            exit()
    except IndexError:
        print("You need to pass in a upper limit for happy numbers list")
        print(help_text)
        exit()
    except ValueError:
        print("Value must be int")
        exit()

    print(f"Searching for happy numbers in list [1,...,{upper_limit}]")

    print(calculate_happy_numbers(int(upper_limit)))

    print("Done")


if __name__ == "__main__":
    main()
