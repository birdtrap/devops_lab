#!/usr/bin/env python
"""PALINDROM CHECKING"""
STR1 = (input("Please enter string: "))
STR2 = STR1[::-1]
if STR1 == STR2:
    print("string '%s' is polindrom" % (STR1))
else:
    print("string '%s' isn't polindrom" % (STR2))
