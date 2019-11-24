"""
    Collections of functions used in arithmetics
"""

from math import *


def divisors_list(n):
    """ Returns the list of divisors of n """
    return [d for d in range(1, n // 2 + 1) if n % d == 0] + [n]


def odd_numbers_list(n):
    """ Returns the list of n first odd numbers """
    return [2 * k - 1 for k in range(1, n + 1)]


def even_numbers_list(n):
    """ Returns the list of n first even numbers"""
    return [2 * k for k in range(0, n)]


def is_prime(n):
    if n == 2:
        return True
    elif n == 0 or n == 1 or n % 2 == 0:
        return False
    else:
        i = 3
        while (i <= int(sqrt(n))):
            if n % i == 0:
                return False
            i += 2
        return True


def primes(a, b):
    r = b % a
    while r != 0:
        b = a
        a = r
        r = b % a
    return a == 1


def primes_2(p,q):
    if p > q:
        return p/q != p//q
    else:
        return primes(q,p)


def phi(n):
    """ Euler's totient function """
    i = 1
    for k in range(2, n):
        if primes(k, n):
            i += 1
    return i
    

def is_perfect(n):
    return sum(divisors_list(n)) - n == n


def non_multiples(a, b, p):
    """
    Retourne la liste des entiers compris entre a et b non-multiples de p
    :param a:
    :param b:
    :param p:
    :return:
    """
    return [k for k in range(a, b + 1) if k % p != 0]


def prime_factors(n):
    l = []
    i = 2
    while i <= n:
        if n % i == 0:
            l.append(i)
            n = n / i
        i += 1
    return l


def gcd_rec(a, b):
    if b == 0:
        return a
    else:
        return gcd_rec(b, a % b)


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def euclid_extended_rec(a, b):
    if b == 0:
        return a, 1, 0
    else:
        q, r = divmod(a, b)
        d, u, v = euclid_extended_rec(b, r)
        return d, v, u - q * v


def euclid_extended(a0, b0):  # invariant : a0*u + b0*v = a et a0*x + b0*y = b
    a, u, v, b, x, y = a0, 1, 0, b0, 0, 1
    while b != 0:
        q, r = divmod(a, b)
        a, u, v, b, x, y = b, x, y, r, u - x * q, v - y * q
    return a, u, v
