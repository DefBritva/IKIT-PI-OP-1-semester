"""
Модуль для тестрирования dijkstra,
при помощи библиотеки pytest
"""

from dijkstra_alg import __path__ as path
from ..dijkstra import dijkstra


def test_first_to_last():
    assert dijkstra(path[0] +
                    '\\tests\\test_matrix.txt', 1, 5) == (12, (1, 2, 5))


def test_last_to_first():
    assert dijkstra(path[0] +
                    '\\tests\\test_matrix.txt', 5, 1) == (12, (5, 2, 1))


def test_unconnected_nodes():
    try:
        dijkstra(path[0] + '\\tests\\test_matrix.txt', -1, 10)
    except ValueError as e:
        assert True, e


def test_some_nodes():
    assert dijkstra(path[0] +
                    '\\tests\\test_matrix.txt', 4, 1) == (7, (4, 0, 1))


def test_invalid_matrix():
    try:
        dijkstra(path[0] + '\\tests\\inv_test_matrix.txt', 1, 2)
    except ValueError as e:
        assert True, e
