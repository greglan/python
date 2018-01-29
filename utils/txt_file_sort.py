#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Sort the lines of the file.
"""
import sys

path = '/home/alan/Documents/Culture/Langues/e.txt'

if len(sys.argv) > 1:
    path = sys.argv[1]

f = open(path, 'r+')

lines = []
for line in f:
    lines.append(line)
lines.sort()

f.seek(0)
f.truncate()

for line in lines:
    f.write(line)

f.close()
