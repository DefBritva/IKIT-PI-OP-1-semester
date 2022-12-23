"""
4 Практическая работа. Вариант 26
Примеры работы программы:
1) Запускаем программу, выбираем 1 пункт, вводим путь к файлу с именем => "Матр
ица успешно задана." Выбираем пункт 2. Вводим узлы 0 5 => "Узлы успешно заданы"
Выбираем пункт 3 => <кратчайшее расстояние>, <оптимальный маршрут>
Завершаем работу программы.

2)Запускаем программу, выбираем несуществующий пункт => Нет такого варианта выб
ора. Завершаем программу.
3)Запускаем программу. Выбираем 3 пункт => "Матрица ещё не задана"

4)Запускаем программу. Завершаем программу

"""


class Graph:
    """Класс Графа, реализующий также пункты меню"""

    def __init__(self):
        """Инициализация экземляра Graph"""
        self.start_n, self.end_n = None, None
        self.node_adj = None

    def set_way(self):
        """Функция задания узлов для поиска пути"""
        self.start_n, self.end_n = \
            map(int, input('Введите начальный и конечный узлы:\n').split(' '))
        return 'Узлы успешно заданы'

    def set_graph(self):
        """Функция задания нового графа"""
        with open(input('Введите имя файла с матрицей:\n'), 'r', encoding='utf\
        -8') as mat:
            wmatrix = list(map(lambda x:
                               list(map(int, x.replace('\n', '').split(' '))),
                               mat.readlines()))
        self.node_adj = {}
        for nnum, node in enumerate(wmatrix):
            conns = []
            for cnum, node_conn in enumerate(node):
                if node_conn != 0:
                    conns.append((cnum, node_conn))
            self.node_adj[nnum] = tuple(conns)
        return 'Матрица успешно задана'

    def get_conn(self, node):
        """Функция, возвращающая все соединения для текущего узла"""
        return self.node_adj[node]

    def findway(self, tree):
        """Функция, выполняющая поиск пути по дереву оптимальных путей графа"""
        res = [self.end_n]
        cnode = self.end_n
        while cnode != self.start_n:
            cnode = tree[cnode]
            res.append(cnode)
        res.reverse()
        return tuple(res)

    def dijkstra(self):
        """Функция, реализующая алгоритма Дейкстры"""
        if self.node_adj is None:
            return 'Матрица еще на задана'
        if self.start_n is None:
            return 'Точки еще не заданы'
        seen = set()
        inf = float('inf')
        weights = {i: [inf, 0] for i in self.node_adj.keys()}
        if self.start_n not in weights.keys() \
                or self.end_n not in weights.keys():
            return 'Ошибка, начальный или конечный ' \
                   'узел не присоединен к графу'
        weights[self.start_n][0] = 0
        while len(seen) != len(weights):
            cur_node = min(filter(lambda x: x[0] not in seen, weights.items()),
                           key=lambda x: x[1][0])[0]
            cur_weight = weights[cur_node][0]
            cnodes = self.get_conn(cur_node)
            for node, weight in cnodes:
                if node not in seen:
                    tot_weight = cur_weight + weight
                    if weights[node][0] > tot_weight:
                        weights[node][0] = tot_weight
                        weights[node][1] = cur_node
            seen.add(cur_node)
        tree = {node: data[1] for node, data in weights.items()}
        weights = {node: data[0] for node, data in weights.items()}
        return weights[self.end_n], self.findway(tree)


graph = Graph()
menu = {'1': ('Задать имя файла с матрицей(Укажите путь к файлу)', graph.set_graph),
        '2': ('Задать начальные и конечные узлы(Нумерация начинается с 0)', graph.set_way),
        '3': ('Просчитать кратчайший маршрут между узлами', graph.dijkstra),
        '4': ('Завершить работу программы', exit)}

while True:
    printable_menu = '\n'.join(map(lambda y: ' - '.join(y),
                                   map(lambda x: (x[0], x[1][0]),
                                       menu.items())))
    opt = input(f"Выберете опцию:\n{printable_menu}\n")
    try:
        print(menu.get(opt)[-1]())
    except TypeError as e:
        print(e)
        print('Нет такого варианта выбора')
    except ValueError:
        print('Ошибка: матрица задана некорректно\nИЛИ\n'
              'Начальный и\\или конечный узел введен(ы) не корректно')
    except FileNotFoundError:
        print('Ошибка: Файла не существует')
