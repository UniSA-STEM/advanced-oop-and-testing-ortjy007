# File          : enclosure_features.py
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

from validation import str_YN_val_uc
from validation import dict_choice
import enviroment_data


def assembly()-> dict:
    """
    Function to assemble the physical characteristics of the enclosure
    :return: dict
    """

    # Container for options as a dictionary
    enclosure_features = {}

    # Environment type selection
    print('Environment type: ')
    option = dict_choice(enviroment_data.ENVIRONMENT_TYPE, '')
    for key, value in enviroment_data.ENVIRONMENT_TYPE.items():
        if key == option:
            enclosure_features.update({key: value})
    print(f'Environment type updated to {enclosure_features[option]}\n')

    # Vegetation type selection
    print('Vegetation type: ')
    option = dict_choice(enviroment_data.VEGETATION_TYPE, '')
    for key, value in enviroment_data.VEGETATION_TYPE.items():
        if key == option:
            enclosure_features.update({key: value})
    print(f'Vegetation type updated to {enclosure_features[option]}\n')

    # Option to include water
    water = str_YN_val_uc(input('Does the enclosure has a body of water? (Y/N):\n'))

    if water == 'Y':

        # Water body type selection
        print('Water body type: ')
        option = dict_choice(enviroment_data.WATER_BODY_TYPE, '')
        for key, value in enviroment_data.WATER_BODY_TYPE.items():
            if key == option:
                enclosure_features.update({key: value})
        print(f'Water body type updated to {enclosure_features[option]}\n')


        # Water type selection
        print('Water type: ')
        option = dict_choice(enviroment_data.WATER_TYPE, '')
        for key, value in enviroment_data.WATER_TYPE.items():
            if key == option:
                enclosure_features.update({key: value})
        print(f'Water type updated to {enclosure_features[option]}\n')

        # Dry season selection
        print('Dry season: ')
        option = dict_choice(enviroment_data.DRYNESS, '')
        for key, value in enviroment_data.DRYNESS.items():
            if key == option:
                enclosure_features.update({key: value})
        print(f'Dry season updated to {enclosure_features[option]}\n')

    if water == 'N':

        # Dry season selection
        print('Dry season: ')
        option = dict_choice(enviroment_data.DRYNESS, '')
        for key, value in enviroment_data.DRYNESS.items():
            if key == option:
                enclosure_features.update({key: value})
        print(f'Dry season updated to {enclosure_features[option]}\n')

    return enclosure_features

