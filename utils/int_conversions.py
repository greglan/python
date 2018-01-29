#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The goal of this file is to implement useful conversion for integers.
The functionalities are very close to Windows' calculator program
"""
from math import floor


def padding_4ch(s):
    """
    Add zeros to form 4 continuous characters and add spaces every 4 characters
    :type s: str
    """
    n = len(s)
    r = n % 4
    if r != 0:
        k = 4 - r
        s = k * '0' + s
    else:
        s = s
    s = s[::-1]
    s = ' '.join(s[i:i + 4] for i in range(0, len(s), 4))
    s = s[::-1]
    return s


def to_hex(x):
    if type(x) == int:
        if x >= 0:
            s = hex(x)
            return '0x' + padding_4ch(s[2:])


def from_hex(n):
    if type(n) == int:
        if n >= 0:
            return n


def logical_not(s):
    """
    Return the logical negation of the given binary string
    :param s: the string to convert
    :type s: str
    :return: str
    """
    ns = ''
    for c in s:
        if c == '0':
            ns += '1'
        elif c == '1':
            ns += '0'
        else:
            raise Exception("Invalid binary string")
    return ns


def formatBin(x):  # FIXME: use ? Change name
    """ Add bits to get a byte and add spaces every 4 digits """
    n = len(x)
    r = n % 8
    if r != 0:
        k = 8 - r
        s = k * '0' + x
    else:
        s = x
    s = ' '.join(s[i:i + 4] for i in range(0, len(s), 4))
    return s


def twoComplement(x):  # TODO
    """ Not fully working """
    s = bin(x)

    if x >= 0:
        return '0b' + formatBin(s[2:])
    else:
        # Strip '-' char
        s = s[3:]

        # Add missing bits
        n = len(s)
        r = n % 4
        if r != 0:
            s = (4 - r) * '0' + s

        print(s)

        # Logical not
        s = logical_not(s)
        print(s)

        s = int(s, 2) + 1
        print(bin(s))
        return '0b' + formatBin(bin(s)[2:])


def to_bin(x):
    if type(x) == int:
        return twoComplement(x)
