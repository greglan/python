# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
    Plot Euler's totient function
"""


import matplotlib.pyplot as plt


def primes(a, b):
    r = b % a
    while r != 0:
        b = a
        a = r
        r = b % a
    return a == 1


def phi(n):
    i = 1
    for k in range(2, n):
        if primes(k, n):
            i += 1
    return i


N = 1000
step = 2

x = [k for k in range(0, N, step)]
y = [phi(k) for k in x]

plt.xlabel(r'$n$')
plt.ylabel(r"$\varphi(n)$")
plt.xlim(0, N)
plt.scatter(x, y)
plt.show()
