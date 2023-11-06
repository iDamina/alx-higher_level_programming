#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = my_list[:]
    index = 0
    for each_item in my_list:
        if each_item % 2 == 0:
            result[index] = True
        else:
            result[index] = False
        index += 1
    return (result)
