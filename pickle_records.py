# File          : save_retrieve_records.py
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

import pickle

def save_record(records_to_save, file_name):
    # Writing an external file for reference
    with open(file_name, 'wb') as f:
        pickle.dump(records_to_save, f)
    print(f'\nRecords successfully saved as: {file_name}.')

def retrieve_record(file_name_to_retrieve):
    # Extracting and external file for reference
    with open(file_name_to_retrieve, 'rb') as file:
        retrieved_data = pickle.load(file)
    print(f'\n{file_name_to_retrieve}\nRecords successfully retrieved.')
    return retrieved_data
