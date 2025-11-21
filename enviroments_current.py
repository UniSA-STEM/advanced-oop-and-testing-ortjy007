# File          : enviroments_current.py
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


import enviroment_data
from enclosure_features import assembly
import pickle_records

# List of current enclosures
current_environments= []

# External file name
file_name = 'environments_current_record'

# Loading external file with environmental features preloaded (if needed)
# F0 = save_retrieve_records.retrieve_record('F0 Environmental features')

# Pre loaded environmental profiles for testing

ZooE_Z0_001 = ZooEnclosure('Z0','E8','True',1,5,250, 'F0','2020-01-01')
current_enclosures.append(ZooE_Z0_001)



#pickle_records.save_record(current_environments, 'environments_current_record')
#print(current_enclosures)

#restore = pickle_records.retrieve_record('environments_current_record')
#print(restore)

