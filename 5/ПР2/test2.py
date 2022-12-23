def get_summ(n):
    symbols = list(str(n))
    return sum([int(x) ** 2 for x in symbols])


def is_happy_number(n):
    arr_of_nums = []
    curr = n
    while True:
        summ = get_summ(curr)
        if summ in arr_of_nums:
            return [False, n]
        if summ == 1:
            return [True, n]
        else:
            arr_of_nums.append(summ)
        curr = summ


def calculate_happy_numbers():
    try:
        upper_limit = int(input("Введите верхнюю границу поиска: "))

        if upper_limit <= 0:
            raise ValueError

        arr_of_numbers = []

        for i in range(upper_limit + 1):
            if is_happy_number(i)[0]:
                arr_of_numbers.append(is_happy_number(i)[1])

        print("Список 'счастливых' чисел: ", arr_of_numbers)

        if input("Повторить алгоритм? (y / n) ") == "y":
            calculate_happy_numbers()

    except ValueError:

        print("Введено некорректное значение! (n должно быть числом, n должно быть > 0)")
        calculate_happy_numbers()


def main():
    calculate_happy_numbers()


if __name__ == "__main__":
    main()
