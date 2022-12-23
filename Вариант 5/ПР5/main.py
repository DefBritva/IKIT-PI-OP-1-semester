"""
This is program that can interact with .csv file with universities info.
You can get list of rows or add some or delete etc.
!!!
    Please start program in powershell or cmd because "cls" is not
    working in PyCharm "Run" and not working correctly in PyCharm
    terminal
!!!
Example:
    input: get all
    output: *list of data*

    input: remove
    output: *successfully removed n items*

    input: clear console
    output: *None*
"""

from time import sleep
import csv
from pick import pick
from os import system
from os import path

SEARCHING_OPTIONS = [
    "Id",
    "Name",
    "Founding date",
    "Count of courses",
    "Count of students",
]
SEARCHING_TITLE = "Select property for searching: "


def print_university(_id, data):
    """
    print university data in pretty view
    :param _id: int
    :param data: data[]
    """
    print(
        f"""
------- University Info -------
Id: {_id}
Name: {data[0]}
Founding date: {data[1]}    
Number of courses: {data[2]}    
Number of students: {data[3]}    
-------------------------------
""")


def do_calcs(n1, n2, op):
    """
    calculate expression depending on operator and return boolean
    :param n1: first number
    :param n2: second number
    :param op: str, operator
    :return: bool
    """
    match op:
        case ">":
            return n1 > n2
        case ">=":
            return n1 >= n2
        case "<":
            return n1 < n2
        case "<=":
            return n1 <= n2
        case "=":
            return n1 == n2
        case "":
            return False


def validate_input(inp, mode):
    """
    validating input
    :param inp: str, user input
    :param mode: str, type of input
    :return: int | str
    """
    match mode:
        case "int":
            try:
                val = int(inp)
                if val < 0:
                    print("\nIncorrect arguments, must be >= 0\n")
                    sleep(.5)
                    return False
                return int(inp)
            except ValueError:
                print("\nIncorrect arguments, must be int\n")
                sleep(.5)
                return False
        case "str":
            if inp.strip() != "":
                return inp.strip()
            print("\nIncorrect arguments, must be not empty\n")
            sleep(.5)
            return False
        case "option":
            if inp.strip() in [">", ">=", "<", "<=", "="]:
                return inp.strip()
            print("Incorrect option")
            sleep(.5)
            return False


def get_all():
    """
    prints list of all universities
    """
    count = 0
    if not path.exists("data.csv"):
        print("\nFile is corrupted or does not exists!\n")
        return
    with open("data.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for i, row in enumerate(csv_reader):
            count += 1
            print_university(i, row)

    if count == 0:
        print("\nThere is no any one item in table!\n")


def get_by_property():
    """
    prints list of all universities
    """
    title = SEARCHING_TITLE
    options = SEARCHING_OPTIONS
    _, ind = pick(options, title, indicator="=>")
    data = []
    if not path.exists("data.csv"):
        print("\nFile is corrupted or does not exists!\n")
        return
    with open("data.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for i, row in enumerate(csv_reader):
            data.append([i, *row])

    if len(data) == 0:
        print("\nThere is no any one item in table!\n")
        return

    found = 0
    if ind != 1:
        op = validate_input(input("Enter operator "
                                  "(>, >=, <, <=, =): "), "option")
        if not op:
            return
        val = validate_input(input("Enter the "
                                   f"value for {options[ind]}: "), "int")
        if val is False:
            return
        for i in data:
            if do_calcs(int(i[ind]), val, op):
                print_university(
                    i[0],
                    [value for index, value in enumerate(i) if index != 0]
                )
                found = 1
    else:
        val: str = validate_input(input("Enter the value "
                                        f"for {options[ind]}: "), "str")
        if not val:
            return
        for i in data:
            if val.lower() in i[ind].lower():
                print_university(
                    i[0],
                    [value for index, value in enumerate(i) if index != 0]
                )
                found = 1

    if not found:
        print("\nThere is no universities with this property!\n")


def get_all_sorted():
    """
    prints sorted list of universities
    """
    data = []
    if not path.exists("data.csv"):
        print("\nFile is corrupted or does not exists!\n")
        return
    with open("data.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for i, row in enumerate(csv_reader):
            data.append([i, *row])
    for i in sorted(data, key=lambda x: x[3]):
        print_university(i[0], [v for j, v in enumerate(i) if j != 0])

    if len(data) == 0:
        print("\nThere are no items in the table!\n")


def add_new():
    """
    adds one of the university
    """
    new_univ = []
    name_of_properties = ["Name", "Founding date",
                          "Number of courses", "Number of students"]
    modes = ["str", "int", "int", "int"]  # ["str", *["int"] * 3]
    for i in range(4):
        val = validate_input(
            input(f"Enter {name_of_properties[i]}: "), modes[i]
        )
        if val is False:
            return
        new_univ.append(val)

    if not path.exists("data.csv"):
        curr_index = 0
    else:
        with open("data.csv") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            curr_index = sum(1 for i in csv_reader)

    with open('data.csv', mode='a+') as csv_file:
        data = csv.writer(csv_file, delimiter=',', lineterminator="\n")
        data.writerow(new_univ)

    print_university(curr_index, new_univ)


def remove_one():
    """
    removes one of the university
    """
    title = SEARCHING_TITLE
    options = SEARCHING_OPTIONS
    _, ind = pick(options, title, indicator="=>")
    data = []
    if not path.exists("data.csv"):
        print("\nFile is corrupted or does not exists!\n")
        return
    with open("data.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for i, row in enumerate(csv_reader):
            data.append([i, *row])

    if len(data) == 0:
        print("\nThere is no any one item in table!\n")
        return

    found = 0
    found_items = []

    if ind != 1:
        op = validate_input(input("Enter operator "
                                  "(>, >=, <, <=, =): "), "option")
        if not op:
            return
        val = validate_input(input("Enter the "
                                   f"value for {options[ind]}: "), "int")
        if val is False:
            return
        for i in data:
            if do_calcs(int(i[ind]), val, op):
                found_items.append(i)
                found = 1
    else:
        val: str = validate_input(input("Enter the value "
                                        f"for {options[ind]}: "), "str")
        if not val:
            return
        for i in data:
            if val.lower() in i[ind].lower():
                found_items.append(i)
                found = 1

    if not found:
        print("\nThere is no universities with this property!\n")
        return

    res_data = [i for i in data if i not in found_items]

    with open('data.csv', mode='w') as csv_file:
        data = csv.writer(csv_file, delimiter=',', lineterminator="\n")
        for i in res_data:
            data.writerow(i[1:])

    print(f"\nSuccessfully removed {len(found_items)} items\n")


def clear():
    system("cls")


def start_menu():
    title = "Welcome to Universities Library! Select your command: "
    options = [
        "Print list of universities",
        "Get university by property",
        "Print list of universities sorted by students count",
        "Add new university",
        "Remove university(-ies) by some property",
        "Clear console"
    ]
    _, ind = pick(options, title, indicator="=>")
    return ind


def main():
    while True:
        ind = start_menu()
        commands = [
            get_all,
            get_by_property,
            get_all_sorted,
            add_new,
            remove_one,
            clear
        ]

        commands[ind]()

        cmd = input("Run program again? (y / n) ")
        if cmd != "y" and cmd != "":
            break


if __name__ == '__main__':
    main()
