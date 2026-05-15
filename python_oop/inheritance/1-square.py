#!/usr/bin/env python3
"""Module that defines a Square class."""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """A class that represents a square."""

    def __init__(self, size):
        """Initialize square with size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
