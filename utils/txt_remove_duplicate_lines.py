#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Remove duplicate lines in a file and sort them
"""
import sys

path = '/home/alan/Documents/Culture/Langues/e.txt'

if len(sys.argv) > 1:
    path = sys.argv[1]

f = open(path, 'r+')

lines = []
for line in f:
    if not line in lines:
        lines.append(line)
lines.sort()

f.seek(0)
f.truncate()

for line in lines:
    f.write(line)

f.close()
