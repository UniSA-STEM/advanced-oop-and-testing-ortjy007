# File          : animal_data.py
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

# Dictionary containing animal's treatment status

A_CLASS = {'A1': 'Mammalia',
          'A2': 'Aves',
          'A3': 'Reptilia',
          'A4': 'Ctenophora'
           }

SPECIES = [ 'Panthera Tigris', 'Lemur catta', 'Eulemur mongoz', 'Chamaeleo chamaeleon', 'Titanus Gojira',
            'Python bivittatus', 'Pygoscelis adeliae', 'Tentaculata', 'Nuda', 'Scleroctenophora']

# Dictionary containing animal's possible origins
ORIGIN = {'R1': 'Wild Captured',
          'R2': 'Bred Locally',
          'R3': 'Bred Elsewhere',
          'R4': 'On Loan'
           }

# Dictionary containing diets
DIET = {'D10': 'APEX Predator',
        'D1': 'Omnivore',
        'D2': 'Herbivore',
        'D3': 'Carnivore',
        'D4': 'Special (under treatment)'
        }

# Dictionary containing animal's health status
HEALTH = {'H1': 'Thriving',
          'H2': 'Healthy',
          'H3': 'Managing',
          'H4': 'Deteriorating',
          'H5': 'Requires attention',
          'H6': 'Critical',
          'HX': 'No longer required... dead!'
          }

# Dictionary containing animal's injury status
INJURY = {'J0': 'None',
          'J1': 'Life Support',
          'J2': 'Critically injured',
          'J3': 'Severely Injured',
          'J4': 'Injured',
          'J5': 'Minor Injury',
          'J6': 'Discomfort',
          }

# Dictionary containing animal's treatment status
TREATMENT = {'T0': 'None',
             'T1': 'Intensive Care',
             'T2': 'Hospitalized',
             'T3': 'Isolated',
             'T4': 'In Therapy',
             'T5': 'On Medication',
             'T6': 'Follow up',
             'T7': 'Discharged',
             'T8': 'Other'
             }
