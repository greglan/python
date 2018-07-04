#!/usr/bin/env python

import sys


def shift_time(line, shift):
    first_seconds = int(line[6:8]) + shift
    second_seconds = int(line[23:25]) + shift

    return line[:6] + str(first_seconds) + line[8:23] + str(second_seconds) + line[25:]


if len(sys.argv) < 3:
    print("Usage: %s subtitle.srt seconds" % sys.argv[0])

filename = sys.argv[1]
shift = int(sys.argv[2])
file = open(filename, 'r')

for line in file:
    if " --> " in line:
        new_line = shift_time(line, shift)
        print(new_line)
    else:
        print(line)

file.close()