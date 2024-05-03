#!/usr/bin/python3
# Author: Joana Casallas
def list_division(my_list_1, my_list_2, list_length):
    """divide element by element 2 lists."""
    new_list = []
    for i in range(list_length):
        try:
            new_list.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
            continue
        except TypeError:
            print("wrong type")
            new_list.append(0)
            continue
        except IndexError:
            print("out of range")
            new_list.append(0)
    return new_list
