#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    lkeys = list(a_dictionary.keys())

    for value_dic in lkeys:
        if value == a_dictionary.get(value_dic):
            del a_dictionary[value_dic]

    return (a_dictionary)
