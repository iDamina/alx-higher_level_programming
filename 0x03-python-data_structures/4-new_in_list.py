#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if 0 <= idx < len(my_list):
        temp_list = my_list[:]
        temp_list[idx] = element
        return (temp_list)
    else:
        return (my_list)
