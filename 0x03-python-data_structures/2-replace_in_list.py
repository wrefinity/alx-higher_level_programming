#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    num_elements = len(my_list) - 1 
    if idx < 0 or idx > num_elements:
        return my_list
    if my_list[idx]:
        my_list[idx] = element
    return my_list
