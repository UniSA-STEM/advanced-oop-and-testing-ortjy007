# File          : date_validation.py
# Author        : Jorge Ortega
# Email id      : ortjy007@mymail.unisa.edu.au
# Description   : COMP 1048 advanced-oop-and-testing Assignment 2
#
# This is my own work as defined by the University's
# Academic Misconduct policy.
#
from datetime import datetime, date


def validate_dob(year: int, month: int, day: int) -> datetime:
    """
    Function to validate date of birth (dob)
    :param day: int
    :param month: int
    :param year: int
    :return: str
    """
    lower_boundary = datetime.strptime('1900-01-01', '%Y-%m-%d')
    try:
        if year.is_integer() and month.is_integer() and day.is_integer() == True:
            date_string = str(year) + '-' + str(month) + '-' + str(day)
            formatted_date = datetime.strptime(date_string, '%Y-%m-%d')
            if formatted_date > datetime.now() or formatted_date < lower_boundary:
                print(f"Valid dates are between 1900 - and today.\nToday's date used as default.")
                return date.today()
            else:
                return formatted_date.date()
    except ValueError:
        print(f"Error.\nOnly integers with valid dates in the YYYY-MM-DD format are valid.\n"
             f"Today's date used as default.")
        return date.today()
    except Exception as e:
        print(f"An unexpected Error occurred:\n{e}.\nToday's date used as default.")
        return date.today()