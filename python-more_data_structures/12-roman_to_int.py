#!/usr/bin/python3
# Author: Joana Casallas
def roman_to_int(roman_string):
    """ convert a Roman numeral to an integer."""
    num = 0
    roman_dict = {
        "I": 1, "V": 5,
        "X": 10, "L": 50,
        "C": 100, "D": 500,
        "M": 1000
    }
    if roman_string != "":
        for i in range(len(roman_string)):
            if i != 0:
                if roman_string[i] != "I" and roman_string[i - 1] == "I":
                    num += roman_dict[roman_string[i]] - 2
                else:
                    num += roman_dict[roman_string[i]]
            else:
                num += roman_dict[roman_string[i]]
        return num
    return 0
