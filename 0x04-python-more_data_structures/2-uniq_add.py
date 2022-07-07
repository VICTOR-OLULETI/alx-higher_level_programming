#!/usr/bin/python3
def uniq_add(my_list=[]):
    newList = set(my_list)
    total = 0
    for i in newList:
        total += i
    return total
