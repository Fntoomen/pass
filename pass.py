#!/usr/bin/env python

from sys import argv
from time import time
from random import randint
from string import printable

def password(n=256):
    chars = tuple(printable)
    randints = []
    passwd = ""
    for i in range(n):
        randints.append(randint(0, int(time())%(len(chars)+1)))
    for i in randints:
        passwd += chars[i]
    return passwd

if __name__ == "__main__":
    print(password(int(argv[1])))