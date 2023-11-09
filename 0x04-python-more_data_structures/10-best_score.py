#!/usr/bin/python3
def best_score(my_dict):
    if not my_dict:
        return None
    max_key = max(my_dict, key=my_dict.get)
    return (max_key)
