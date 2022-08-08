#!/usr/bin/python3
"""
This program defines the class Square
"""


from .rectangle import Rectangle


class Square(Rectangle):
    """
    The class Square inherits from the Rectangle class.
    """

    # Constructor
    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor of a Square
        Args:
          - size: integer
          - x: integer
          - y: integer
          - id: integer
        """
        super().__init__(size, size, x, y, id)

    # Public Methods
    def update(self, *args, **kwargs):
        """
        Updates the attributes of the Square
        Args [either *args or **kwargs but not both]:
        id, size , x, y are all int types
          *args form:
            - Rectangle.update(id, size, x, y)
          **kwargs form:
            - Rectangle.update(id=int, size=int, x=int, y=int)
        """
        keys = ["id", "size", "x", "y"]
        len_keys, len_args = len(keys), len(args)

        # Maybe refactor because setter of size and use update
        if (args) and (args[0] is not None):
            length = len_keys if (len_args > len_keys) else len_args
            for i in range(length):
                setattr(self, keys[i], args[i])
        elif (kwargs is not None):
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return the representation of the Square Instance"""
        return ({
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y,
        })

    # Magic Methods
    def __str__(self):
        """Informal representation of a Square Instance"""
        return ("[{}] ({:d}) {:d}/{:d} - {:d}".format(
            type(self).__name__, self.id, self.x, self.y, self.width))

    # Getters and Setters
    @property
    def size(self):
        """Getter for the private attribute size"""
        return (self.width)

    @size.setter
    def size(self, value):
        """
        Setter for the private attribute size
        Args:
          - value: int
        """
        self.width = value
        self.height = value
