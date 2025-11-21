# File          : staff_current.py
# Author        : Jorge Ortega
# Email id      : ortjy007@mymail.unisa.edu.au
# Description   : COMP 1048 advanced-oop-and-testing Assignment 2
#
# This is my own work as defined by the University's
# Academic Misconduct policy.
from os import remove

# 100 % StarDust: Zoo Management Software(ZMS).
# Created by ByteWise Consulting.
# All rights unreserved.

# Submission rebuild 9.7
# Pixie dust added

from animal_v9_7 import Mammal
from animal_v9_7 import Reptilia
from animal_v9_7 import Aves
from animal_v9_7 import Ctenophora

import pickle_records

# List of current animals
current_animals= {}

# External file name
file_name = 'animals_current_record'

def generate_animals() -> dict:
    """
    Generating a list of animal objects to be used for assembly.
    Current parameters are random and cover all options for completion testing
    :return: current_animals dictionary
    """

    # Mammals
    m1 =  Mammal('Tigger', 'Panthera Tigris', 'D1', 'H1','J1', 'T0', 50,'2020-03-02','A1','R1',False,'ZooE_Z0_001')
    current_animals['m1'] = m1

    m2 =  Mammal('King Julien', 'Lemur catta', 'D2', 'H2','J2', 'T1', 35,'2021-02-01','A1','R2',True,'ZooE_Z0_001')
    current_animals['m2'] = m2

    m3 =  Mammal('Mort', 'Eulemur mongoz', 'D3', 'H3','J3', 'T3',  75,'2022-11-17','A1','R3',False,'ZooE_Z0_001')
    current_animals['m3'] = m3

    # Reptilia
    r1 =  Reptilia('Rango', 'Chamaeleo chamaeleon', 'D1', 'H4','J4', 'T4', 73, '2005-06-28','A3','R4',True,'ZooE_Z0_001')
    current_animals['r1'] = r1

    r2 =  Reptilia('Godzilla', 'Titanus Gojira', 'D1', 'H5','J5', 'T5', 500,'1954-10-27','A3','R1',False,'ZooE_Z0_001')
    current_animals['r2'] = r2

    r3 =  Reptilia('Kaa', 'Python bivittatus', 'D3', 'H6','J6', 'T6', 250,'1910-01-01','A3','R1',True,'ZooE_Z0_001')
    current_animals['r3'] = r3

    # Aves
    a1 =  Aves('Skipper', 'Pygoscelis adeliae', 'D1', 'HX','J5', 'T7', 123,'2001-08-23','A2','R1',False,'ZooE_Z0_001')
    current_animals['a1'] = a1

    a2 =  Aves('Rico', 'Pygoscelis adeliae', 'D1', 'H1','J4', 'T8', 123,'2005-12-24','A2','R2',True,'ZooE_Z0_001')
    current_animals['a2'] = a2

    a3 =  Aves('Kowalski', 'Pygoscelis adeliae', 'D1', 'H2', 'J3', 'T1', 123,'2008-04-30','A2','R3',False,'ZooE_Z0_001')
    current_animals['a3'] = a3

    """
    # Ctenophora
    c1 =  Ctenophora('Erine', 'Tentaculata', 'D1', 'H3', 'J2', 'T2', 100,'2020-06-12','A4','R4',False)
    current_animals['c1'] = c1

    c2 =  Ctenophora('Bernie', 'Nuda', 'D2', 'H4', 'J1', 'T3', 110,'2021-05-22','A4','R1',False)
    current_animals['c2'] = c2

    c3 =  Ctenophora('Granny', 'Scleroctenophora', 'D3', 'H5', 'J2', 'T4', 120,'2022-04-15','A4','R2',False)
    current_animals['c3'] = c3
    """

    return current_animals

def rep_keys_IDs() -> dict:

    current_keys = current_animals.keys()
    current_keys = list(current_keys)

    _IDs = []
    for i in current_animals:
        _IDs.append(current_animals[i]._ID)

    exchange = {}
    for key, id in zip(current_keys, _IDs):
        exchange[key] = id

    # Iterate over the keys to be renamed
    for key, id in exchange.items():
        if key in current_animals:  # Check if the old key exists
            current_animals[id] = current_animals.pop(key)

def pickle_export() -> None:
    """
    Pickle function for saving the animal records in an external file
    :return:
    """
    # Saving an external copy of a dictionary with animal objects
    pickle_records.save_record(current_animals, file_name)

def pickle_import() -> dict:
    """
    Pickle function for retrieving the animal records from an external file
    :return:
    """

    # Restoring from the external copy
    animals_restored = pickle_records.retrieve_record(file_name)
    return animals_restored

generate_animals()
rep_keys_IDs()

#pickle_export()

