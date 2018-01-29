# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
    Sort the lines of the file.
"""

import os

os.chdir('/home/alan/Documents/Culture/Langues')
f = open('e.txt', 'r+')

lines = []
for line in f:
    lines.append(line)
lines.sort()

f.seek(0)
f.truncate()

for line in lines:
    f.write(line)

f.close()
