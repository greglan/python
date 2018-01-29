#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This file generates a list of wordlist given a input list of words, a prefix word, and a suffix word.
The output words all contain the PREFIX string and end with the SUFFIX string. between thos two strings, we insert
all the combinations of words given by the file 'words.txt'
It can be used in case you forget a password but remember the pattern you used.
"""
from itertools import combinations

PREFIX = ''
SUFFIX = ''

words = []
f_words = open('words.txt', 'r')
for line in f_words:
    words.append(line.strip())
f_words.close()

word_list = [PREFIX + ''.join(w) + SUFFIX for w in combinations(words)]

f_output = open('wordlist.txt', 'w')
for word in word_list:
    f_output.write(word+'\n')
f_output.close()
