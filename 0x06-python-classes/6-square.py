#!/usr/bin/python3
"""
Class Square with:
size, position (private properties)
methods which are area and print_square
getters & setters.
"""


class Square:
    """Class Square with size"""
    def __init__(self, size=0, position=(0, 0)):
        """Constructor for Class Square"""
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.size = size
        if (type(position) is not tuple) \
                or (position[0] and type(position[0]) is not int) \
                or (position[1] and type(position[1]) is not int) \
                or (position[0] < 0) \
                or (position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.position = position

    def area(self):
        """Method that returns the area of Square"""
        return (self.__size ** 2)

    def my_print(self):
        """ Method to print a Square"""
        if (self.__size == 0):
            print()
        else:
            for s in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)

    @property
    def size(self):
        """Getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size"""
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Getter for Private Position"""
        return self.__postion

    @position.setter
    def position(self, value):
        """Setter for position"""
        if (value[0] < 0) or (value[1] < 0) \
                or (type(value[0]) is not int) \
                or (type(value[1]) is not int) \
                or (len(value) != 2) \
                or (type(value) is not tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
