def get_sum(n):
    """
    Get sum of squares of every digit in number

    >>> get_sum(12)
    5

    >>> get_sum(23)
    13

    :param n: int
    :return: int, sum of squares
    """
    symbols = list(str(n))
    return sum([int(x) ** 2 for x in symbols])


def is_happy_number(n):
    """
    Check if number is happy

    >>> is_happy_number(5)
    (False, 5)

    >>> is_happy_number(1)
    (True, 1)

    :param n: int
    :return: (bool, n)
    """
    arr_of_nums = []
    curr = n
    while True:
        summ = get_sum(curr)
        if summ in arr_of_nums:
            return False, n
        if summ == 1:
            return True, n
        else:
            arr_of_nums.append(summ)
        curr = summ


def calculate_happy_numbers(n):
    """
    Calculate how many happy numbers in
    list [0, n], where n is user input
    and shows this list

    >>> calculate_happy_numbers(1)
    [1]

    >>> calculate_happy_numbers(20)
    [1, 7, 10, 13, 19]

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


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
