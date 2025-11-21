# File          : dict_edit.py
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

from printing_type import printing_dic

def add_type(dict_: dict) -> dict:
    """
    Appending a key-value to the dictionary
    :param dict_: to modify
    :return:  modified
    """
    # Select dictionary to modify
    dict_wip = dict_

    # Printing dictionary for selection
    printing_dic(dict_)

    # Getting last key:
    last_key = len(dict_wip)

    # Building new key
    new_key = 'E' + str(last_key + 1)

    # User input and capitalization
    new_enclosure = str(input('New enclosure type: '))
    new_enclosure = new_enclosure.capitalize()

    # 'Appending' value
    dict_wip.update({new_key: new_enclosure})

    # Saving
    dict_wip = dict_

    return dict_

def modify_type(dict_: dict) -> dict:
    """
    Editing a key-value to the dictionary
    :param dict_: to modify
    :return:  modified
    """
    # Select dictionary to modify
    dict_wip = dict_

    # Printing dictionary for selection
    printing_dic(dict_)

    # User input
    key_tb_modified = input('Select item to be modified: ')
    if key_tb_modified == '0':
        print('Nothing modified.')
        return dict_
    else:
        # Validation loop
        while key_tb_modified not in dict_wip:
            try:
                key_tb_modified = input('Item needs to in the list (0 to exit): ')
                if key_tb_modified == '0':
                    print('Nothing modified.')
                    return dict_

            except ValueError:
                print("Invalid input. Please enter a value in the list (0 to exit).\n")

        revised_value = str(input('Please add revised description: '))
        dict_wip.update({key_tb_modified: revised_value})

        print('The following value has been edited:\n'
              f'{key_tb_modified}: {revised_value}')

    return dict_

def remove_type(dict_: dict) -> dict:
    """
    Removing a key-value to the dictionary
    :param dict_: to modify
    :return:  modified
    """
    # Select dictionary to modify
    dict_wip = dict_

    # Printing dictionary for selection
    printing_dic(dict_)

    # User input
    key_tb_removed = input('Select item to be removed (0 to exit): ')
    if key_tb_removed == '0':
        print('Nothing removed.')
        return dict_
    else:
        # Validation loop
        while key_tb_removed not in dict_wip:
            try:
                key_tb_removed = input('Item needs to in the list (0 to exit): ')
                if key_tb_removed == '0':
                    print('Nothing removed.')
                    break
            except ValueError:
                print("Invalid input. Please enter a value in the list (0 to exit).\n")

        removed = dict_wip.pop(key_tb_removed)
        print('The following value has been removed:\n'
              f'{removed}')

    return dict_