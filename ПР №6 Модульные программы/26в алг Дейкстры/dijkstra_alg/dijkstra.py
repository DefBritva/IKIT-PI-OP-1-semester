"""Набор функций для вычисления кратчайшего расстояния между узлами графа"""


def _set_graph(matrix_name):
    """
    Функция вычисляющая список смежности на основании матрицы смежности
    :param matrix_name: имя файла с матрицей смежности
    :return: dict, список смежности
    """

    try:
        with open(matrix_name, 'r', encoding='utf-8') as mat:
            wmatrix = list(map(lambda x:
                               list(map(int, x.replace('\n', '').split(' '))),
                               mat.readlines()))
    except ValueError:
        raise ValueError('Матрица задана некорректно')
    node_adj = {}
    for nnum, node in enumerate(wmatrix):
        conns = []
        for cnum, node_conn in enumerate(node):
            if node_conn != 0:
                conns.append((cnum, node_conn))
        node_adj[nnum] = tuple(conns)
    return node_adj


def _find_way(tree, start_n, end_n):
    """
    Функция, выполняющая поиск пути по дереву оптимальных путей графа
    :param tree: дерево оптимальных путей между узлами графа
    :param start_n: начальный узел
    :param end_n: конечный узел
    :return: tuple, кортеж с узлами, через которые проходит путь между заданными узлами
    """
    res = [end_n]
    cnode = end_n
    while cnode != start_n:
        cnode = tree[cnode]
        res.append(cnode)
    res.reverse()
    return tuple(res)


def dijkstra(matrix_name, start_n, end_n):
    """
    Функция, реализующая алгоритма Дейкстры
    :param matrix_name: имя файла с матрицей смежности
    :param start_n: качальный узел
    :param end_n: конечный узел
    :return: tuple, кортеж с узлами, через которые проходит путь между заданными узлами
    >>> dijkstra('matrix.txt', 1, 5)
    (12, (1, 2, 5))
    >>> dijkstra('matrix.txt', 2, 3)
    (6, (2, 1, 3))
    >>> dijkstra('matrix.txt', 2, 10)
    Traceback (most recent call last):
        ...
    ValueError: Начальный или конечный узел не присоединен к графу
    """
    node_adj = _set_graph(matrix_name)
    seen = set()
    inf = float('inf')
    weights = {i: [inf, 0] for i in node_adj.keys()}
    if start_n not in weights.keys() \
            or end_n not in weights.keys():
        raise ValueError('Начальный или конечный'
                         ' узел не присоединен к графу')
    weights[start_n][0] = 0
    while len(seen) != len(weights):
        cur_node = min(filter(lambda x: x[0] not in seen, weights.items()),
                       key=lambda x: x[1][0])[0]
        cur_weight = weights[cur_node][0]
        cnodes = node_adj[cur_node]
        for node, weight in cnodes:
            if node not in seen:
                tot_weight = cur_weight + weight
                if weights[node][0] > tot_weight:
                    weights[node][0] = tot_weight
                    weights[node][1] = cur_node
        seen.add(cur_node)
    tree = {node: data[1] for node, data in weights.items()}
    weights = {node: data[0] for node, data in weights.items()}
    return weights[end_n], _find_way(tree, start_n, end_n)
