#!/usr/bin/python3
"""My Rectangle Class"""


class Rectangle:
    """Rectangle class with width and height"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Constructor of class Rectangle
                Args:
                    - width (default = 0): int
                    - height (default = 0): int
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """"Prints message when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.numbeer_of_instances -= 1

    def area(self):
        """Calculates Area of rectangle: width * height"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates Perimeter of the rectangle: 2 * (width + height)"""
        if (self.__width == 0) or (self.__height == 0):
            return 0

        return (2 * (self.__width + self.__height))

    def __str__(self):
        """Prints the rectangle with '#' character"""
        if (self.__width == 0) or (self.__height == 0):
            return ""
        str_rec = [str(self.print_symbol) * self.__width
                   for i in range(self.__height)]
        return '\n'.join(str_rec)

    def __repr__(self):
        """Return a string representation of the rectangle"""
        return f'Rectangle({self.__width}, {self.__height})'

    @property
    def width(self):
        """Getter for private instance width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for private instance width
                Args:
                    - value: int
        """
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for private instance height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the private instance height
                Args:
                    - value: int
        """
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the biggest rectangle based on area from the arguments
            Args:
                - rect_1: Rectangle
                - rect_2: Rectangle
        """
        if (not isinstance(rect_1, Rectangle)):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if (not isinstance(rect_2, Rectangle)):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (rect_1.area() >= rect_2.area()):
            return (rect_1)
        else:
            return (rect_2)
