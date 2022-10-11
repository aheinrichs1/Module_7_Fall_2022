"""
Program: basic_list.py
Author: Alex Heinrichs
Last date modified: 10/11/2022

Declares 2 functions make_list() to return a list of user input while
and get_input() to get one input and return it.
"""


def get_input():
    """
    :return: Returns a string, casts the input to desired type,
             raising exception on non-numeric input
    """

    return input("Enter a number: ")


def make_list(num):
    """
    :param num: number of times the get_input() function is looped
    :return: a list of all get_input() inputs
    """
    user_list = []
    for x in range(num):
        try:
            temp_num = float(get_input())
            user_list.append(temp_num)
        except ValueError:
            print("Error, non-numeric input")
    return user_list


if __name__ == "__main__":
    print(make_list(1))
    print(make_list(2))
    print(make_list(3))
