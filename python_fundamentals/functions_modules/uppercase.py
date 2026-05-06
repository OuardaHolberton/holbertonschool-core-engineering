#!/usr/bin/env python3

def uppercase(str):
    result = ""
    for char in str:
        ascii_code = ord(char)
        if 97 <= ascii_code <= 122:
            result += chr(ascii_code - 32)
        else:
            result += char
    print("{}".format(result))
