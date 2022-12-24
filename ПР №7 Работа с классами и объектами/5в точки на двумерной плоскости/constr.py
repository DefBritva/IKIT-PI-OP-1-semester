from classes import  Constraint


def get_constraint():
    """
    the function responsible for entering restrictions
    """
    while True:
        try:
            constraint_x = list(map(int, input('enter restrictions for points for x\n').split()))
        except ValueError:
            print('invalid input\n')
            continue
        if len(constraint_x) != 2:
            print('invalid input\n')
            continue
        try:
            constraint_y = list(map(int, input('enter restrictions for points for y\n').split()))
        except ValueError:
            print('invalid input\n')
            continue
        if len(constraint_y) != 2:
            print('invalid input\n')
            continue
        break
    con = Constraint(constraint_x, constraint_y)
    print(con)
    return con
