#!/usr/bin/python3
def roman_to_int(roman_string):
    if input is None:
        return 0
    if not isinstance(roman_string, str):
        return 0
    total = 0
    numeral = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(len(roman_string)):
        roman = numeral.get(roman_string[i])
        if roman is None:
            return 0
        if i > 0:
            prev = numeral.get(roman_string[i - 1])
        else:
            prev = 0
        if prev < roman:
            total += roman - prev - prev
        else:
            total += roman
    return total
