# File          : main.py
# Author        : Jorge Ortega
# Email id      : ortjy007@mymail.unisa.edu.au
# Description   : COMP 1048 advanced-oop-and-testing Assignment 2
#
# This is my own work as defined by the University's
# Academic Misconduct policy.
#
import pickle
import print_report
import pprint
from animal import Aves
from animal import Reptilia
from animal import Mammal
from animal import Ctenophora

# Animal testing: Mammals
Tigger = Mammal('Tigger', 'Panthera Tigris', 3, '2020-03-02', {}, False, False, 2)
King_Julian = Mammal('King Julian', 'Lemur Catta', 1, '2022-06-03',{}, True, False, 1)
Marlene = Mammal('Marlene', 'Lutra Lutra', 3, '2016-11-24', {}, False,True, 4)

# Animal testing: Reptilia
Cody = Reptilia('Cody','Varanus Komodoensis', 1,'2011-02-22',{}, False, False,3)

# Animal testing: Aves
Kowalski = Aves('Kowalski','Aptenodytes patagonicus', 3, '2014-08-30',{},True,True ,1 )

# Animal testing: Ctenophora
Squshy = Ctenophora('Squshy', 'Mertensia ovum', 1, '2025-01-03', {}, False, False,1)

# Print animals
# Tigger details str
print(Tigger)
print()
print(Cody)
print()
print(Kowalski)
print()
print(Squshy)

# Tigger details str
print(King_Julian)
print()

# Tigger details str
print(Marlene)
print()

current = Mammal.MAMMAL_INVENTORY
pprint.pprint(current)

"""
# Tigger details str
print(Tigger)

# 1 Tigger Origin
print(Tigger.origin)

# Changing Tiggers origin
Tigger.origin = 1

# Confirmation of change
print(Tigger.origin)

# 2 Tigger Own Sound
print(Tigger.own_sound)

# Changing Tigger sound
Tigger.own_sound = 'boing, boing, boing'

# Confirmation of change
print(Tigger.own_sound)

# 3 Tigger Sleeping
print(Tigger.sleeping)

# Sending Tigger to bed
Tigger.sleeping = True

# Confirmation of change
print(Tigger.sleeping)
"""