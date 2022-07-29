#!/usr/bin/python3
def magic_string(value={'count': 0}):
    value['count'] += 1
    return ', '.join(['BestSchool'] * value['count'])
