"""
Практика 2
КИ22-16/1Б
Ахмадуллин Рамиль
Вариант 5
table_key = tuple(input()) 1000,0010,1001,0000
table_inf = tuple(input()) 1362,9045,7219,6804 
"""
flag = True
while flag:
    data = []
    while len(data) != 4:
        t = input()
        try:
            test_for_numbers = int(t)
        except ValueError:
            print('Один из элементов или несколько не подходят под условие')
            continue
        data.append(t)
    table_key = tuple(data)
    # Ввод таблицы-ключа построчно
    data = []
    while len(data) != 4:
        t = input()
        try:
            test_for_numbers = int(t)
        except ValueError:
            print('Один из элементов или несколько не подходят под условие')
            continue
        data.append(t)
    table_inf = tuple(data)
    # Ввод таблицы построчно
    answer = ''
    for k in range(4):
        for x in range(4):
            for y in range(4):
                if table_key[x][y] == "1":
                    answer = answer + table_inf[x][y]
        table_rotated = []
        for j in range(4):
            table_line = ""
            for b in reversed(table_key):
                table_line += b[j]
            table_rotated.append(table_line)
        table_key = table_rotated
    print(answer)  # 1479321895246060
    flag = input('Начать заново? (ДА/НЕТ)  ') in 'ДАYESYesДадаyes'
