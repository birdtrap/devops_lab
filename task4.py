#!/usr/bin/env python
"""Each printed value must be formatted to the width of the binary value N"""

N = int(input("Please enter parametr N: "))
INDENT = len(str(bin(N)[2:])) + 1

for i in range(1, N+1):
    print('{:>{w}}{:>{w}}{:>{w}}{:>{w}}'.format(i, oct(i)[2:], hex(i)[2:], bin(i)[2:], w=INDENT))
