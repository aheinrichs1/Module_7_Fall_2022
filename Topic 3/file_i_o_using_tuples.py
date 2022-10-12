"""
Program: file_i_o_using_tuples.py
Author: Alex Heinrichs
Last date modified: 10/12/2022

takes a student's name and an unknown number of test scores,
stores them in a tuple, saves that tuple into a file,
and then finally prints the data from the file back to the screen
"""

import os as os


def write_to_file(student_tuple):
    """
    Writes a tuple of a student's name and list of test scores
    :param student_tuple: contains student's name and list of test scores
    """
    f = open('student_info.txt', 'a')
    for val in student_tuple:
        f.write(str(val) + ' ')
    f.write('\n')
    f.close()


def get_student_info(student_name):
    """
    Prompts user for input as many test scores as wished
    then sends a tuple containing student_name and test scores
    to write_to_file()
    :param student_name: string of student's name
    """

    print('Writing test score for ' + student_name)
    student_tuple = (student_name, [])
    while True:
        x = input("Please enter a test score, type -1 to exit: ")
        if x == '-1':
            break
        try:
            student_tuple[1].append(int(x))
        except ValueError:
            print("Value was not an int")
    write_to_file(student_tuple)


def read_from_file():
    """
    Reads file line by line, prints each line to the console
    """
    f = open('student_info.txt', 'r')
    print(f.read())
    f.close()


# driver
if __name__ == '__main__':
    open("student_info.txt", "w").close()
    get_student_info('Alex')
    get_student_info('Tabbi')
    get_student_info('Joe')
    get_student_info('Judy')
    read_from_file()
