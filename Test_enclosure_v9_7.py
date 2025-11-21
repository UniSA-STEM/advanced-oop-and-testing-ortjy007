# File          : test_enclosure_v9_7.py
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

import pytest

from Exercises.Trigger import Trigger
from enclosure_v9_7 import ZooEnclosure


# First test
# Running Pytest on the child class ZooEnclosure
@pytest.fixture
def valid_ZooEnclosure() -> ZooEnclosure:
    """
    ZooEnclosure created with VALID parameters inputs for testing
    :return: ZooEnclosure
    """
    return ZooEnclosure('Z1', 'E1', True, 1,
                        1, 250,'F0', '2020-01-01')


# Adding values to Enclosures's own methods
# ZooEnclosure.add_care_team = 'GRRRRRR'
# ZooEnclosure.remove_care_team = 'something'
# ZooEnclosure.add_animals = Trigger
# ZooEnclosure.remove_animals = Trigger
# ZooEnclosure.cleaning = 'something else'

# Adding values to ZooEnclosure inherited methods
# ZooEnclosure.checking = '... just chicken ...'

class TestZooEnclosure():

    # Testing all parameter inputs @ instance creation
    def test_parameters(self, valid_ZooEnclosure):
        assert valid_ZooEnclosure._location == 'Z1'
        assert valid_ZooEnclosure._type_ == 'E1'
        assert valid_ZooEnclosure._multi_species == True
        assert valid_ZooEnclosure._cleaning == 1
        assert valid_ZooEnclosure._area == 250
        assert valid_ZooEnclosure._features == 'F0'
        assert valid_ZooEnclosure._date_built == '2020-01-01'
