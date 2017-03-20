# -*- coding: utf-8 -*-

def naive(txt: str, w: str) -> list:
    """
    Naive method for string searching.
    :param txt: text to search the word in.
    :param w: word to be searched.
    :return: list of start indexes.
    """
    n = len(txt)
    m = len(w)
    indexes = []

    d = 0
    i = 0

    while d < n - m:
        if i == m:  # If a match is found.
            indexes.append(d)
            i = 0
            d += 1

        if txt[d + i] == w[i]:
            i += 1
        else:
            i = 0
            d += 1

    return indexes
