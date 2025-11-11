# File          : enclosure.py
# Author        : Jorge Ortega
# Email id      : ortjy007@mymail.unisa.edu.au
# Description   : COMP 1048 advanced-oop-and-testing Assignment 2
#
# This is my own work as defined by the University's
# Academic Misconduct policy.

from abc import ABC, abstractmethod
from datetime import date
from pos_dig_val import digit_val_float
import re
import pickle

import date_validation
import print_report
import reports
from pprint import pprint


class Enclosure(ABC):
    """
    100% StarDust: Zoo Management Software (ZMS)
    Created ByteWise Consulting.
    All rights unreserved.

    Abstract Enclosure class to be used as the parent class for the
    zoo project...
    Class attributes:
    DIET: dictionary with the 3 main diets, additional information
    allowed in the child classes.
    ANIMAL_ID: Unique sequential number for each individual animal.
    ANIMAL_INVENTORY: List of all animals created using this class.

    Attributes:
    name: str
    species: str
    diet: int = 1 (Omnivore)
    dob: str = 2020-01-01 (Default)
    age: YYYY (calculated from dod to today's date)

    Methods w/decorators (all validating input):
    +name @property getter + setter
    +species @property getter + setter
    +diet @property getter + setter
    +dob @property getter + setter

    Abstract methods:
    +health_report
    +actions
    +behaviours
    +traits
    """
    ENCLOSURE_TYPE = {'E1': 'Outdoors',
                      'E2': 'Indoors',
                      'E3': 'Aviary',
                      'E4': 'Ponds',
                      'E5': 'Aquarium',
                      'E6': 'Terrarium',
                      'E7': 'Riparium',
                      'E8': 'Paludarium',
                      'E9': 'Other'
                      }

    ZOO_ZONES = {'Z1': 'Big Green',
                 'Z2': 'The Plains',
                 'Z3': 'Whiteout',
                 'Z4': 'Low and Blue',
                 'Z5': 'Tropical',
                 'Z6': 'At Altitude',
                 'Z7': 'From Above',
                 }

    ENCLOSURE_ID = 0
    ENCLOSURE_INVENTORY = []

    def __init__(self, location: str, size_m2: float, capacity: int, type_='E1',
                 multi_species=True, date_build='2010-01-01',
                 operational=True, clean_status=True, repairs=False, max_size=1):
        self.__location = location
        self.__size_m2 = size_m2
        self.__capacity = capacity
        self.__type_ = type_
        self.__multi_species = multi_species
        self.__date_build = date_build
        self.__operational = operational
        self.__clean_status = clean_status
        self.__repairs = repairs
        self.__max_size = max_size
        self.__age = 0

        self.ENCLOSURE_ID += 1
        self.__code = self.__location + self.__type_ + str(self.ENCLOSURE_ID)

        Enclosure.ENCLOSURE_INVENTORY.append(self)
        print('100% StarDust: Zoo Management Software (ZMS).\n')

    def __str__(self) -> str:
        # Calculating age from date_build
        today = date.today()
        tmp_age = date(int(self.date_build[0:4]),
                       int(self.date_build[5:7]),
                       int(self.date_build[8:]))
        self.__age = today.year - tmp_age.year

        return (f'Code: {self.__code}\n'
                f'Location: {self.__location}\n'
                f'Size (in m2): {self.__size_m2}\n'
                f'Capacity: {self.__capacity}\n'
                f'Type: {self.__type_}\n'
                f'Multi Species: {self.__multi_species}\n'
                f'Date Build: {self.__date_build}\n'
                f'Operational: {self.__operational}\n'
                f'Clean Status: {self.__clean_status}\n'
                f'Repairs Needed: {self.__repairs}\n'
                f'Max Enclosure Size: {self.__max_size}\n'
                f'Age: {self.__age}\n'
                f'Enclosure ID: {self.ENCLOSURE_ID:02d}\n')

    def __repr__(self):
        return (f'location: {self.__location},'
                f'size_m2: {self.__size_m2}, '
                f'capacity: {self.__capacity},'
                f'type: {'E1'}, '
                f'multi_species: {True},'
                f'date_build: {'2010-01-01'},'
                f'operational: {True},'
                f'clean_status: {True},'
                f'repairs: {True}'
                f'max_size: {1}')

    @property
    def location(self) -> str:
        """location property"""
        return self.__location

    @location.setter
    def location(self, location: str) -> None:
        """
        Setter for validating the location of the enclosure as per
        current ZOO_ZONES dictionary
        :param location: str
        :return: None
        """

        # Printing locations to assist user selection
        print('The current valid Zoo Zones for location are:')
        for key, value in Enclosure.ZOO_ZONES.items():
            print(f'{key}:{value}')

        # Input validation using while loop
        while location not in Enclosure.ZOO_ZONES:
            try:
                location = input(f'Please enter a valid input.\n'
                                 f'Input needs to match a Zoo Zone: ')
                self.__location = location

            except ValueError:
                print("Invalid input. Please enter a valid location.\n")

    @property
    def size_m2(self) -> float:
        """size_m2 property"""
        return self.__size_m2

    @size_m2.setter
    def size_m2(self, size_m2: float, animal= None) -> None:
        """
        Validating the size of the enclosure to float with 2 decimal points.
        :param size_m2: float
        :return: None
        """
        val_size_m2 = digit_val_float(size_m2)
        valid = True

        while valid:

            # If animal input is provided
            if animal:

                # Required area per animal according to their file
                area_per_animal = animal.min_encl_size
                print(f'{animal.name} require {area_per_animal}m2 per individual.')

                # Calculating the animal density
                density = int(val_size_m2 / area_per_animal)

                # Validating input
                if density > 1:
                    print(f'The {size_m2} enclosure will take a maximum '
                          f'population of {density} {animal}(s).\n'
                          f'Enclosure size saved.')
                    self.__capacity = density
                    self.__size_m2 = val_size_m2
                    break

                elif density < 1:
                    print(f'The enclosure is to small for this animal,'
                          f'please increase the enclosure size and try'
                          f' again.')
                    valid = True

            # if no animal input is provided
            if not animal:

                if val_size_m2 <= self.__max_size:
                    print('Enclosure size saved.')
                    self.__size_m2 = val_size_m2
                    break

                elif val_size_m2 > self.__max_size:
                    val_size_m2 = digit_val_float(input('The proposed enclosure'
                        f'size exceeds the maximum \nsize of {self.__max_size} '
                        f'please decrease the size of the enclosure: '))
                    valid = True

    @property
    def type_(self) -> str:
        """type property"""
        return self.__type_

    @type_.setter
    def type_(self, type_: str) -> None:
        """
        Setter for validating the type of the enclosure as per
        current ENCLOSURE_TYPE dictionary
        :param type: str
        :return: None
        """

        # Printing locations to assist user selection
        print('The current valid Enclosure Types are:')
        for key, value in Enclosure.ENCLOSURE_TYPE.items():
            print(f'{key}:{value}')

        # Input validation using while loop
        while type_ not in Enclosure.ENCLOSURE_TYPE:
            try:
                type_ = input(f'Please enter a valid input.\n'
                                 f'Input needs to match an Enclosure Type: ')
                self.__type_ = type_

            except ValueError:
                print("Invalid input. Please enter a Enclosure Type.\n")

    @property
    def multi_species(self) -> bool:
        """multi_species property"""
        return self.__multi_species

    @multi_species.setter
    def multi_species(self, multi_species: bool) -> None:
        """
        Setter for the multi_species parameter
        :param multi_species: bool
        :return: None
        """
        # Simple boolean operation to invert value
        if not multi_species:
            self.__multi_species = True
        else:
            self.__multi_species = False

    @property
    def date_build(self) -> str:
        """date_build property"""
        return self.__date_build

    @date_build.setter
    def date_build(self, date_build: str) -> None:
        """
        setter for dob validated though the date_validation module
        :param date_build: str
        :return: None
        """
        # Creating sets to compare dob against numbers 0-9 and'-'
        set1 = '0123456789-'

        # Validating numbers and format
        while True:
            if set(date_build).issubset(set(set1)) and len(date_build) == 10:
                dob_split = date_build.split('-')
                dob_split_int = []
                for item in dob_split:
                    dob_split_int.append(item)
                # Validation date including no futures (not allowed).
                if (len(str(dob_split_int[0])) == 4
                        and len(str(dob_split_int[1])) == 2
                        and len(str(dob_split_int[2])) == 2):
                    # Validation date including no futures (not allowed).
                    self.__date_build = date_validation.validate_dob(int(dob_split_int[0]),
                                                                     int(dob_split_int[1]),
                                                                     int(dob_split_int[2]))
                    break
            else:
                date_build = input('Please input a valid date in the DD-MM-YYYY format: ')
        self.__age = self.__date_build - date.today()

    @property
    def operational(self) -> bool:
        """operational property"""
        return self.__operational

    @operational.setter
    def operational(self, operational: bool) -> None:
        """
        Setter for the operational parameter
        :param operational: bool
        :return: None
        """
        # Simple boolean operation to invert value
        if not operational:
            self.__operational = True
        else:
            self.__operational = False

    @property
    def clean_status(self) -> bool:
        """clean_status property"""
        return self.__clean_status

    @clean_status.setter
    def clean_status(self, clean_status: bool) -> None:
        """
        Setter for the clean_status parameter
        :param clean_status: bool
        :return: None
        """
        # Simple boolean operation to invert value
        if not clean_status:
            self.__clean_status = True
        else:
            self.__clean_status = False

    @property
    def repairs(self) -> bool:
        """repairs_needed property"""
        return self.__repairs

    @repairs.setter
    def repairs(self, repairs: bool) -> None:
        """
        Setter for the repairs parameter
        :param repairs: bool
        :return: None
        """
        # Simple boolean operation to invert value
        if not repairs:
            self.__repairs = True
        else:
            self.__repairs = False

    @abstractmethod
    def clean_regime(self):
        """
        Enclosure cleaning regime
        """
        pass

    @abstractmethod
    def maintenance_regime(self):
        """
        Enclosure maintenance regime
        """
        pass
