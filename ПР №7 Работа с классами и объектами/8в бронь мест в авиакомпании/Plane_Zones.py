class Plane:
    """
    Класс Самолёт
    Содержит конструктор __init__ и методы choose_plane, plane_seats,
    относящиеся к экземпляру класса.
    Конструктор __init__ принимает параметр экземпляра класса plane_type

    Пример: SI
    -> return: 5000 (Стоимость за самолёт)
    -> return 200 (Количество мест в самолёте)
    """

    def __init__(self, plane_type):
        """
        Конструктор объекта класса
        Экземпляр класса ринимает переменную plane_type
        :param: plane_type
        """
        self.plane_type = plane_type


    def choose_plane(self):
        """
        Метод объекта класса, возвращающий стоимость самолёта
        соответствующего типа
        Относится к экземпляру класса
        :return: стоимость самолёта

        Пример: NA
        -> 7000
        """
        if self.plane_type == 'NA':
            return 7000
        if self.plane_type == 'SA':
            return 10000
        if self.plane_type == 'AU':
            return 12000
        if self.plane_type == 'AF':
            return 5000
        if self.plane_type == 'EU':
            return 5000
        if self.plane_type == 'AS':
            return 5000
        if self.plane_type == 'FE':
            return 10000
        if self.plane_type == 'RS':
            return 8000
        if self.plane_type == 'UR':
            return 5000
        if self.plane_type == 'ER':
            return 5000
        if self.plane_type == 'SI':
            return 5000


    def plane_seats(self):
        """
        Метод объекта класса, возвращающий число мест
        самолёта соответствующего типа
        Относится к экземпляру класса
        :return: число мест в самолёте

        Пример: SA
        -> 200
        """
        if self.plane_type == 'NA':
            return 200
        if self.plane_type == 'SA':
            return 200
        if self.plane_type == 'AU':
            return 200
        if self.plane_type == 'AF':
            return 200
        if self.plane_type == 'EU':
            return 300
        if self.plane_type == 'AS':
            return 300
        if self.plane_type == 'FE':
            return 200
        if self.plane_type == 'RS':
            return 200
        if self.plane_type == 'UR':
            return 200
        if self.plane_type == 'ER':
            return 300
        if self.plane_type == 'SI':
            return 200

class Zone:
    """
    Класс Зона
    Содержит атрибуты класса (number_of_seats_e, number_of_seats_c,
    number_of_seats_b, number_of_seats_f), конструктор __init__ и
    методы класса zone_seats_amount, zone_pricing, относящиеся к
    экземпляру класса

    Пример: SI f
    -> 10
    -> 100000
    """

    number_of_seats_e = list()
    number_of_seats_c = list()
    number_of_seats_b = list()
    number_of_seats_f = list()


    def __init__(self, seats, zone_class):
        """
        Конструктор объекта класса
        Принимает переменные seats, zone_class
        :param: seats, zone_class
        """
        self.seats = seats
        self.zone_class = zone_class


    def zone_seats_amount(self):
        """
        Метод объекта класса, возвращающий список доступных мест зоны
        Относится к экземпляру класса
        :return: number_of_seats

        Пример: SI e
        -> 10
        """
        if self.zone_class == 'e':
            self.seats = int(self.seats * 0.6)
            number_of_seats_e = [str(number) for number in range(1, self.seats + 1)]
            return number_of_seats_e
        elif self.zone_class == 'c':
            self.seats = int(self.seats * 0.25)
            number_of_seats_c = [str(number) for number in range(1, self.seats + 1)]
            return number_of_seats_c
        elif self.zone_class == 'b':
            self.seats = int(self.seats * 0.1)
            number_of_seats_b = [str(number) for number in range(1, self.seats + 1)]
            return number_of_seats_b
        else:
            self.seats = int(self.seats * 0.05)
            number_of_seats_f = [str(number) for number in range(1, self.seats + 1)]
            return number_of_seats_f


    def zone_pricing(self):
        """
        Метод экземпляра класса, возвращающий цену за зону
        Относится к экземпляру класса
        :return: цена за зону

        Пример: ER c
        -> 20000
        """
        if self.zone_class == 'e':
            return 10000
        if self.zone_class == 'c':
            return 20000
        if self.zone_class == 'b':
            return 30000
        if self.zone_class == 'f':
            return 100000
