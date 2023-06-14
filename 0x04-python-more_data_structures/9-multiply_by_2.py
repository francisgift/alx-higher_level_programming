#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dik = a_dictionary.copy()
    lkeys = list(new_dik.keys())

    for r in lkeys:
        new_dik[r] *= 2

    return (new_dik)
