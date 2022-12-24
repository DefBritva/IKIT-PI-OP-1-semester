from constr import get_constraint
from full_print import print_all_points
from count import counter
from answers import get_answer


def main():
    flag = True
    while flag:
        print("""select an action (enter the number):
    1 - entering constraints and coordinates of points
    2 - entering a new restriction
    3 - entering additional points
    4 - output of all data (constraints + coordinates of points)
    5 - end program execution\n""")
        action = None
        all_data = dict()
        try:
            action = int(input())
        except ValueError:
            print('invalid command\n')
        if action == 1:
            constraint = get_constraint()
            xy = counter()
            desired_points = get_answer(xy, constraint)
        elif action == 2:
            constraint = get_constraint()
        elif action == 3:
            xy = counter()
            desired_points = get_answer(xy, constraint)
        elif action == 4:
            print_all_points(constraint, desired_points, all_data)
        elif action == 5:
            flag = False
        else:
            print('invalid command\n')


if __name__ == '__main__':
    main()
