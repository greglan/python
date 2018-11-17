# -*- coding: utf-8 -*-


def naive(t: str, w: str) -> list:
    """
    Naive method for string searching.
    :param t: text to search the word in.
    :param w: word to be searched.
    :return: list of start indexes.
    """
    n = len(t)
    m = len(w)
    indexes = []

    d = 0
    i = 0

    while d < n - m:
        if i == m:  # If a match is found.
            indexes.append(d)
            i = 0
            d += 1

        if t[d + i] == w[i]:
            i += 1
        else:
            i = 0
            d += 1

    return indexes


def kmb_table():
    return None


def kmp():
    return None


def custom_hash(w):  # TODO: finish
    m = len(w)
    h = 0

    for i in range(m):
        h += ord(w[i]) * 2**(m-1-i)
    return h % q

# TODO: add other algorithm
# TODO: change filename if needed (one per algorithm)
