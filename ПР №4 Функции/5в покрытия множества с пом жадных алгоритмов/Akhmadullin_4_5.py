"""Ахмадуллин Рамиль
КИ22-16/1Б
вариант 5
практика 4
Напишите функцию, реализующую решение задачи покрытия
множества с помощью жадных алгоритмов.

Входные значения: словарь, ключи которого наименование
операторов сотовой связи, а значения – множества регионов, которые они
покрывают; множество всех регионов, которые необходимо покрыть.

Выходные значения: множество операторов сотовой связи, которые
работают во всех указанных регионах.

Жадный алгоритм:
а) выбрать оператора, покрывающего наибольшее количество
регионов, и еще не входящих в покрытие. Если оператор будет покрывать
некоторые регионы, уже входящие в покрытие, это нормально;
б) повторять, пока остаются непокрытые элементы множества
"""


def main():
    cover()


def cover():
    flag = True
    while flag:
        k = int(input('Введите кол-во операторов  '))
        phone_operator_regions = dict()
        while len(phone_operator_regions) != k:
            try:
                phone_operator_regions[input('Введите название  ')] \
                    = set(map(int, input('Список покрытия регионов оператором (формат ввода: 1 6 43 9 )  ').split()))
            except ValueError:
                print('Некорректный формат данных')
                continue
        try:
            regions = set(map(int, input('Введите множество регионов (формат ввода: 1 6 85 43 9 20)  ').split()))
        except ValueError:
            print('Ввод не соответствует формату')
            continue
        greedy_alg(phone_operator_regions, regions)
        flag = input('Начать заново? (ДА/НЕТ)  ') in 'ДАYESYesДадаyes'


def greedy_alg(phone_operator_regions, regions):
    phone_operator = list(phone_operator_regions)
    answer = []
    while regions != set():
        hit_max = name_of_max = 0
        for i in range(len(phone_operator)):
            hits = len(phone_operator_regions[phone_operator[i]] & regions)
            if hits > hit_max:
                hit_max = hits
                name_of_max = phone_operator[i]
        try:
            regions = regions.difference(phone_operator_regions[name_of_max])
            del phone_operator_regions[name_of_max]
            phone_operator.remove(name_of_max)
            answer.append(name_of_max)
        except KeyError:
            print('Один из регионов не входит в покрытие всех операторов')
            return
    print(answer)


if __name__ == '__main__':
    main()
