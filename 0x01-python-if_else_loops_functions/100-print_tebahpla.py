#!/usr/bin/python3

""""Print the alphabet in reverse order"""
i = 0
for b in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(b - i)), end="")
    i = 32 if i == 0 else 0
