"""
Ахмадуллин Рамиль
КИ22-16/1Б
вариант 15
Дано два набора случайных целых чисел размером N и M
соответственно.
Предусмотреть:
• ввод границ и размеров для первого и второго наборов (могут
быть различны)
• вывод исходных наборов на экран
• вывод сначала количества, а затем отсортированные по
возрастанию числа такие, что каждое число есть в обоих наборах
• вывод количества и отсортированные по возрастанию остальные
числа в первом наборе
• вывод количества и отсортированные по возрастанию числа во
втором наборе
"""
import random
flag = True
n_top_lim = m_top_lim = 0
n_bot_lim = m_bot_lim = 0
n_size = m_size = 0
while flag:
    try:
        n_size = int(input('Введите размер первого набора чисел '))
        n_bot_lim = int(input('Введите нижнюю границу первого набора '))
        n_top_lim = int(input('Введите верхнюю границу первого набора '))
    except ValueError:
        print('Not a number')
        continue
    n = set()
    if n_top_lim - n_bot_lim < n_size:
        print('error')
        continue
    while len(n) != n_size:
        i = random.randint(n_bot_lim, n_top_lim)
        while i not in n:
            n.add(i)
        else:
            continue
    try:
        m_size = int(input('Введите размер второго набора чисел '))
        m_bot_lim = int(input('Введите нижнюю границу второго набора '))
        m_top_lim = int(input('Введите верхнюю границу второго набора '))
    except ValueError:
        print('Not a number')
    m = set()
    if m_top_lim - m_bot_lim < m_size:
        print('error')
        continue
    while len(m) != m_size:
        j = random.randint(m_bot_lim, m_top_lim)
        while j not in m:
            m.add(j)
        else:
            continue
    intersect = n & m
    n_others = sorted(n - intersect)
    m_others = sorted(m - intersect)
    print(n)
    print(m)
    print(len(intersect), sorted(intersect))
    print(len(n_others), n_others)
    print(len(m_others), m_others)
    flag = input('start over? (Yes/No)  ') in 'ДАYESYesДадаyes'
