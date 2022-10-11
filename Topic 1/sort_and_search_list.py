"""
Program: sort_and_search_list.py
Author: Alex Heinrichs
Last date modified: 10/11/2022

Passes a list into a sort_list() and search_list() function in the main
"""


def sort_list(user_list):
    """
    :param user_list: list to be sorted
    :return: sorted list
    """
    # sorts list
    user_list.sort()

    # I did not include a return statement as .sort() affects the
    # user_list within main


def search_list(user_list, var):
    """
    :param user_list: list to be searched
    :param var: variable to be searched for
    :return: index of searched variable
    """
    # I included a return of the index of the location of the
    # searched var
    return user_list.index(var)


if __name__ == "__main__":
    user_list = [3, 6, 7, 43, 2, 6, 4, 1, 78, 34, 2, 87]
    print(user_list)
    print("Sorted:")
    sort_list(user_list)
    print(user_list)
    var = 34
    print("Searching for index locations of var " + str(var))
    print(search_list(user_list, var))
