#!/usr/bin/python3
"""
This program returns a list of lists of integers
representing the Pascal's triangle
"""


def pascal_triangle(n):
    """This function returns a list of lists of the
    pascal's triangle
    Args:
        n : length of triangle(integer type)
    """
    result = []
    if (n <= 0):
        return result

    first_element = [1]
    current = [1, 1]
    for i in range(1, n+1):
        r = 0
        m = 2
        if i == 1:
            result.append([1])
            continue
        if i == 2:
            result.append([1, 1])
            continue

        element = first_element[:]
        for j in range(i - 2):
            element.append(sum(current[r:m]))
            r += 1
            m += 1

        element += first_element
        result.append(element)
        current = element[:]
    return result
