# File          : print_report.py
# Author        : Jorge Ortega
# Email id      : ortjy007@mymail.unisa.edu.au
# Description   : COMP 1048 advanced-oop-and-testing Assignment 2
#
# This is my own work as defined by the University's
# Academic Misconduct policy.

def print_b(report: dict) -> None:
    """
    Function to print Dictionaries
    :param report: Dict
    :return: None
    """
    if len(report) == 0:
        print('No comments\n')
    else:
        for key, value in report.items():
            print(f'{key} {value}')


def print_c(report: dict) -> None:
    """
    Function to print Dictionaries with colons
    :param report: Dict
    :return: None
    """
    if len(report) == 0:
        print('No comments\n')
    else:
        for key, value in report.items():
            print(f'{key}: {value}')


def print_n(report: dict) -> None:
    """
    Function to print nested Dictionaries without brackets/commas tec.
    :param report: Dict
    :return: None
    """
    report_s = (str(report)
                .replace('0', '')
                .replace('{', '')
                .replace('}', '')
                .replace("'", '')
                .replace(':', '')
                .replace(',', '\n'))

    if len(report_s) == 0:
        print('No comments\n')
    else:
        print(report_s)

