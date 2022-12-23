
class Terminal:
    def __init__(self):
        pass

    seat = 0
    total_revenue = 0
    tickets_num = [i for i in range(1, 5000)]
    active_ticket = None
    films = [None, 'Drive', 'The Departed', 'American Psycho']
    sessions = []
    num_of_sessions = [range(1, len(sessions) + 1)]
    active_choise = []
    active_session = 0
    active_session_object = None
    list_of_sessions = []
    hall = None

    @classmethod
    def print_menu(cls):
        print('!!!WELCOME TO THE CINEMA KINOGO!!!')
        print()
        print('Movies for today:')
        print()
        j = 1
        for i in cls.films:
            if i != None:
                print(f'{i}. Number of session [{j}]')
                j += 1
        print()

    @classmethod
    def choise_session(cls):
        enter = input('enter session number ')
        cls.active_session = int(enter)
    def choise_seat(self):
        print(DATA[self.active_session])
        seat = int(input('Выберите место '))
        Terminal.seat = seat
        return self.seat

    @classmethod
    def payment(cls):
        choise = input('Точно хотите купить билет? ')
        while choise != 'Yes':
            choise = input('Хотите купить билет? ')

        pay = input('Приложите банковскую карту ')
        while pay != 'Приложить и оплатить':
            pay = input('Приложите банковскую карту!')
        print('Оплата прошла!')
        cls.total_revenue += 500

    @classmethod
    def take_ticket(cls):
        cls.active_ticket = cls.tickets_num[0]
        del cls.tickets_num[0]

    def take_seat(self, session=active_session, seat=None):
        if session == 1:
            if 1 <= seat <= 50:
                session1.hall[seat] = 'Место занято'
        elif session == 2:
            if 1 <= seat <= 200:
                session2.hall[seat] = 'Место занято'
        elif session == 3:
            if 1 <= seat <= 400:
                session3.hall[seat] = 'Место занято'

    def add_session(self, session):
        Terminal.sessions.append(session)

    @staticmethod
    def create_list_of_sessions(session1, session2, session3):
        Terminal.list_of_sessions = [0, session1, session2, session3]
class Session:
    def __init__(self):
        pass

    film = None
    hallseats = 0
    ticket_price = None
    times = None
    revenue_now = 0
    hall = None
    def choise_session_char(self, hallseats, ticket_price, times, film):
        self.hallseats = hallseats
        self.ticket_price = ticket_price
        self.times = times
        self.film = film

    @classmethod
    def calculate_revenue(cls, hall: dict, price: int):
        """ Подсчитать выручку """
        occupied_seats = len([hall[key] for key in hall if not (hall[key] is None)])
        revenue = price * occupied_seats
        cls.revenue_now = revenue
        print(revenue)


class Ticket(Terminal):
    def __init__(self,time = '18:00', ticket_num=Terminal.active_ticket):
        self.time = time
        self.film = None
        for i, k  in enumerate(Terminal.films):
            if i == Terminal.active_session:
                self.film = k
        self.seat = self.seat
        self.ticket_num = ticket_num

    def ticket_dilivery(self):
        ticket = Terminal.active_ticket
        print(f'получите билет номер {ticket} \n'
              f'Фильм {self.film} \n'
              f'время {self.time} \n')


class Hall(Session):
    def __init__(self, seats, screen_size):
        self.seats = seats
        self.screen_size = screen_size
        self.hall = {seat: None for seat in range(1, seats)}
        Terminal.hall = self.hall
        Session.hall = self.hall
little_hall = Hall(50, '6x8 meters')
medium_hall = Hall(200, '9x12 meters')  # создание кинозалов
big_hall = Hall(400, '12x16 meters')

terminal1 = Terminal()  # создание терминала

session1 = Session()
session1.choise_session_char(100, 500, '18:00', Terminal.films[1])
terminal1.add_session(session1)

session2 = Session()  # Создание сессий
session2.choise_session_char(200, 500, '18:00', Terminal.films[2])
terminal1.add_session(session2)

session3 = Session()
session3.choise_session_char(400, 500, '18:00', Terminal.films[3])
terminal1.add_session(session3)

Terminal.create_list_of_sessions(session1, session2, session3)


DATA = [None, little_hall.hall, medium_hall.hall, big_hall.hall]

while True:
    terminal1.print_menu()
    terminal1.choise_session()
    terminal1.choise_seat()
    terminal1.payment()
    Terminal.take_ticket()
    new_ticket = Ticket()
    new_ticket.ticket_dilivery()
    choise = input('Купить ещё билет? ([1] Yes or [2] No, go away)\n'
                   'Хотите узнать текущую прибыль кинотеатра с какого-нибудь сеанса '
                   'На данный момент? \n([Узнать прибыль 1 сеанса]\n'
                   '[Узнать прибыль 2 сеанса]\n'
                   '[Узнать прибыль 3 сеанса]\n')
    if choise == 'Yes':
        pass
    elif choise == 'No':
        break
    elif choise == 'Узнать прибыль 1 сеанса':
        session1.calculate_revenue(session1.hallseats, session1.ticket_price)
    elif choise == 'Узнать прибыль 2 сеанса':
        session2.calculate_revenue(session2.hallseats, session2.ticket_price)
    elif choise == 'Узнать прибыль 3 сеанса':
        session3.calculate_revenue(session3.hallseats, session2.ticket_price)
