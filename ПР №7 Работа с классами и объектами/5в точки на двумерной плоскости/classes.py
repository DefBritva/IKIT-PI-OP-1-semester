class Point:
    """
    Class of points
    """
    def __init__(self, point):
        self.point = point

    def add_point(self, conteiner: list):
        """adding points to the container"""
        conteiner.append(self.point)

    def __str__(self):
        params = f'xy coordinate: {self.point}'
        return params


class Constraint:
    """
    constraint class for points
    """
    def __init__(self, constr_x, constr_y) -> None:
        self.constr_x = constr_x
        self.constr_y = constr_y
    def __str__(self):
        params = f'the border for x: {self.constr_x},'\
                    f'for y: {self.constr_y}.'
        return params


class Conteiner:
    """
    a container that stores points
    """
    def __init__(self, conteiner: list):
        self.conteiner = conteiner

    def __str__(self):
        params = f'points satisfying the constraint {self.conteiner}.'
        return params


class AllPoints:
    """
    container class for storing all entered data
    """
    def __init__(self, point_dataset: dict):
        self.point_dataset = point_dataset

    def __str__(self):
        params = f'all points and restrictions: {self.point_dataset}'
        return params
