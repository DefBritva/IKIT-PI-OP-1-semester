"""
1.  input - 12
    output - 79, odd
2.  input - d
    output - Incorrect arguments (n must be int)
3.  input - -4
    output - Incorrect arguments (n >= 0)
4.  input - 2.4
    output - Incorrect arguments (n must be int)
"""


def get_central_polygonal_number(string_n):
    try:
        n = int(string_n)
        if n < 0:
            print("Incorrect arguments, (n >= 0)\n\nTry again)\n")
            get_central_polygonal_number(input("Enter n: "))
            return
    except ValueError:
        print("Incorrect arguments, (n must be int)\n\nTry again)\n")
        get_central_polygonal_number(input("Enter n: "))
        return
    res_num = int(((n * (n + 1)) / 2) + 1)
    if not (res_num % 2):
        message = "It is even"
    else:
        message = "It is odd"
    print("Central polygonal number is ", res_num, ". ", message, sep="")
    if input("Do u wanna run program again? (y / n) ") == "y":
        get_central_polygonal_number(input("Enter n: "))
        return


def main():
    a = None
    if (not a):
        print("helo")
    print("This is a program that displays the n-th central polygonal number.",
          "The central polygonal numbers show how many pieces a circle can be cut into using n lines\n", sep="\n")
    get_central_polygonal_number(input("Enter n: "))


if __name__ == "__main__":
    main()
