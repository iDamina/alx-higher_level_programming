#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return (None)
    max_val = my_list[0]
    for each_item in my_list:
        if max_val is None or each_item > max_val:
            max_val = each_item

    return (max_val)
