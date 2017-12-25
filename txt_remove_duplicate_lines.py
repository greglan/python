# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
    Remove duplicate lines in a file and sort them
"""

import os
os.chdir('/home/alan/Documents/Culture/Langues')
f = open('e.txt', 'r+')

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
