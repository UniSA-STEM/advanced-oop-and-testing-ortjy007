# File          : TestEnclosure.py
# Author        : Jorge Ortega
# Email id      : ortjy007@mymail.unisa.edu.au
# Description   : COMP 1048 advanced-oop-and-testing Assignment 2
#
# This is my own work as defined by the University's
# Academic Misconduct policy.

from enclosure import ZooEnc
import pytest


# As I'm unable to test the enclosure and environmental classes
# (being both abstract classes)  I will test the ZooEnclosure
# child classes which is instantiated from both of then and includes
# its own set of parameters and methods

# Running Pytest on the child class ZooEnclosure
@pytest.fixture
def valid_ZooEnc() -> ZooEnc:
    """
    ZooEnclosure created with VALID parameter inputs for testing
    :return: ZooEnclosure
    """
    return ZooEnc('Z1', 250, 'E1', True, 1,
                        '2020-01-01', True, True, True,
                        {}, True, True, True, True, 25)


# Adding values to ZooEnclosure's own methods
# ZooEnclosure.telco_contract = 'GRRRRRR'

ZooEnc('Z1', 250, 'E1', True, 1,
                        '2020-01-01', True, True, True,
                        {}, True, True, True, True, 25)

class TestZooEnclosure:

    # Testing all parameter inputs @ instance creation
    def test_rain(self, ZooEnc, capsys):
        ZooEnc.rain()
        rain = capsys.readouterr()
        assert  rain.out.strip() == 'If artificial rain is needed activate the sprinklers'

