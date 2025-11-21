# File          : staff_enclosure_v9_7.py
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
from staff_v9_7 import Staff


# First test
# Running Pytest on the child class ZooEnclosure
@pytest.fixture
def valid_Staff() -> Staff:
    """
    Staff created with VALID parameters inputs for testing
    :return: Staff
    """
    return Staff('Cat', 'Stevens', '1948-07-21', 'G1', 'W0', 'Q1', 'R0')


# Adding values to Staff's own methods
# Aves.sleeping = 'Snooozing'

# Adding values to Aves inherited methods
# Aves.suckling = '... having a nurturing breakfast...'

class TestStaff():

    # Testing all parameter inputs @ instance creation
    def test_parameters(self, valid_Staff):
        assert valid_Staff._name == 'Cat'
        assert valid_Staff._last_name == 'Stevens'
        assert valid_Staff.dob == '1948-07-21'
        assert valid_Staff.gender == 'G1'
        assert valid_Staff.work_r == 'W0'
        assert valid_Staff.qualifications == 'Q1'
        assert valid_Staff.salary == 'R0'
