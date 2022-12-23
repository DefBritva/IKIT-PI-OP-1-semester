"""
<<<<<<< HEAD

=======
Гопиенко Александр
КИ22-17/2Б
>>>>>>> 2a8c1789734272fcbfc17adf71b844b6a110e9ce

Пример 1: команда - book
самолёт - EU
зона - c
ФИО - Малышев Николай Александрович
возраст - 18
дополнительная услуга - Вино
Место в зоне самолёта - 5
-> Ваши данные - пассажир Малышев Николай Александрович : тип самолёта EU,
зона c, номер сидения 5, ваша итоговая сумма 24300

Пример 2: команда - book
самолёт - NA
зона - f
ФИО - Гопиенко Александр Дмитриевич
возраст - 45
дополнительная услуга - Виски
Место в зоне самолёта - 11
-> В зоне f нет этого места

Пример 3 :команда - book
самолёт - ER
зона - h
-> Такой зоны не существует

Пример 4: команда - view
-> f : ['EU', 'e', 12000.0, '5']
Гопиенко Александр Дмитриевич : ['NA', 'f', 110000, '10']

Пример 5: команда - book
самолёт - FE
зона - f
ФИО - Сыроватский Евгений Владимирович
возраст - 14
дополнительная услуга - Виски
-> Какой тебе алкоголь, иди взрослей

"""
import instructions
import Book_persons
import Plane_Zones


