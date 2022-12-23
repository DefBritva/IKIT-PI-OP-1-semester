def get_sum(n):
    symbols = list(str(n))
    return sum([int(x) ** 2 for x in symbols])


def is_happy_number(n):
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
