#!/usr/bin/env python3
"""Module that defines a Square class."""


class Square:
    """A class that represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square with size and position."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter - return the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter - set the size with validation."""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter - return the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter - set the position with validation."""
        if (not isinstance(value, tuple) or len(value) != 2
                or not isinstance(value[0], int)
                or not isinstance(value[1], int)
                or isinstance(value[0], bool)
                or isinstance(value[1], bool)
                or value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the character #."""
        if self.__size == 0:
            print("")
            return
        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Return string representation of the square."""
        result = ""
        if self.__size == 0:
            return result
        for i in range(self.__position[1]):
            result += "\n"
        for i in range(self.__size):
            result += " " * self.__position[0] + "#" * self.__size
            if i < self.__size - 1:
                result += "\n"
        return result
