#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    
    num_elements = len(my_list) - 1
    if idx < 0 or idx > num_elements:
        return my_list
    new_list = [x for x in my_list]
    new_list[idx] = element
    return new_list

