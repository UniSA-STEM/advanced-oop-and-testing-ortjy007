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
from pos_dig_val import digit_val_int
from pos_dig_val import str_YN_val_uc
from animal import Mammal
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
    ENCLOSURE-TYPE: dictionary with the 9 main types of enclosures
    available
    ZOO_ZONES: Zones a per current Zoo Facilities.
    ENCLOSURE_ID: Unique sequential number for each individual Enclosure.
    ENCLOSURE_INVENTORY: List of all enclosures created using this class.
    MAX_SIZE: Maximum enclosure size

    Attributes (self-explanatory):
    -location: str
    -size_m2: float
    -capacity: int
    -type: str
    -multi_species: bool
    -date_build: str
    -operational: bool
    -clean_status: bool
    -repairs: bool
    -inhabitants: animal
    -age: int (calculated from dod to today's date)

    Methods w/decorators (all validating input):
    +location @property getter + setter
    +size_m2 @property getter + setter
    +capacity @property getter + setter
    +type_ @property getter + setter
    +multi_species @property getter + setter
    +date_build @property getter + setter
    +operational @property getter + setter
    +clean_status @property getter + setter
    +repairs @property getter + setter

    Abstract methods:
    +clean_regime
    +maintenance_regime

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

    # Valid input for location:
    ZOO_ZONES = {'Z1': 'Big Green',
                 'Z2': 'The Plains',
                 'Z3': 'Whiteout',
                 'Z4': 'Low and Blue',
                 'Z5': 'Tropical',
                 'Z6': 'At Altitude',
                 'Z7': 'From Above',
                 }

    # Maximum Enclosure Size
    MAX_SIZE = 2000

    ENCLOSURE_ID = 0
    ENCLOSURE_INVENTORY = []

    def __init__(self, location: str, size_m2: float, capacity= 0, type_='E1',
                 multi_species=True, date_build='2010-01-01',
                 operational=True, clean_status=True, repairs=False):
        self.__location = location
        self.__size_m2 = size_m2
        self.__capacity = capacity
        self.__type_ = type_
        self.__multi_species = multi_species
        self.__date_build = date_build
        self.__operational = operational
        self.__clean_status = clean_status
        self.__repairs = repairs
        self.__inhabitants = {}
        self.__age = 0

        self.ENCLOSURE_ID += 1
        self.__code = self.__location + '.' + self.__type_ + '.' + str(f'{self.ENCLOSURE_ID:03d}')

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
                f'Size (m2): {self.__size_m2}\n'
                f'Inhabitants: {self.__inhabitants}\n'
                f'Capacity: {self.__capacity}\n'
                f'Type: {self.__type_}\n'
                f'Multi Species: {self.__multi_species}\n'
                f'Date Build: {self.__date_build}\n'
                f'Operational: {self.__operational}\n'
                f'Clean Status: {self.__clean_status}\n'
                f'Repairs Needed: {self.__repairs}\n'
                f'Max Enclosure Size: {Enclosure.MAX_SIZE}\n'
                f'Age: {self.__age}\n'
                f'Enclosure ID: {self.ENCLOSURE_ID:03d}\n'
                )

    def __repr__(self) -> str:
        return (f'location= {self.__location}, '
                f'size_m2= {self.__size_m2}, '
                f'Inhabitants= {self.__inhabitants}, '
                f'capacity= {self.__capacity}, '
                f'type= {'E1'}, '
                f'multi_species= {True}, '
                f'date_build= {'2010-01-01'}, '
                f'operational= {True}, '
                f'clean_status= {True}, '
                f'repairs= {True}, '
                f'max_size= {1}'
                )

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
    def size_m2(self, size_m2: float) -> None:
        """
        Validating the size of the enclosure to float with 2 decimal points.
        :param size_m2: float
        :return: None
        """
        val_size_m2 = digit_val_float(size_m2)
        valid = True

        # while loop to validate user input
        while valid:

            # Is the input is larger that maximum size
            if val_size_m2 <= Enclosure.MAX_SIZE:
                print('Enclosure size saved.')
                self.__size_m2 = val_size_m2
                break

            elif val_size_m2 > Enclosure.MAX_SIZE:
                val_size_m2 = digit_val_float(input('The proposed enclosure'
                        f'size exceeds the maximum \nsize of {self.MAX_SIZE} '
                        f'please decrease the size of the enclosure: '))
                valid = True

    @property
    def capacity(self) -> int:
        """
        Capacity property
        :return:
        """
        return self.__capacity

    @capacity.setter
    def capacity(self, value) -> None:

        # Reset capacity
        self.__capacity = 0

        # Local working area valuables
        working_size = self.__size_m2
        remaining_area = 0
        resident = None
        species_list = []
        add_ = 'Y'


        # Or any other animal, this is only to have access to the
        # concrete class inventory list
        animal = Tigger

        # User information regarding the available species
        print(f'The following animals are currently in the inventory: ')

        for animal in animal.MAMMAL_INVENTORY:
            species_list.append(animal.species)
            print(f'{animal.species}, recommended area per individual(m2): {animal.min_encl_size}')


        while add_ == 'Y':

            # Animal validation selection
            while resident not in species_list:
                print(f'Note: Only animals in the current inventory can be '
                      f'considered. ')

                # What species is this enclosure for?
                resident = input(f'\nPlease select the species '
                                 f'to accommodate: ')

            else:

                # Area per individual for the selected species
                m2_resident = digit_val_float(input('Please input the area per '
                                                  'animal you want to provide: '))

                # Calculating max density
                max_density = int(working_size // m2_resident)

                print(f'With {m2_resident}m2 per {resident} we can accommodate '
                      f'{max_density} {resident}/s.')

                # Requesting the expected number of individuals in the enclosure
                resident_count = digit_val_int(input(f'Please provide the number '
                            f'of {resident}s you want in this enclosure '
                            f'({max_density}max): '))

                if resident_count > max_density:

                    remaining_area = working_size - (max_density * m2_resident)
                    print(f'The maximum number of {resident}s is {max_density}.'
                          f'Maximum number used.\n'
                          f'{remaining_area}m2 remain to be allocated.\n')

                elif resident_count < max_density:
                    remaining_area = working_size - (resident_count * m2_resident)
                    print(f'{resident_count} {resident}s can be allocated to this enclosure.\n'
                          f'{remaining_area}m2 remain to be allocated.')

                if self.__multi_species:
                    add_ = str_YN_val_uc(input(f'This is a multi-species enclosure.\n'
                                               f'Do you want to add another species? (Y/N):'))

        print('Exiting application')


    @property
    def type_(self) -> str:
        """type property"""
        return self.__type_

    @type_.setter
    def type_(self, type_: str) -> None:
        """
        Setter for validating the type of the enclosure as per
        current ENCLOSURE_TYPE dictionary
        :param type_: str
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

class Environment(ABC):
    """
    100% StarDust: Zoo Management Software (ZMS)
    Created ByteWise Consulting.
    All rights unreserved.

    Abstract Environment class to be used as the parent class for the
    zoo project...
    Class attributes:
    ENCLOSURE-TYPE: dictionary with the 9 main types of enclosures
    available
    ZOO_ZONES: Zones a per current Zoo Facilities.
    ENCLOSURE_ID: Unique sequential number for each individual Enclosure.
    ENCLOSURE_INVENTORY: List of all enclosures created using this class.
    MAX_SIZE: Maximum enclosure size

    Attributes (self-explanatory):
    -location: str
    -size_m2: float
    -capacity: int
    -type: str
    -multi_species: bool
    -date_build: str
    -operational: bool
    -clean_status: bool
    -repairs: bool
    -inhabitants: animal
    -age: int (calculated from dod to today's date)

    Methods w/decorators (all validating input):
    +location @property getter + setter
    +size_m2 @property getter + setter
    +capacity @property getter + setter
    +type_ @property getter + setter
    +multi_species @property getter + setter
    +date_build @property getter + setter
    +operational @property getter + setter
    +clean_status @property getter + setter
    +repairs @property getter + setter

    Abstract methods:
    +clean_regime
    +maintenance_regime

    """
    # Valid input for Environment:
    ENVIRONMENT_TYPE = {'A': 'Tropical',
                        'B': 'Arid',
                        'C': 'Temperate',
                        'D': 'Continental',
                        'E': 'Polar',
                        'Z': 'Other'
                        }

    # Valid input for Vegetation:
    VEGETATION_TYPE = { 'V1': 'Forest',
                        'V2': 'Grassland',
                        'V3': 'Savanna',
                        'V4': 'Tundra',
                        'V5': 'Desert',
                        'V6': 'Ice Sheet',
                        'V7': 'Aquatic',
                        }

    WATER_BODY_TYPE = { 'B1': 'Estuary',
                        'B2': 'Lake',
                        'B3': 'Wetlands',
                        'B4': 'Lake',
                        'B5': 'Pond',
                        'B6': 'Glacier',
                        'B7': 'Delta',
                        'B8': 'River',
                        'B9': 'Ocean'
                      }

    WATER_TYPE = { 'W1': 'Seawater',
                   'W2': 'Freshwater'
                 }

    def __init__(self, env_type: str, vegetation: str, water_body= True,
                 water_type= str, art_rain= True, heated= False, uv_if=False):
        self.__env_type = env_type
        self.__vegetation = vegetation
        self.__water_body = water_body
        self.__water_type = water_type
        self.__art_rain = art_rain
        self.__heated = heated
        self.__uv_if = uv_if
        print('100% StarDust: Zoo Management Software (ZMS).\n')

    def __str__(self) -> str:

        return (f'Environment: {self.__env_type}\n'
                f'Vegetation: {self.__vegetation}\n'
                f'Water Body: {self.__water_body}\n'
                f'Water Type: {self.__water_type}\n'
                f'Artificial Rain: {self.__art_rain}\n'
                f'Heated: {self.__heated}\n'
                f'UV or IF lights: {self.__uv_if}\n'
                )

    def __repr__(self) -> str:
        return (f'env_type= {'C'}, '
                f'vegetation= {'V1'}, '
                f'water_body= {'B5'}, '
                f'water_type= {'W2'}, '
                f'art_rain= {True}, '
                f'heated= {False}, '
                f'uv_if= {False}'
                )

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
    def size_m2(self, size_m2: float) -> None:
        """
        Validating the size of the enclosure to float with 2 decimal points.
        :param size_m2: float
        :return: None
        """
        val_size_m2 = digit_val_float(size_m2)
        valid = True

        # while loop to validate user input
        while valid:

            # Is the input is larger that maximum size
            if val_size_m2 <= Enclosure.MAX_SIZE:
                print('Enclosure size saved.')
                self.__size_m2 = val_size_m2
                break

            elif val_size_m2 > Enclosure.MAX_SIZE:
                val_size_m2 = digit_val_float(input('The proposed enclosure'
                        f'size exceeds the maximum \nsize of {self.MAX_SIZE} '
                        f'please decrease the size of the enclosure: '))
                valid = True

    @property
    def capacity(self) -> int:
        """
        Capacity property
        :return:
        """
        return self.__capacity

    @capacity.setter
    def capacity(self, value) -> None:

        # Reset capacity
        self.__capacity = 0

        # Local working area valuables
        working_size = self.__size_m2
        remaining_area = 0
        resident = None
        species_list = []
        add_ = 'Y'


        # Or any other animal, this is only to have access to the
        # concrete class inventory list
        animal = Tigger

        # User information regarding the available species
        print(f'The following animals are currently in the inventory: ')

        for animal in animal.MAMMAL_INVENTORY:
            species_list.append(animal.species)
            print(f'{animal.species}, recommended area per individual(m2): {animal.min_encl_size}')


        while add_ == 'Y':

            # Animal validation selection
            while resident not in species_list:
                print(f'Note: Only animals in the current inventory can be '
                      f'considered. ')

                # What species is this enclosure for?
                resident = input(f'\nPlease select the species '
                                 f'to accommodate: ')

            else:

                # Area per individual for the selected species
                m2_resident = digit_val_float(input('Please input the area per '
                                                  'animal you want to provide: '))

                # Calculating max density
                max_density = int(working_size // m2_resident)

                print(f'With {m2_resident}m2 per {resident} we can accommodate '
                      f'{max_density} {resident}/s.')

                # Requesting the expected number of individuals in the enclosure
                resident_count = digit_val_int(input(f'Please provide the number '
                            f'of {resident}s you want in this enclosure '
                            f'({max_density}max): '))

                if resident_count > max_density:

                    remaining_area = working_size - (max_density * m2_resident)
                    print(f'The maximum number of {resident}s is {max_density}.'
                          f'Maximum number used.\n'
                          f'{remaining_area}m2 remain to be allocated.\n')

                elif resident_count < max_density:
                    remaining_area = working_size - (resident_count * m2_resident)
                    print(f'{resident_count} {resident}s can be allocated to this enclosure.\n'
                          f'{remaining_area}m2 remain to be allocated.')

                if self.__multi_species:
                    add_ = str_YN_val_uc(input(f'This is a multi-species enclosure.\n'
                                               f'Do you want to add another species? (Y/N):'))

        print('Exiting application')


    @property
    def type_(self) -> str:
        """type property"""
        return self.__type_

    @type_.setter
    def type_(self, type_: str) -> None:
        """
        Setter for validating the type of the enclosure as per
        current ENCLOSURE_TYPE dictionary
        :param type_: str
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

class ZooEnclosure(Enclosure):

    def __init__(self, location, size_m2, capacity, type_, multi_species,
                 date_build, operational, clean_status, repairs):
        super().__init__(location, size_m2, capacity, type_, multi_species,
                         date_build, operational, clean_status, repairs)

    def __str__(self) -> str:
        # Calculating age from date_build
        today = date.today()
        tmp_age = date(int(self.date_build[0:4]),
                       int(self.date_build[5:7]),
                       int(self.date_build[8:]))
        self.__age = today.year - tmp_age.year

        return f'{super().__str__()}'

    def __repr__(self) -> str:
        return (f'location: {self.location}, '
                f'size_m2: {self.size_m2}, '
                f'capacity: {self.capacity}, '
                f'type: {'E1'}, '
                f'multi_species: {True}, '
                f'date_build: {'2010-01-01'}, '
                f'operational: {True}, '
                f'clean_status: {True}, '
                f'repairs: {True},'
                f'Inhabitants: {None}'
                )

    def clean_regime(self):
        """
        Enclosure cleaning regime
        """
        pass


    def maintenance_regime(self):
        """
        Enclosure maintenance regime
        """
        pass
