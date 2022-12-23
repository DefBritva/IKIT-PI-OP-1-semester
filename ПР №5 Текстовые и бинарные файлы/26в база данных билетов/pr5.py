"""
 Практическая работа №5
 Вариант 26
 Задание:
    Напишите программу, реализующую базу данных (на основе списков и
    многоуровневых словарей), предназначенную для хранения информации о
    билетах.
    Структура: дата вылета; время вылета; аэропорт назначения (страна,
    город); стоимость; время в пути.
    Предусмотрите возможность:
    а) добавления записей;
    б) удаления записей;
    в) сортировке по времени в пути;
    г) фильтрации по стоимости.
    Для длительного хранения данных реализуйте возможность
    сериализации и десериализации данных в формат json.
    Для выполнения задания используйте стандартный модуль json.
"""
if __name__ == "__main__":

    import json

    with open("data.json", "r") as file:
        tickets_info = json.load(file)


    def option1():
        # функция выполняющая добавление записей
        tickets_info["ticket num"].append(int(input('Введите номер билета ')))
        tickets_info["departure data"].append(input('Введите дату вылета '))
        tickets_info["departure time"].append(input('Введите время вылета '))
        tickets_info["destination airport"].append(input('Введите аэропорт назначения '))
        tickets_info["price"].append(input('Введите цену билета '))
        tickets_info["travel time"].append(input('Введите время полёта в минутах '))


    def option2():
        # функция выполняющая удаление записей
        while True:
            try:
                num = tickets_info["ticket num"].index(int(input('Введите номер билета ')))
                del tickets_info["ticket num"][num]
                del tickets_info["departure data"][num]
                del tickets_info["departure time"][num]
                del tickets_info["destination airport"][num]
                del tickets_info["price"][num]
                del tickets_info["travel time"][num]
                print(tickets_info)
                break
            except ValueError:
                print('Введите номер корректно!!! Для возврата в меню введите "back", чтобы продолжить введите любое значение')
                if input() == "back":
                    break

    def option3_4(inner_dict):
        # функция, которая может отсортировать данные, в зависимости от переданного аргумента.
        list_1 = inner_dict  # tickets_info["travel time"]
        dict1 = {}
        for i, j in list(enumerate(list_1)):
            dict1[i] = j
        dict1 = dict(sorted(dict1.items(), key=lambda key_value: (key_value[1], key_value[0])))
        index = list(dict1.keys())
        tickets_info_new = {}
        for key in tickets_info:
            tickets_info_new[key] = dict(enumerate(tickets_info[key]))

        def create_sorted_dict(inner_dict):
            # функция с помощью которой создаем отсортированные вложенные словари
            par = dict(zip(index, inner_dict))
            for i in par:
                par[i] = inner_dict[i]
            return par

        list_end = []
        list_end.append(create_sorted_dict(tickets_info_new["ticket num"]))
        list_end.append(create_sorted_dict(tickets_info_new["departure data"]))
        list_end.append(create_sorted_dict(tickets_info_new["departure time"]))
        list_end.append(create_sorted_dict(tickets_info_new["destination airport"]))
        list_end.append(create_sorted_dict(tickets_info_new["price"]))
        list_end.append(create_sorted_dict(tickets_info_new["travel time"]))
        for element in list_end:
            print(element)


    def option3():
        # функция выполняющая сортировку по времени

        option3_4(tickets_info["travel time"])


    def option4():
        # функция выполняющая фильтрацию по стоимости
        option3_4(tickets_info["price"])


    def menu():
        # функция вывода меню для пользователя
        print('[1] adding an entry')
        print('[2] deleting entries')
        print('[3] sorted by travel time')
        print('[4] price filtering')
        print('[0] exit the program')


    menu()
    option = int(input('Enter your option '))  # реализация меню
    while True:
        if option == 1:
            option1()
            print(tickets_info)
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            option4()
        elif option == 0:
            with open("data.json", "w") as write_file:  # сохранение данных
                json.dump(tickets_info, write_file)
            break
        else:
            print('Invalid option!!!!!!!!')
        menu()
        option = int(input('Enter your option '))
