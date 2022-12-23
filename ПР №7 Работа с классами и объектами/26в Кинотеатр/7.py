class Terminal:
    def __init__(self, seat=None):
        self.seat = seat

    tickets_num = [i for i in range(1, 5000)]
    active_ticket = None
    films = ['Drive', 'The Departed', 'American Psycho']
    sessions = [1, 2, 3]
    active_choise = []
    active_session = None

    @classmethod
    def print_menu(cls):
        j = 1
        for i in cls.films:
            print(f'{i}. Number of session [{j}]')
            j += 1

    @classmethod
    def choise_session(cls):
        enter = input('enter session number ')
        cls.active_choise.append('Session number - ' + enter + '. ')
        cls.active_session = int(enter)

    def choise_seat(self):
        print(DATA[self.active_session])
        seat = int(input('Выберите место '))
        self.seat = seat
        return self.seat

    @classmethod
    def payment(cls):
        print('Приложите банковскую карту')

    @classmethod
    def check_ticket(cls):
        cls.active_ticket = cls.tickets_num[0]
        del cls.tickets_num[0]


class Session:
    def __init__(self, hallseats, ticket_price, times, revenue=0):
        self.hallseats = hallseats
        self.ticket_price = ticket_price
        self.times = times
        self.revenue = revenue
        self.hall = {i: None for i in range(1, hallseats)}

    @staticmethod
    def calculate_revenue(hall: dict, price: int):
        """ Подсчитать выручку """
        occupied_seats = len([key for key in hall if not (hall[key] is None)])
        revenue = price * occupied_seats
        return revenue


class Ticket:
    def __init__(self, times, movie, seat, ticket_num=Terminal.active_ticket):
        self.times = times
        self.movie = movie
        self.seat = seat
        self.ticket_num = ticket_num
        Terminal.active_ticket = None

    def ticket_dilivery(self):
        for i in self.__dir__():
            if not ((i[0] == '_' and i[1] == '_') and (i[-1] == '_' and i[-2] == '_')):
                print(i)


class Hall:
    def __init__(self, seats, screen_size):
        self.seats = seats
        self.screen_size = screen_size
        hall = {seat: None for seat in range(seats)}


little_hall = Hall(50, '6x8 meters')
medium_hall = Hall(200, '9x12 meters')
big_hall = Hall(400, '12x16 meters')


terminal1 = Terminal()


session1 = Session(little_hall.seats, 500, '10:00')
session2 = Session(medium_hall.seats, 500, '11:00')
session3 = Session(big_hall.seats, 500, '12:00')


DATA = [None, session1.hall, session2.hall, session3.hall]

Terminal.print_menu()
Terminal.choise_session()
Terminal.payment()
Terminal.check_ticket()
seat = terminal1.choise_seat()


class Check():
    @staticmethod
    def check():
        if Terminal.active_session == 1:
            if 1 <= terminal1.seat <= 50:
                session1.hall[terminal1.seat] = 'Место занято'
                print(1)
                terminal1.seat = None
        elif Terminal.active_session == 2:
            if 1 <= terminal1.seat <= 200:
                session2.hall[terminal1.seat] = 'Место занято'
                terminal1.seat = None
        elif Terminal.active_session == 3:
            if 1 <= terminal1.seat <= 400:
                session3.hall[terminal1.seat] = 'Место занято'
                terminal1.seat = None


Check.check()
print(session1.calculate_revenue(DATA[1], session1.ticket_price))
print(session1.hall)
