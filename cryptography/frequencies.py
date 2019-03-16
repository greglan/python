#!/bin/bash

input = "eTffm  ebauo toyruf varoti eahkc .ff8b3sfdrw9sqmweaur@deabffoosnceruti'yocmT fe lema obtuy uo rafovireth ca.kf bfs8d3wfsrm9equw@aerbdfaolnoesucirytc.moeTffm  ebauo tayruf varoti eahkc .ff8b3sfdrw9sqmweaur@deabffoosnceruti'yocmT fe lema obtuy uo rafovireth ca.kf bfs8d3wfsrm9equw@aerbdfaolnoesucirytc."

freq = {}

for c in input:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

print(freq)

"""
eTffm ebauo toyruf varoti eahkc 

.ff8b3sfdrw9sqmweaur@deabffoosnceruti'yocmT 
fe lema obtuy uo rafovireth ca.kf 
bfs8d3wfsrm9equw@aerbdfaolnoesucirytc.

mo

eTffm ebauo tayruf varoti eahkc 
.ff8b3sfdrw9sqmweaur@deabffoosnceruti'yocmT 

fe lema obtuy uo rafovireth ca.kf 
bfs8d3wfsrm9equw@aerbdfaolnoesucirytc.
"""
