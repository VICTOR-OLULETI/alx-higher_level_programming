#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if i == j:
            continue
        if i > j:
            continue
        else:
            print("{}".format(i), end="")
            if i < 8:
                print("{}".format(j), end=", ")
            else:
                print("{}".format(j))
