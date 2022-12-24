from classes import Conteiner, Point


def counter():
    """
    function for entering points
    """
    try:
        count = int(input('enter the number of points\n'))
    except ValueError:
        print('invalid input\n')
    blank_sheet = Conteiner([])
    for _ in range(count):
        point = list(map(int, input('enter coordinates of point\n').split()))
        if len(point) != 2:
            print('invalid input\n')
            continue    
        point = Point(point)
        point.add_point(blank_sheet.conteiner)
    xy = blank_sheet.conteiner
    return xy
