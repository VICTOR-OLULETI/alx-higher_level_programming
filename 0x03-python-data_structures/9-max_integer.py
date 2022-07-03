#!/usr/bin/python3
def max_integer(my_list=[]):
    max_num = 0
    for i in my_list:
        if i > max_num:
            max_num = i
    return (None if not my_list or len(my_list) <= 0 else max_num)
