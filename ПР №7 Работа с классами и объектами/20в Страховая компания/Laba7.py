"""Никитин Александр, КИ19-17/1Б, вариант 20, описание работы страховой компании"""

import re
import datetime as dt
import json
from pprint import PrettyPrinter
from random import randint


class Address:
    def __init__(self, country, district, city, street, number_of_house, building, number_of_flat):
        self.country = country
        self.district = district
        self.city = city
        self.street = street
        self.house = number_of_house
        self.building = building
        self.flat = number_of_flat

    def check_country(self):
        while True:
            if not self.country.isdigit():
                break  # минимальное - 3
            self.country = input('Введите корректную страну ')

    def check_house(self):
        while True:
            if self.house.isdigit():
                break
            self.house = input('Введите правильный формат номера дома ')

    def check_building(self):
        while True:
            if self.building.isdigit():
                break
            self.building = input('Введите правильный формат номера строения ')

    def check_flat(self):
        while True:
            if self.flat.isdigit():
                break
            self.flat = input('Введите правильный формат номера квартиры ')

    def squash(self):  # Представление адреса в виде одной строчки
        if self.building == '':
            return f'{self.country.capitalize()}, {self.district.capitalize()}, {self.city.capitalize()},' \
                   f' {self.street.capitalize()}, д. {self.house}, кв. {self.flat}'
        else:
            return f'{self.country.capitalize()}, {self.district.capitalize()}, {self.city.capitalize()},' \
                   f' {self.street.capitalize()}, д. {self.house}, стр. {self.building}, кв. {self.flat}'


class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number

    def check_number(self):
        while True:
            if re.match(r'[8]|[+7][0-9]{10}', self.phone_number):  # Номер начинается с 8 или +7
                if (self.phone_number[0] == '8' and len(self.phone_number) == 11) or (
                        self.phone_number[0] == '+' and len(self.phone_number) == 12):
                    break
            self.phone_number = input('Введите корректный номер ')


class Filial:
    def __init__(self, country, district, city, street, number_of_house, number_of_flat,
                 building, name, phone_number, branches):
        self.class_address = Address(country, district, city, street, number_of_house, building, number_of_flat)
        self.filial_name = name
        self.address = self.class_address.squash()
        self.branches = branches
        self.class_phone = Phone(phone_number)

    def add_filial(self):
        self.branches[self.filial_name] = [self.address, self.class_phone.phone_number, []]

        with open('branches.json', 'w') as add:
            json.dump(self.branches, add)


class Person:
    def __init__(self, name, nickname, middle_name, person_phone):
        self.name = name
        self.nickname = nickname
        self.middle = middle_name
        self.class_phone = Phone(person_phone)

        self.class_phone.check_number()

    def check_nickname(self):
        nickname = self.nickname
        while True:
            nickname = nickname.lower()
            nickname = nickname.replace('ё', 'е')

            if '-' in nickname and nickname.find('-') == nickname.rfind('-'):  # Проверка на наличие одного дефиса
                temporary_string = nickname.replace('-', '')  # Временная переменная без дефиса
            else:
                temporary_string = nickname

            for char in temporary_string:
                if not 1072 <= ord(char) <= 1103:  # Буквы от "а" до "я"
                    print('Фамилия должна состоять только из русских букв')
                    nickname = input('Введите корректное значение ')
                    break
            else:
                nickname = nickname.capitalize()
                if len(temporary_string) >= 2:  # Проверка на длину
                    break
                print('Фамилия должна быть длиннее двух символов')
                nickname = input('Введите корректное значение ')
        self.nickname = nickname

    def check_name(self):
        name = self.name
        while True:
            name = name.lower()
            name = name.replace('ё', 'е')

            for char in name:
                if not 1072 <= ord(char) <= 1103:  # Буквы от "а" до "я"
                    print('Имя должно состоять только из русских букв')
                    name = input('Введите корректное значение ')
                    break
            else:
                name = name.capitalize()
                if len(name) >= 2:  # Проверка на длину
                    break
                print('Имя должно быть длиннее двух символов')
                name = input('Введите корректное значение имени ')
        self.name = name

    def check_middle(self):
        string = self.middle
        while True:
            if string == '0':  # Отсутствие отчества автоматически проходит проверку
                break

            string = string.lower()
            string = string.replace('ё', 'е')

            for char in string:
                if not 1072 <= ord(char) <= 1103:  # Буквы от "а" до "я"
                    print('Отчество должно состоять только из русских букв')
                    string = input('Введите корректное значение ')
                    break
            else:
                string = string.capitalize()
                if len(string) >= 6:
                    if string[-3:] in ['вич', 'вна']:  # Проверка окончаний отчеств
                        break
                string = input('Введите корректное значение отчества ')


class Agent(Person):
    def __init__(self, nickname, name, middle_name, branch_name, phone_number):
        super().__init__(name, nickname, middle_name, phone_number)
        self.branch_name = branch_name
        self.phone = phone_number

    def check_filial(self, branches):
        while True:
            if self.branch_name not in branches.keys():
                self.branch_name = input('Введите существующий филиал агента ')
            else:
                break

    def add_agent(self, all_branches):
        agent_name = f'{self.nickname} {self.name} {self.middle}'
        personal_date = [agent_name, self.phone]
        all_branches[self.branch_name][2].append(personal_date)

        with open('branches.json', 'w') as add:
            json.dump(all_branches, add)


