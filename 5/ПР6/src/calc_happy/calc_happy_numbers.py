from .is_happy_number import is_happy_number


def calculate_happy_numbers(n=None):
    """
    Calculate how many happy numbers in
    list [0, n], where n is user input
    and shows this list. If n is not defined, generates it
    automatically

    :param: n: upper limit | None
    :return: list of happy numbers
    """

    upper_limit = n

    arr_of_numbers = []
    for i in range(upper_limit + 1):
        result = is_happy_number(i)
        if result[0]:
            arr_of_numbers.append(result[1])

    return arr_of_numbers
