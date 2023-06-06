#!/usr/bin/python3

"""Print all combinations of two digits in ascending order.

    The two digits must be different - 01 and 10 are considered a combination.
    """
for num1 in range(0, 10):
    for num2 in range(num1 + 1, 10):
        if num1 == 8 and num2 == 9:
            print("{}{}".format(num1, num2))
        else:
            print("{}{}".format(num1, num2), end=", ")
