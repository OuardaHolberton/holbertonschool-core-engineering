#!/usr/bin/env python3

def pow(a, b):
    result = 1
    if b < 0:
        return None
    for i in range(b):
        result *= a
    return result
