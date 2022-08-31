#!/usr/bin/python3
def complex_delete(my_dict, value):
    tar = []
    for k, v in my_dict.items():
        if k is value:
            targets.append(k)
    for x in tar:
        del my_dict[x]
    return(my_dict)
