# File          : enclosure_current.py
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


from enclosure_v9_7 import ZooEnclosure
import pickle_records

# List of current enclosures
current_enclosures= {}

# External file name
file_name = 'enclosures_current_record'

def preload_environments() -> dict:
    """
    Loading a list of environment objects to be used for the enclosures.
    Current parameters are random and cover all options for completion testing
    :return: current_environments dictionary
    """
    # Loading external file with environmental features preloaded (if needed)
    F0 = pickle_records.retrieve_record('F0 Environmental features')

    return F0

def generate_enclosures() -> dict:
    """
    Generating a list of enclosure objects to be used for assembly.
    Current parameters are random and cover all options for completion testing
    :return: current_enclosures dictionary
    """

    # Pre loaded enclosures profiles for testing
    ZooE_Z0_001 = ZooEnclosure('Z0','E8',True,1,5,250, 'F0')
    current_enclosures['ZooE_Z0_001'] = ZooE_Z0_001

    ZooE_Z1_002 = ZooEnclosure('Z1','E9',False,2,4,125, 'F0')
    current_enclosures['ZooE_Z1_002'] = ZooE_Z1_002

    ZooE_Z2_003 = ZooEnclosure('Z2','E0',True,3,3,375, 'F0')
    current_enclosures['ZooE_Z2_003'] = ZooE_Z2_003

    ZooE_Z3_004 = ZooEnclosure('Z3','E1',False,4,2,444, 'F0')
    current_enclosures['ZooE_Z3_004'] = ZooE_Z3_004

    ZooE_Z4_005 = ZooEnclosure('Z4','E2',True,5,1,10, 'F0')
    current_enclosures['ZooE_Z4_005'] = ZooE_Z4_005

    ZooE_Z5_006  = ZooEnclosure('Z5','E3',False,5,2,99, 'F0')
    current_enclosures['ZooE_Z5_006'] = ZooE_Z5_006

    ZooE_Z6_007 = ZooEnclosure('Z6','E4',True,4,3,258, 'F0')
    current_enclosures['ZooE_Z6_007'] = ZooE_Z6_007

    ZooE_Z7_008 = ZooEnclosure('Z7','E5',False,3,4,386, 'F0')
    current_enclosures['ZooE_Z7_008'] = ZooE_Z7_008

    ZooE_Z0_009 = ZooEnclosure('Z0','E6',True,2,5,412, 'F0')
    current_enclosures['ZooE_Z0_009'] = ZooE_Z0_009

    ZooE_Z1_010  = ZooEnclosure('Z1','E7',False,1,5,75, 'F0')
    current_enclosures['ZooE_Z1_010'] = ZooE_Z1_010

    ZooE_Z2_011 = ZooEnclosure('Z2','E8',True,2,3,89, 'F0')
    current_enclosures['ZooE_Z2_011'] = ZooE_Z2_011

    ZooE_Z3_012 = ZooEnclosure('Z3','E9',False,3,2,132, 'F0')
    current_enclosures['ZooE_Z3_012'] = ZooE_Z3_012

    return current_enclosures

def pickle_export() -> None:
    """
    Pickle function for saving the enclosure records in an external file
    :return:
    """
    # Saving an external copy of a dictionary with  enclosure objects
    pickle_records.save_record(current_enclosures, file_name)

def pickle_import() -> dict:
    """
    Pickle function for retrieving the enclosure records from an external file
    :return:
    """

    # Restoring from the external copy
    enclosures_restored = pickle_records.retrieve_record(file_name)
    return enclosures_restored

#generate_enclosures()
#pickle_export()