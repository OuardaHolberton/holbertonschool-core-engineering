#!/usr/bin/env python3
"""Module that defines a Square class."""


class Square:
    """A class that represents a square."""

    def __init__(self, size=0):
        """Initialize a square with a given size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Getter - return the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter - set the size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the character #."""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)
