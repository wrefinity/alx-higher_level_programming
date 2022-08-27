#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    n = len(my_list)
    cpy = my_list.copy()
    if idx < 0:
        return _cpy
    elif idx > n - 1:
        return cpy
    else:
        cpy[idx] = element
        return cpy
