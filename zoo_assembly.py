# File          : zoo_assembly.py
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

import animal_v9_7
import animals_current
import animal_data

import enclosure_v9_7
import enclosure_current
import enclosure_data

import zoo_zones

import staff_v9_7
import staff_current
import staff_data

import validation
import print_report
import pickle_records

# Containers for main assembled data
CURRENT_STAFF = {}
CURRENT_ANIMALS = {}
CURRENT_ENCLOSURES = {}

# Populating containers
CURRENT_STAFF = staff_current.pickle_import()
CURRENT_ANIMALS = animals_current.pickle_import()
CURRENT_ENCLOSURES = enclosure_current.pickle_import()

# Coupling animals, enclosures and staff
#def ZooEis():

#x = animal_v9_7.Mammal('Tigger', 'Panthera Tigris', 'D1', 'H1', 'J1', 'T0', 50, '2020-03-02', 'A1', 'R1', False, 'ZooE_Z0_001')
#print(x)

#print(CURRENT_ANIMALS)
#print(CURRENT_ANIMALS['mammal_1'].name)

#y = animals_current.pickle_import()

#print(y)
#print(y['mammal_1'].name)

#print(CURRENT_STAFF)

def staff_display(d_type: int) -> None:
    """
    display options for staff
    :param d_type: int
    """
    if isinstance(d_type, int):
        if d_type == 1:
            counter = 0
            print(f'\n{'=' * 10} Staff List {'=' * 10}\nName | Qualification')
            for i in CURRENT_STAFF:
                counter += 1
                print(f'{counter}: {CURRENT_STAFF[i].name} {CURRENT_STAFF[i].last_name} | {staff_data.QUALIFICATIONS[CURRENT_STAFF[i].qualifications]}')
            print(f'{'=' * 33}')
        if d_type == 2:
            for key, value in CURRENT_STAFF.items():
                print(f'Staff record: {key}\n{value}')
    else:
        d_type = int(input('Please select 1 if a simple table or 2 for full records:'))

def animal_display(d_type: int) -> None:
    """
    display options for animals
    :param d_type: int
    """
    if isinstance(d_type, int):
        # Simplified list
        if d_type == 1:
            counter = 0
            print(f'\n{'=' * 10} Animal List {'=' * 10}\nName - Species | Enclosure')
            for i in CURRENT_ANIMALS:
                counter += 1
                print(f'{counter}: {CURRENT_ANIMALS[i].name} - {CURRENT_ANIMALS[i].species} | {CURRENT_ANIMALS[i].enclosure}'
                      )
            print(f'{'=' * 33}')

        # Simplified Health Records
        if d_type == 2:
            counter = 0
            print(f'\n{'=' * 10} Animal List {'=' * 10}\nName - Species\nHealth Status | Injury Status | Treatment\n{'=' * 33}')
            for i in CURRENT_ANIMALS:
                counter += 1
                print(f'{counter}: {CURRENT_ANIMALS[i].name} - {CURRENT_ANIMALS[i].species}:\n'
                      f'{(animal_data.HEALTH[CURRENT_ANIMALS[i].health])} | '
                      f'{(animal_data.INJURY[CURRENT_ANIMALS[i].injury])} | '
                      f'{(animal_data.TREATMENT[CURRENT_ANIMALS[i].treatment])}\n'
                      )
            print(f'{'=' * 33}')

        if d_type == 3:
            counter = 0
            print(f'\n{'=' * 10} Animal List {'=' * 10}\nName - Species\nDiet | Diet notes\n{'=' * 33}')
            for i in CURRENT_ANIMALS:
                counter += 1
                print(f'{counter}: {CURRENT_ANIMALS[i].name} - {CURRENT_ANIMALS[i].species}:\n'
                      f'{(animal_data.DIET[CURRENT_ANIMALS[i].diet])} | '
                      f'{(animal_data.INJURY[CURRENT_ANIMALS[i].print_dietary_comments()])}'
                      )
            print(f'{'=' * 33}')

        # List with keys for selection
        if d_type == 3:
            print(f'\n{'=' * 10} Animal List {'=' * 10}\nName - Species | Enclosure')
            for key, value in CURRENT_ANIMALS.items():
                print(f'{key}: {value.ANIMAL_ID}')

        # All details
        if d_type == 5:
            for key, value in CURRENT_ANIMALS.items():
                print(f'Animal record: {key}\n{value}')


    else:
        d_type = int(input('Please select 1 if a simple table or 2 for full records:'))

