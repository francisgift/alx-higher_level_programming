#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    order = list(a_dictionary.keys())
    order.sort()
    for r in order:
        print("{}: {}".format(r, a_dictionary.get(r)))
