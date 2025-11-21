# File          : staff_current.py
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

from staff_v9_7 import Staff
import pickle_records

# List of current staff
current_staff= {}

#external file name
file_name = 'staff_current_record'

def generate_staff() -> dict:
    """
    Generating a list of staff objects to be used for assembly.
    Current parameters are random and cover all options for completion testing
    :return: current_staff dictionary
    """

    # Pre loaded staff profiles for testing
    s1 = Staff('Cat', 'Stevens', '1948-07-21', 'G0', 'W0', 'Q0', 'R0')
    current_staff['s1'] = s1

    s2 = Staff('Katy', 'Gallagher', '1970-03-18', 'G1', 'W1', 'Q1', 'R1')
    current_staff['s2'] = s2

    s3 = Staff('Patrick', 'Gorman', '1984-12-12', 'G2', 'W2', 'Q2', 'R2')
    current_staff['s3'] = s3

    s4 = Staff('Rebecca', 'White', '1983-02-04', 'G3', 'W3', 'Q3', 'R3')
    current_staff['s4'] = s4

    s5 = Staff('Andrew', 'Charlton', '1978-09-26', 'G4', 'W4', 'Q4', 'R4')
    current_staff['s5'] = s5

    s6 = Staff('Richard', 'Marles', '1967-07-13', 'G0', 'W5', 'Q5', 'R5')
    current_staff['s6'] = s6

    s7 =  Staff('Penny', 'Wong', '1968-12-05', 'G1', 'W6', 'Q6', 'R6')
    current_staff['s7'] = s7

    s8 = Staff('Jim', 'Chalmers', '1978-03-02', 'G2', 'W0', 'Q7', 'R0')
    current_staff['s8'] = s8

    s9 =  Staff('Tony', 'Burke', '1969-12-04', 'G3', 'W2', 'Q8', 'R1')
    current_staff['s9'] = s9

    s10 = Staff('Catherine', 'King', '1966-06-02', 'G4', 'W2', 'Q9', 'R2')
    current_staff['s10'] = s10

    return current_staff

def pickle_export() -> None:
    """
    Pickle function for saving the staff records in an external file
    :return:
    """
    # Saving an external copy of a dictionary with staff objects
    pickle_records.save_record(current_staff, file_name)

def pickle_import() -> dict:
    """
    Pickle function for retrieving the staff records from an external file
    :return:
    """

    # Restoring from the external copy
    staff_restored = pickle_records.retrieve_record(file_name)
    return staff_restored

#generate_staff()
#pickle_export()