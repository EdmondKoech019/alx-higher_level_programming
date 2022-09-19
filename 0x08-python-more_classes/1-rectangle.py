#!/usr/bin/python3
"""
Module that has an empty class that defines a rectangle
"""


class Rectangle:
    """
    Class that defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Instantiation
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        Property to retrieve private attribute width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        property setter to set the value of width
        width must be an integer, otherwise raise TypeError
        width greater than 0, otherwise raise ValueError
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Property to retrieve the value of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Property setter. To set it;
        height must be an integer, otherwise raise TypeError.
        if height is < 0, raise ValueError.
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
