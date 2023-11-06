#!/usr/bin/python3
def no_c(my_string):
    rep_str = ""
    for char in my_string:
        if char not in "cC":
            rep_str += char
    return (rep_str)
