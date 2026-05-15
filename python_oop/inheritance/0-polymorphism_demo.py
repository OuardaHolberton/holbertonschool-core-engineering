#!/usr/bin/env python3


def safe_print_integer(value):
    """Print an integer with {:d} format."""
    try:
        if isinstance(value, bool):
            return False
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
