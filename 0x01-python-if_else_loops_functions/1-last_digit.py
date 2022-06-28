#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number1 = (number * -1) % 10
    number1 = -number1
else:
    number1 = number % 10
if number1 > 5:
    string = "and is greater than 5"
elif number1 == 0:
    string = "and is 0"
else:
    string = "and is less than 6 and not 0"
print("Last digit of {} is {} {}".format(number, number1, string))
