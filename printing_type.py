# File          : printing_type.py
# Author        : Jorge Ortega
# Email id      : ortjy007@mymail.unisa.edu.au
# Description   : COMP 1048 advanced-oop-and-testing Assignment 2
#
# This is my own work as defined by the University's
# Academic Misconduct policy.

# 100 % StarDust: Zoo Management Software(ZMS).
# Created by ByteWise Consulting.
# All rights unreserved.

# Submission rebuild 9.7
# Pixie dust added

def printing_dic(dict_) -> None:
    """
    :param dic_d:
    """
    # Printing dictionary
    for key, value in dict_.items():
        print(f'{key}: {value}')
    print()
