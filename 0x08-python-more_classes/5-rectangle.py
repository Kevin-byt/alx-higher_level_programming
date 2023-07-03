#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): rectangle width.
            height (int): rectangle height.
        """
        self.width = width
        self.height = height

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        # returns the area of the Rectangle
        return self.__height * self.__width

    def perimeter(self):
        # returns the perimeter of the Rectangle
        if (self.__height == 0 or self.__width == 0):
            return 0

        return (2 * (self.__height + self.__width))

    def __str__(self) -> str:
        # returns the visual of the rectangle using '#' to rep a unit length
        if (self.__width == 0 or self.__height == 0):
            return ("")

        rec = []
        for y in range(self.__height):
            [rec.append('#') for x in range(self.__width)]

            if y != self.__height - 1:
                rec.append('\n')

        return ("".join(rec))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        print("Bye rectangle...")
