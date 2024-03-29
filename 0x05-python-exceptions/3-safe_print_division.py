#!/usr/bin/python3

def safe_print_division(a, b):
    """Returns the division of a by b."""
    try:
        quo = a / b
    except (TypeError, ZeroDivisionError):
        quo = None
    finally:
        print("Inside result: {}".format(quo))
    return (quo)
