#!/usr/bin/python3
def print_last_digit(number):
    if number == 0:
        lst = 0
        print("{}".format(lst), end="")
        return 0
    elif number > 0:
        lst = number % 10
        print("{}".format(lst, end="")
        return lst
    elif number < 0:
        number *= -1
        lst = number % 10
        print("{}".format(lst), end="")
        return lst
