#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of a list that are integers
    Args:
        my_list (list): The list to print elements from.
        x (int): the number of elements of my_list to print.

    Returns:
        The number of elements printed
    """
    i, counter = 0, 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end='')
            counter += 1
        except (ValueError, TypeError):
            pass
        i += 1
    print("")
    return (counter)											     