def main():
    """
    Главная функция

    Принимает функции menu, plane_instructions,
    services, age_instructions из модуля instructions

    Классы Plane и Zone из модуля Plane_Zones

    Классы Booking и Passager из модуля Book_persons

    Пример 1:команда - pook
    -> Вы ввели неверную команду
    """
    while True:
        print('Авиакомпания OstroFly')
        print('Меню')
        instructions.menu()
        try:
            menu_option = input()
            if menu_option == 'END':
                print('Вы завершили работу программы')
                break
            if menu_option == 'book':
                print('Введите данные для бронирования')
                print('1) Введите самолёт, на котором полетите')
                print('Вы также можете завершить работы программы (введите END)')
                instructions.plane_instructions()
                avalaible_planes = ('NA', 'SA', 'AU', 'AF', 'EU', 'AS',
                                    'FE', 'RS', 'UR', 'ER', 'SI')
                plane = input()
                if plane not in avalaible_planes:
                    print('У нашей авиакомпании нет самолётов такого типа')
                    continue
                plane_choose = Plane_Zones.Plane(plane)
                price_for_plane = plane_choose.choose_plane()
                seats_in_plane = plane_choose.plane_seats()
                print('2) Выберете зону в самолёте')
                print('e - econom, c - comfort, b - bissiness, f - first')
                zones = ['e', 'c', 'b', 'f']
                zone = input()
                if zone not in zones:
                    print('Такой зоны не существует')
                    continue
                zone_seats = Plane_Zones.Zone(seats_in_plane, zone)
                numbers_of_places = zone_seats.zone_seats_amount()
                price_for_zone = zone_seats.zone_pricing()
                total_price = price_for_plane + price_for_zone
                print('3) Ваше ФИО')
                person_fio = input()
                digit_flag = False
                for element in person_fio:
                    if element.isdigit():
                        print('ФИО содержит цифры')
                        digit_flag = True
                        continue
                if digit_flag:
                    continue
                if Book_persons.Booking.book != {}:
                    fio_flag = False
                    for sim_fio in Book_persons.Booking.book.keys():
                        if person_fio == sim_fio:
                            print('Человек с таким же ФИО уже существует')
                            fio_flag = True
                            continue
                    if fio_flag:
                        continue
                print('4) Ваш возраст')
                instructions.age_instructions()
                person_age = int(input())
                if person_age < 0:
                    print('Не думаем, что вы настолько малы')
                    continue
                elif person_age == 0:
                    print('Приятного полёта, малыш')
                elif (person_age >= 100) and (person_age <= 200):
                    print('Да вы долгожитель')
                elif person_age > 200:
                    print('Да вы ходячая история')
                    continue
                print('Какое блюдо в полёт хотите вы выбрать? (необязательно)')
                instructions.services()
                print('Алкоголь можете брать с 18 лет!')
                person_service = input()
                avalaible_services = ['Виски', 'Бургер', 'Вино',
                                    'Коньяк', 'Стейк', 'Карабанара', 'Ничего']
                alcogol = ['Виски', 'Вино', 'Коньяк']
                if person_service == '':
                    print('Вы не ввели название услуги')
                    person_service = 'Ничего'
                if person_service not in avalaible_services:
                    print('У нашей авиакомании нет такой услуги')
                    person_service = 'Ничего'
                if person_service in alcogol and person_age < 18:
                    print('Какой тебе алкоголь, иди взрослей')
                person = Book_persons.Passager(person_fio, person_age, person_service)
                total_price += person.service_price()
                if person.age >= 0 and person_age < 14:
                    print('Вы получаете скидку 20% по возрасту(0-13)')
                    total_price = total_price * 0.8
                elif (person_age >= 14) and (person_age <= 18):
                    print('Вы получаете скидку 10% по возрасту (14-18)')
                    total_price = total_price * 0.9
                elif person_age >= 70:
                    print('Вы получаете скидку 20% по возрасту (70+)')
                print('5) Выберете номер сидения в вашем классе')
                print(f'Вы можете выбрать в классе {zone} номера мест'
                        f' от {numbers_of_places[0]} до {numbers_of_places[-1]}')
                seat_number = input()
                datas_in_database = [person_fio, plane, zone, seat_number]
                flag_taken = False
                for places in Book_persons.Booking.taken_seats_with_data:
                    if places[1] == plane and places[2] == zone:
                        if seat_number in places[3]:
                            print('Это место уже занято')
                            print('Выберете другое')
                            flag_taken = True
                if flag_taken:
                    continue

                taken_seats = set()
                for places in Book_persons.Booking.taken_seats_with_data:
                    if places[1] == plane and places[2] == zone:
                        taken_seats.add(seat_number)
                if taken_seats ^ set(numbers_of_places) == set():
                    print(f'Все места в самолёте {plane}, классе {zone}  заняты')
                    continue

                if (seat_number in numbers_of_places) and \
                        (datas_in_database not in Book_persons.Booking.taken_seats_with_data):
                    pasagers_params = [plane, zone, total_price, seat_number]
                    Book_persons.Booking.book[person.fio] = pasagers_params
                    Book_persons.Booking.add_seat_in_data(datas_in_database)
                    print(f'Ваши данные - пассажир {person_fio} : тип самолёта {datas_in_database[1]},'
                            f' зона {datas_in_database[2]}, номер сидения {datas_in_database[3]},'
                            f' ваша итоговая сумма {total_price}')
                    print('Приятного полёта!')

                if seat_number not in numbers_of_places:
                    print(f'В зоне {zone} нет этого места')
                    continue
            elif menu_option == 'view':
                booking = Book_persons.Booking()
                database = booking.get_dates()
                for key, value in database.items():
                    print(f"{key} : {value}")
            elif menu_option == 'del':
                if Booking.book == {}:
                    print('База данных пассажиров пустая')
                    continue
                else:
                    print('Введите ФИО пассажира, которого хотите удалить')
                    fio_del = input()
                    flag_pas = False
                    for pas in Book_persons.Booking.book.keys():
                        if pas != fio_del:
                            print('Такого пассажира нет')
                            flag_pas = True
                    if flag_pas:
                        continue
                    Book_persons.Booking.del_passagers(fio_del)
                    el_number = 0
                    for el in Book_persons.Booking.taken_seats_with_data:
                        if el[0] == fio_del:
                            del Book_persons.Booking.taken_seats_with_data[0]
                        else:
                            el_number += 1
            else:
                print('Вы ввели неверную команду')
                continue
        except ValueError:
            print('Неверный тип данных')


if __name__ == '__main__':
    """
    Точка входа функции
    """
    main()
