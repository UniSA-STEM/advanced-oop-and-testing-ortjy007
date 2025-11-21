# File          : gen_i_val.py
# Author        : Jorge Ortega
# Email id      : ortjy007@mymail.unisa.edu.au
# Description   : COMP 1048 advanced-oop-and-testing Assignment 2
#
# This is my own work as defined by the University's
# Academic Misconduct policy.

def digit_val_float(num, max=1000000000) -> float:
    """
    Function to validate input as digit as positive numbers as
    float with a maximum value
    :param max: int
    :param num: anything
    :return: float
    """
    # Dealing with empy inputs, None and zeroes as first input
    # bypasses all to fish
    if num is None or num == 0 or num == '':
        num = input(f'Please enter positive digits only:')
    # While loop with a try/except block to validate input
    while num:
        try:
            # Converting input to float AFTER digit validation
            num = float(num)
            # Validating number between boundaries
            if 0 < num < max:
                break
            # Validating for negative numbers
            elif 0 >= num:
                num = input(f'Please enter positive digits only:')
            # Validating for max number
            elif num > max:
                num = input(f'Please enter positive digits '
                            f'not exceeding {max}: ')
        # Catching Errors and requesting input to maintain loop
        except (ValueError, TypeError):
            num = input(f'Please enter positive digits only:')
    return round(num, 2)


def digit_val_int(num, max=1000000000) -> int:
    """
    Function to validate input as digit as positive numbers as
    an integer with a maximum value
    :param max: int
    :param num: anything
    :return: int
    """
    # Dealing with empy inputs, None and zeroes as first input
    # bypasses all to fish
    if num is None or num == 0 or num == '':
        num = input(f'Please enter positive digits only:')
    # While loop with a try/except block to validate input
    while num:
        try:
            # Converting input to float AFTER digit validation
            num = int(num)
            # Validating number between boundaries
            if 0 < num < max:
                break
            # Validating for negative numbers
            elif 0 >= num:
                num = input(f'Please enter positive digits only:')
            # Validating for max number
            elif num > max:
                num = input(f'Please enter positive digits '
                            f'not exceeding {max}: ')
        # Catching Errors and requesting input to maintain loop
        except (ValueError, TypeError):
            num = input(f'Please enter positive digits only:')
    return num


def str_YN_val_uc(str_) -> str:
    """
    Function to validate a str input in uppercase
    :param str_:
    :return: bool
    """
    # Dealing with empy inputs, None and zeroes as first input
    # bypasses all to fish
    if str_ is None or str_ == 0 or str_ == '':
        str_ = input(f'Please enter Y/N only:')

    # While loop with a try/except block to validate input
    while str_:

        try:
            # Converting input to uppercase AFTER validation
            str_ = str_.upper()

            # Validating characters
            if str_ == 'Y' or str_ == 'N':
                break
            else:
                str_ = input(f'Please enter Y/N only:')

        # Catching Errors and requesting input to maintain loop
        except (ValueError, TypeError):
            str_ = input(f'Please enter Y/N only:')
    return str_


def dict_choice(dict_: dict, choice) -> str:
    """
    Function to validate input selecting a key in
    a dictionary
    :param dict_: reference dictionary
    :param choice: selection
    :return: choice
    """

    # Printing dictionary for selection
    for key, value in dict_.items():
        print(f'{key}: {value}')

    # Input validation using while loop
    while choice not in dict_:
        try:
            choice = input(f'Please select a value from the list: ')

        except ValueError:
            print("Invalid input. Please enter a value in the list.\n")

    return choice


def list_choice_enum(options: list, choice: str) -> str:
    """
    Function to validate input selecting from a list
    :param choice: list
    :param options: str
    """
    # If valid option
    if choice in options:
        return choice

    else:
        # Printing list for user selection
        print('Please select an item:')
        for i, item in enumerate(options):
            print(f"{i + 1}. {item}")
        while True:
            try:
                choice = int(input('Enter the number of your choice: '))
                if 1 <= choice <= len(options):
                    selected_item = options[choice - 1]
                    print(f'You selected: {selected_item}')
                    return selected_item
                else:
                    print('Invalid choice. Please enter a number within the range.')
            except ValueError:
                print('Invalid input. Please enter a number.')


def bool_TF_val(bool_: bool) -> bool:
    """
    Function to validate a boolean input
    :param bool:
    :return: bool
    """
    # Dealing with empy inputs, None and zeroes as first input
    # bypasses all to fish
    if bool_ is None or bool_ == 0 or bool_ == '':
        bool_ = input(f'Please enter True or False only: ')

    # block to validate input
    try:
        # Validating characters
        if bool_ == False or bool_ == 'False' or bool_ == 'false' or bool_ == 'f' or bool_ == 'F' or bool_ == '' or bool_ == []:
            return False
        else:
            return True
    # Catching Errors and requesting input to maintain loop
    except (ValueError, TypeError):
        print('Invalid input, default False value used.')
        return False


def str_1(str_: str, prompt: str) -> str:
    """
    Function to validate input as at least one alphanumeric character
    :param str_:
    """
    # Validating Name
    # Dealing with empy inputs, None and zeroes as first input
    # bypasses all to fish
    if str_ is None or str_ == 0 or str_ == '':
        str_ = input(f'Your {prompt} can not be empty:')

    # While loop with a try/except block to validate input
    while str_.isalpha() == False:
        try:
            # Converting input to uppercase AFTER validation
            str_ = str_.capitalize()
            if str_:
                break
            else:
                str_ = input(f'Your {prompt} can not be empty:')
        # Catching Errors and requesting input to maintain loop
        except (ValueError, TypeError):
            str_ = input(f'Your {prompt} can not be empty:')
    return str_


def list_choice(options: list, choice: str) -> str:
    """
    Function to validate input selecting from a list
    :param choice:
    :param options: str
    """
    # If valid option
    if choice in options:
        return choice

    else:
        # Printing list for user selection
        print('Please select an item:')
        for i in options:
            print(f"{i}")
        while True:
            try:
                choice = input('Enter your choice: ')
                if choice in options:
                    print(f'You selected: {choice}')
                    return choice
                else:
                    print('Invalid choice. Please enter a name in the list.')
            except ValueError:
                print('Invalid input. Please enter a name.')


def dict_selection(dict_: dict) -> str:
    """
    Function to validate input selecting a key in
    a dictionary
    :param dict_: reference dictionary
    :param choice: selection
    :return: choice
    """

    # Printing dictionary for selection
    for key, value in dict_.items():
        print(f'{key}: {value}')

    # Graphics and obtaining the length of the dict for selection display
    print(f'{'>'}' * 3 )
    no_items = len(dict_)

    # Requesting user input
    choice = int(input(f'Please input your selection 1-{no_items} or 0 to exit: '))

    # Input validation using while loop
    while choice not in dict_ or choice == 0:

        if choice == 0:
            print('Exiting menu.')
            return choice
        else:
            try:
                choice = int(input(f'Please select a value from the list: '))
            except ValueError:
                print("Invalid input. Please enter a value in the list.\n")
    return choice