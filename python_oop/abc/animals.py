#!/usr/bin/env python3
"""Module that defines abstract Animal class and subclasses."""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class that represents an animal."""

    @abstractmethod
    def sound(self):
        """Return the sound of the animal."""
        pass


class Dog(Animal):
    """A class that represents a dog."""

    def sound(self):
        """Return the sound of a dog."""
        return "Bark"


class Cat(Animal):
    """A class that represents a cat."""

    def sound(self):
        """Return the sound of a cat."""
        return "Meow"
