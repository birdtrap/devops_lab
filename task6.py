#!/usr/bin/env python
"""REVERSE EACH WORD IN STRING"""
STR = (input("Please enter string: "))

WORDS = STR.split()
N = len(WORDS)

for i in range(N):
    WORDS[i] = WORDS[i][::-1]

STR = ' '
print("%s" % (STR.join(WORDS)))
