#!/usr/bin/env python3
"""Module for safe integer printing."""


def safe_print_integer(value):
    """Print an integer with {:d} format."""
    try:
        if isinstance(value, bool):
            return False
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
