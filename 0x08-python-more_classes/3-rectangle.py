#!/usr/bin/python3
"""
Rectangle class
"""

class Rectangle:
    """variables and methods"""

    def __init__(self, width=0, height=0):
        """initialize attributes"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getwidth"""
        return self.__width

    @width.setter
    def width(self, value):
        """setwidth"""
        if isinstance(value, int) and value >= 0:
            self.__width = value
        elif not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """getheight"""
        return self.__height

    @height.setter
    def height(self, value):
        """setheight"""
        if isinstance(value, int) and value >= 0:
            self.__height = value
        elif not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        """area method, evaluate rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """perimeter method, evaluate rectangle perimeter"""
        return (self.__width + self.__height) * 2

    def __str__(self):
        """
        special __str__ method for printing a rectangle
        when print(self) is called
        """
        pattern = ''
        if self.__width is 0 or self.__height is 0:
            return pattern
        else:
            for j in range(self.__height):
                for i in range(self.__width):
                    pattern += '#'
                if j is not (self.__height - 1):
                    pattern += '\n'
            return pattern
