#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a + (0,) * 2
    b = tuple_b + (0,) * 2

    x = a[0] + b[0]
    y = a[1] + b[1]
    result = (x, y)
    return result
