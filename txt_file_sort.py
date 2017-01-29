# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
os.chdir('E:/Documents/Google Drive/Culture/Langues')
f = open('s.txt', 'r+')
lines = []
for line in f:
    lines.append(line)
lines.sort()
f.seek(0)
f.truncate()
for line in lines:
    f.write(line)
f.close()