def enclosures_display(d_type: int) -> None:
    """
    display options for enclosures
    :param d_type: int
    """
    if isinstance(d_type, int):
        if d_type == 1:
            counter = 0
            print(f'\n{'=' * 9} Enclosure List {'=' * 9}\nZone - Type | Enclosure_ID')
            for i in CURRENT_ENCLOSURES:
                counter += 1
                print(f'{counter}: {zoo_zones.ZOO_ZONES[CURRENT_ENCLOSURES[i].location]} - {enclosure_data.ENCLOSURE_TYPE[CURRENT_ENCLOSURES[i].type_]} | {CURRENT_ENCLOSURES[i].id_}')
            print(f'{'=' * 33}')
        if d_type == 2:
            for key, value in CURRENT_ENCLOSURES.items():
                print(f'Enclosure record: {key}\n{value}')
    else:
        d_type = int(input('Please select 1 if a simple table or 2 for full records:'))

#staff_display(1)
animal_display(3)
#enclosures_display(1)


MAIN_MENU = {1: 'Animal Management',
             2: 'Enclosure Management',
             3: 'Staff Management',
             }

ANIMAL_MANAGEMENT = {1: 'List of Current Animals',
                     2: 'Individual Animal Records',
                     3: 'Health and Care Records',
                     4: 'Diet Records',
                     5: 'Other Records'
                     }

ENCLOSURE_MANAGEMENT = {1: 'List of Current Enclosures',
                        2: 'Individual Enclosures Records',
                        3: 'Cleaning and Maintenance',
                        4: 'Moving Animals',
                        }

STAFF_MANAGEMENT  = {1: 'List of Current Staff',
                     2: 'Individual Staff Records',
                     3: 'Animal Care Teams',
                     4: 'Enclosure Care Teams',
                     5: 'Grounds and Admin Teams',
                     6: 'Rsearch Teams',
                     7: 'Visitor and Event teams',
                     }


#print(CURRENT_ANIMALS)
#print(CURRENT_ANIMALS['A1001'])



"""
print(f'\n{'=' * 15} ZooE Main Menu {'=' * 15}')
selection = validation.dict_selection(ANIMAL_MANAGEMENT)
if selection == 1:
    animal_display(1)

elif selection == 2:

    # Display list for information
    animal_display(1)

    # Compiling keys for matching
    animal_keys = list(CURRENT_ANIMALS.keys())
    no_animals = [i for i in range(1, len(CURRENT_ANIMALS))]

    # Requesting user input
    [i for i in range(1, len(ANIMAL_MANAGEMENT))]
    animal_no = int(input('Please input the numer of the animal records you want to retrieve or 0 to exit: '))

    while animal_no in no_animals or animal_no == 0:
        if animal_no == 0:
            print('Exiting menu.')
            break
        else:
            print(CURRENT_ANIMALS[animal_keys[animal_no]])
            break

elif selection == 3:

    # Display list for information
    animal_display(1)

    # Compiling keys for matching
    animal_keys = list(CURRENT_ANIMALS.keys())
    no_animals = [i for i in range(1, len(CURRENT_ANIMALS))]

    # Requesting user input
    [i for i in range(1, len(ANIMAL_MANAGEMENT))]
    animal_no = int(input('Please input the numer of the animal health records you want to retrieve or 0 to exit: '))

    while animal_no in no_animals or animal_no == 0:
        if animal_no == 0:
            print('Exiting menu.')
            break
        else:
            print(CURRENT_ANIMALS[animal_keys[animal_no]])
            break


#CURRENT_ANIMALS['A1001'].dietary_comments()
#CURRENT_ANIMALS['A1001'].health_comments()


#h_report = pickle_records.retrieve_record('A1001_health_comments')
#d_report = pickle_records.retrieve_record('A1001_dietary_comments')
#print(h_report)
#print(d_report)
"""