#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    num = 0
    divisor = 0

    for value in my_list:
        num += value[0] + value[1]
        divisor += value[1]

    return (num / divisor)
