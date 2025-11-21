# File          : TestAnimal.py
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


from animal_v9_7 import Mammal
from animal_v9_7 import Aves
import pytest

# As I'm unable to test the Animal class (being an abstract class)
# I will test two of the four child classes instantiated from it
# the mammal and the aves subclasses

# First test
# Running Pytest on the child class Aves
@pytest.fixture
def valid_mammal() -> Mammal:
    """
    mammal created with VALID parameter inputs for testing
    :return: Aves
    """
    return Mammal('Tigger', 'Panthera Tigris', 'D1', 'H1','J1', 'T0', 50,'2020-03-02','A1','R1',False,'ZooE_Z0_001')

# Adding values to Aves's own methods
Mammal.own_sound = 'GRRRRRR'
Mammal.sleeping = 'Snooozing'

# Adding values to Aves inherited methods
Mammal.suckling = '... having a nurturing breakfast...'
Mammal.actions = 'give birth to live of springs'
Mammal.behaviours = 'social bonding', 'communications through', 'vocalizations and scent', 'territorial'
Mammal.traits = 'endotherm', 'have hair or fur', 'have three middle ear bones'

@pytest.fixture
def invalid_mammal()-> Mammal:
    """
    mammal created with INVALID parameter inputs for testing
    :return: Aves
    """
    return Mammal(True, 1, 'Carnivore', '10-NOV-2024',
                  True, 'False', 21, '17')

class TestMammal:

    # Testing all parameter inputs @ instance creation
    def test_parameters(self, valid_mammal):
        assert valid_mammal.name == 'Tigger'
        assert valid_mammal.species == 'Panthera Tigris'
        assert valid_mammal.diet == 'D1'
        assert valid_mammal.health == 'H1'
        assert valid_mammal.injury == 'J1'
        assert valid_mammal.treatment == 'T0'
        assert valid_mammal.min_encl_size == 50
        assert valid_mammal.dob == '2020-03-02'
        assert valid_mammal.class_ == 'A1'
        assert valid_mammal.origin == 'R1'
        assert valid_mammal.sleeping == False
        assert valid_mammal.enclosure == 'ZooE_Z0_001'

    # Testing methods
    def test_methods(self, valid_mammal):
        assert valid_mammal.own_sound == 'GRRRRRR'
        assert valid_mammal.sleeping == 'Snooozing'
        assert valid_mammal.suckling == '... having a nurturing breakfast...'
        assert valid_mammal.actions == 'give birth to live of springs'
        assert valid_mammal.behaviours == ('social bonding',
                                           'communications through',
                                           'vocalizations and scent',
                                           'territorial')
        assert valid_mammal.traits == ('endotherm',
                                       'have hair or fur',
                                       'have three middle ear bones')


# Second test
# Running Pytest on the child class Aves
@pytest.fixture
def valid_ave() -> Aves:
    """
    ave created with VALID parameter inputs for testing
    :return: Ave
    """
    return Aves('Julius Caesar', 'Cacatua Galerita', 1, '2000-09-27',
           {}, True, True, 50)

# Adding values to Aves's own methods
Aves.own_sound = 'HIZZZZZZZZ'
Aves.sleeping = 'quiet........shhhhhh'

# Adding values to Aves inherited methods
Aves.flying = '... looking at the world from above...'
Aves.actions = 'flight', 'perching', 'preening'
Aves.behaviours = 'cooperative breeding', 'social learning', 'pair bonds', 'flocking'
Aves.traits = 'have feathers', 'beak without teeth', 'wings', 'bipedal'

@pytest.fixture
def invalid_ave()-> Aves:
    """
    mammal created with INVALID parameter inputs for testing
    :return: Ave
    """
    return Aves(True, '', 'food', 'Friday 7th June',
           {}, 'yes', 'No', -15)

class TestAve:

    # Testing all parameter inputs @ instance creation
    def test_parameters(self, valid_ave):
        assert valid_ave.name == 'Julius Caesar'
        assert valid_ave.species == 'Cacatua Galerita'
        assert valid_ave.diet == 1
        assert valid_ave.dob == '2000-09-27'
        assert valid_ave.health == {}
        assert valid_ave.injury == True
        assert valid_ave.treatment == True
        assert valid_ave.min_encl_size == 50

    # Testing methods
    def test_methods(self, valid_ave):
        assert valid_ave.own_sound == 'HIZZZZZZZZ'
        assert valid_ave.sleeping == 'quiet........shhhhhh'
        assert valid_ave.flying == '... looking at the world from above...'
        assert valid_ave.actions == ('flight', 'perching', 'preening')
        assert valid_ave.behaviours == ('cooperative breeding',
                                           'social learning',
                                           'pair bonds',
                                           'flocking')
        assert valid_ave.traits == ('have feathers',
                                       'beak without teeth',
                                       'wings',
                                       'bipedal')