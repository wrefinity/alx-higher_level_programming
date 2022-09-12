#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    list_len = 0
    n_element = 0

    for _ in my_list:
        list_len += 1
    try:
        if (x == 0):
            return n_element
        if (x >= list_len):
            for e in my_list:
                print("{}".format(e), end ="")
            print()
            return list_len
        else:
            for e in my_list:
                n_element += 1
                print("{}".format(e), end="")
                if (n_element == x):
                    break
            print()
    except BaseException:
        pass
