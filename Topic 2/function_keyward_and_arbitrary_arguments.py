"""
Program: function_keyward_and_arbitrary_arguments.py
Author: Alex Heinrichs
Last date modified: 10/12/2022

Contains a function average_scores that returns a string in a
specific format
"""


def average_scores(*args, **kwargs):
    """
    :param args: List of numbers to be averaged and added to gpa
    :param kwargs: List of keywords name, gpa, and course
    :return: A string of the name, averaged gpa, and course
    """
    string = "Result: "
    for key, value in kwargs.items():
        if key == "gpa":
            # Using *args for average calculation
            for score in args:
                value += score
            value /= len(args)
        string = string + ("%s = %s " % (key, value))

    return string


if __name__ == '__main__':
    print(average_scores(4, 3, 2, 4, name='Michelle',
                         gpa=0, course='Python'))
    print(average_scores(4, 2, 1, 1, 4, 3, name='Tony',
                         gpa=0, course='Java'))
    print(average_scores(4, name='Alex',
                         gpa=0, course='SQL'))
