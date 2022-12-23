"""

input -> add user
output -> enter name, enter age...
if arguments are good: *shows user info*
if arguments is not good: *shows error message*

input -> read user data
output -> choose criterion
if there is user with criterion == value: *shows user info*

etc.

"""

import json
from pick import pick
import time


def ask_menu():
    if input("Wanna go to menu? (y / n) ").lower() == "y":
        start_menu()


def convert_to_number(number, name):
    try:
        return int(number)

    except ValueError:
        print(name, "must be int, returning to menu...")
        time.sleep(2)
        start_menu()
        return False


def print_user(name, age, balance, count_of_transactions, user_id):
    print()
    print("-- User Info --")
    print("Id is", user_id)
    print("Name is", name)
    print("Age is", age)
    print("Balance is", balance)
    print("Count of transactions is", count_of_transactions)
    print("---------------")
    print()
    return


def add_user(name, age, balance, count_of_transactions):
    validated_user = {
        "name": name,
        "age": convert_to_number(age, "Age"),
        "balance": convert_to_number(balance, "Balance"),
        "count_of_transactions": convert_to_number(count_of_transactions, "Count of transactions")
    }

    for value in validated_user.values():
        if value is False:
            print("Returning to menu...")
            time.sleep(4)
            start_menu()
            return

    if validated_user["age"] <= 0 or validated_user["name"] == "":
        print("Incorrect arguments (age > 0, name is not empty)")
        print("Returning to menu...")
        time.sleep(4)
        start_menu()
        return

    with open("users.json", "r") as f:
        current_users = json.load(f)

    current_users.append(validated_user)
    validated_user["id"] = len(current_users) - 1

    with open("users.json", "w") as f:
        json.dump(current_users, f, indent=4)

    print("User successfully created! Here it is: ")
    values = list(validated_user.values())
    print_user(values[0], values[1], values[2], values[3], values[4])

    ask_menu()

    return


def get_users_by_criterion(criterion, value):
    if criterion != "name":
        int_value = convert_to_number(value, "Value")
        if criterion == "age" and int_value <= 0:
            print("Incorrect value. (Age > 0, balance and count "
                  "of transactions >= 0) Returning to menu...")
            time.sleep(4)
            start_menu()
            return
        if criterion != "age" and int_value < 0:
            print("Incorrect value. (Age > 0, balance and count "
                  "of transactions >= 0) Returning to menu...")
            time.sleep(4)
            start_menu()
            return

    if value == "":
        print("Name must be not empty, returning to menu...")
        time.sleep(4)
        start_menu()
        return

    with open("users.json", "r") as f:
        users = json.load(f)

    if criterion == "name":
        right_users = list(filter(lambda u: u[criterion].lower() == value.lower(), users))
    else:
        right_users = list(filter(lambda u: u[criterion] == int(value), users))

    if not len(list(right_users)):
        print(f"There is no user with {criterion} = {value}")
        ask_menu()
        return

    for user in right_users:
        values = list(user.values())
        print_user(values[0], values[1], values[2], values[3], values[4])

    ask_menu()

    return


def view_all_users():
    with open("users.json", "r") as f:
        users = json.load(f)

    for user in users:
        values = list(user.values())
        print_user(values[0], values[1], values[2], values[3], values[4])

    ask_menu()

    return


def edit_user(user_id):
    if convert_to_number(user_id, "Id") is False:
        return
    else:
        i = int(user_id)
        if i < 0:
            print(
                "Incorrect arguments (id >= 0), returning to menu..."
            )
            time.sleep(4)
            start_menu()
            return

    with open("users.json", "r") as f:
        users = json.load(f)

    if i >= len(users):
        print(f"User with id = {i} is not exist, returning to menu...")
        time.sleep(4)
        start_menu()
        return

    title = "Which property do u wanna to edit? "
    options = ["Name", "Age", "Balance", "Count of transactions"]
    app_options = ["name", "age", "balance", "count_of_transactions"]
    option, index = pick(options, title, indicator="=>", default_index=0)

    new_value = input(f"Enter new value of property "
                      "(current is {users[i][app_options[index]]}): ")

    validated_value = new_value
    if app_options[index] in ["balance", "age", "count_of_transactions"]:
        validated_value = convert_to_number(new_value, option)
        if app_options[index] == "age" and validated_value <= 0:
            print("Incorrect value. (Age > 0, balance and "
                  "count of transactions >= 0) Returning to menu...")
            time.sleep(4)
            start_menu()
            return
        if app_options[index] != "age" and validated_value < 0:
            print(
                "Incorrect value. (Age > 0, balance and "
                "count of transactions >= 0) Returning to menu..."
            )
            time.sleep(4)
            start_menu()
            return

    if validated_value == "":
        print("Incorrect arguments (name is not empty), returning to menu...")
        time.sleep(4)
        start_menu()
        return

    users[i][app_options[index]] = validated_value

    with open("users.json", "w") as f:
        json.dump(users, f, indent=4)

    print("User successfully edited! Here it is: ")
    values = list(users[i].values())
    print_user(values[0], values[1], values[2], values[3], values[4])

    ask_menu()

    return


def remove_user(user_id):
    if convert_to_number(user_id, "Id") is False:
        return
    else:
        int_id = int(user_id)
        if int_id < 0:
            print(
                "Incorrect arguments (id >= 0), returning to menu...")
            time.sleep(4)
            start_menu()
            return

    with open("users.json", "r") as f:
        users = json.load(f)

    if int_id >= len(users):
        print(f"User with id = {int_id} is not exist, returning to menu...")
        time.sleep(4)
        start_menu()
        return

    right_users = list(filter(lambda user: user["id"] != int_id, users))

    for i in range(len(right_users)):
        right_users[i]["id"] = i

    with open("users.json", "w") as f:
        json.dump(right_users, f, indent=4)

    print("User successfully deleted!")

    ask_menu()

    return


def start_menu():
    title = "Welcome to bank service! Enter the command: "
    options = [
        "Add user", "Read user data", "View all users",
        "Edit user data (by id)", "Remove user (by id)", "Exit"
    ]

    option, index = pick(options, title, indicator="=>", default_index=0)
    match index:
        case 0:
            add_user(
                input("Enter name: "),
                input("Enter age: "),
                input("Enter balance: "),
                input("Enter count of transactions: ")
            )
        case 1:
            title = "Choose criterion: "
            options = ["Name", "Age", "Balance", "Count of transactions"]
            app_options = ["name", "age", "balance", "count_of_transactions"]

            option, index = pick(options, title, indicator="=>", default_index=0)
            get_users_by_criterion(
                app_options[index],
                input(f"Enter value of criterion ({options[index]}): ")
            )
        case 2:
            view_all_users()
        case 3:
            edit_user(input("Enter id: "))
        case 4:
            remove_user(input("Enter id: "))
        case 5:
            print("Bye bye!")
            pass


def main():
    start_menu()


if __name__ == "__main__":
    main()
