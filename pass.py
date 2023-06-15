#!/usr/bin/env python

from sys import argv
from string import punctuation, digits, ascii_letters
import secrets

chars = punctuation + digits + ascii_letters

def password(n=256):
    return ''.join(secrets.choice(chars) for i in range(n))

if __name__ == "__main__":
    try:
        length = int(argv[1])
    except:
        length = int(input("Password length: "))
    print(password(length))