class Client(Person):
    def __init__(self, nickname, name, middle_name, phone):
        super().__init__(name, nickname, middle_name, phone)
        self.full_information = f'{nickname} {name} {middle_name}; номер телефона: {phone}'


class Insurance:
    def __init__(self, number_of_contract, date, cost, rate, object_of_insurance,
                 filial_of_contract, kind_of_insurance, client):
        self.number = number_of_contract
        self.date = date
        self.cost = cost
        self.rate = rate
        self.object = object_of_insurance
        self.filial = filial_of_contract
        self.kind = kind_of_insurance
        self.class_client = client  # Клиент передается уже экземпляром

    def check_filial(self, branches):
        while True:
            if self.filial not in branches:
                self.filial = input('Введите существующий филиал агента ')
            else:
                break

    def check_date(self):
        while True:
            try:
                dt_lst = self.date.split('.')
                if len(dt_lst) > 3:
                    self.date = input('Введите корректный формат даты ')
                    continue
                self.date = dt.date(int(dt_lst[2]), int(dt_lst[1]), int(dt_lst[0]))
                return self.date.isoformat()
            except (TypeError, ValueError, IndexError):
                self.date = input('Введите корректный формат даты ')

    def check_cost(self):
        while True:
            try:
                float(self.cost)
                break
            except ValueError:
                self.cost = input('Введите корректную сумму ')

    def check_rate(self):
        while True:
            try:
                if 0 < float(self.rate) <= 1.0:
                    break
            except ValueError:
                pass
            self.rate = input('Введите корректную процентную ставку ')

    def check_object(self):
        while True:
            if self.object.isalpha():
                break
            self.object = input('Введите корректное значение объекта страхования ')

    def check_kind(self):
        while True:
            if self.kind.isalpha():
                break
            self.kind = input('Введите корректный вид страхования ')

    def add_contract(self, contracts):
        contracts[self.number] = f'{self.class_client.full_information}. Дата оформления: {self.date}.' \
                                 f'Цена: {self.cost} рублей. Ставка: {self.rate}. Объект страхования: {self.object}.' \
                                 f'Филиал страхования: {self.filial}. Вид страхования: {self.kind}'

        with open('contracts.json', 'w') as add:
            json.dump(contracts, add)


def main():
    with open('branches.json', 'r') as read:
        all_branches = json.load(read)

    with open('contracts.json', 'r') as read:
        all_contracts = json.load(read)

    while True:
        user_choice = input('Введите, что хотите сделать:\n1. Добавить филиал\n2. Добавить нового страхового агента\n'
                            '3. Оформить контракт\n4. Вывести все существующие филиалы\n'
                            '5. Вывести все заключенные контракты\n')

        if user_choice not in ['1', '2', '3', '4', '5']:
            print('Введите "1", "2", "3", "4", "5"')
        else:
            break

    if user_choice == '1':
        filial = Filial(input('Введите страну '), input('Введите край/область/округ '), input('Введите город '),
                        input('Введите улицу '), input('Введите номер дома '),
                        input('Введите номер строения (при отсутствии оставить пустым)'),
                        input('Введите номер квартиры '),
                        input('Введите название филиала '), input('Введите номер телефона филиала '), all_branches)
        filial.class_address.check_country()
        filial.class_address.check_building()
        filial.class_address.check_house()
        filial.class_address.check_flat()
        filial.class_phone.check_number()
        filial.add_filial()

    elif user_choice == '2':
        agent = Agent(input('Введите фамилию агента '), input('Введите имя агента '),
                      input('Введите отчество агента (если его нет, введите "0") '),
                      input('Введите название филиала, в котором работает агент '),
                      input('Введите номер телефона агента '))
        agent.check_nickname()
        agent.check_name()
        agent.check_middle()
        agent.check_filial(all_branches)
        agent.class_phone.check_number()
        agent.add_agent(all_branches)

    elif user_choice == '3':
        client_data = Client(input('Введите вашу фамилию '), input('Введите ваше имя '),
                             input('Введите ваше отчество '), input('Введите ваш номер телефона  '))
        client_data.check_nickname()
        client_data.check_name()
        client_data.check_middle()

        while True:
            unique_number = f'№ {randint(0, 999999):06.0f}'
            if unique_number not in all_contracts.keys():
                break

        print('\n'*3)
        contract = Insurance(unique_number, input('Введите дату подписания договора (в формате ЧЧ.ММ.ГГГГ) '),
                             input('Введите сумму договора (в рублях) '), input('Введите процентную ставку '),
                             input('Назовите объект страхования '),
                             input('Введите номер филиала, в котором был оформлен договор '),
                             input('Назовите вид страхования '),
                             client_data)
        contract.check_filial(all_branches)
        contract.check_cost()
        contract.check_date()
        contract.check_rate()
        contract.check_object()
        contract.check_kind()
        contract.add_contract(all_contracts)

    elif user_choice == '4':
        PrettyPrinter().pprint(all_branches)

    elif user_choice == '5':
        PrettyPrinter().pprint(all_contracts)


if __name__ == '__main__':
    main()
