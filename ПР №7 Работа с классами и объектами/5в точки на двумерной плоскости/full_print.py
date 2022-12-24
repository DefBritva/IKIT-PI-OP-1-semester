from classes import AllPoints


def print_all_points(constraint, desired_points, all_data):
    """
    the function responsible for storing all data,
    which are presented in the form of a dictionary, where
    the key is a set of constraints,
    and the values are the coordinates of the points (x,y)
    """
    constraint = str(constraint)
    all_data[constraint] = desired_points
    all_data = AllPoints(all_data)
    print(all_data)
