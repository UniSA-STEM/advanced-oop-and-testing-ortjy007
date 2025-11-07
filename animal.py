# File          : animal.py
# Author        : Jorge Ortega
# Email id      : ortjy007@mymail.unisa.edu.au
# Description   : COMP 1048 advanced-oop-and-testing Assignment 2
#
# This is my own work as defined by the University's
# Academic Misconduct policy.
#
from abc import ABC, abstractmethod
from datetime import datetime, date
import re
import date_validation


class Animal(ABC):
    """
    Abstract Animal class to be used as the parent class for the
    zoo project..
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
    +actions
    +behaviours
    +traits
    """
    DIET = {1: 'Omnivore',
            2: 'Herbivore',
            3: 'Carnivore'}
    ANIMAL_ID = 0
    ANIMAL_INVENTORY = []

    def __init__(self, name: str, species: str, diet=1, dob='2020-01-01'):
        self.__name = name
        self.__species = species
        self.__dob = dob
        self.__diet = diet
        self.__age = 0
        self.ANIMAL_ID += 1
        Animal.ANIMAL_INVENTORY.append(self)
        print('Created ByteWise Consulting, all rights unreserved :).')

    def __str__(self) -> str:
        # Calculating age from DoB
        today = date.today()
        tmp_age = date(int(self.__dob[0:4]), int(self.__dob[5:7]), int(self.__dob[8:]))
        self.__age = today.year - tmp_age.year

        return (f'Name:{self.__name}\n'
                f'Species: \x1B[3m{self.__species}\x1B[0m\n'
                f'Diet: {Animal.DIET[self.__diet]}\n'
                f'DoB: {self.__dob}\n'
                f'Age: {self.__age}\n'
                f'Animal ID: {self.ANIMAL_ID:04d}\n')

    def __repr__(self):
        return f'Animal(name= {self.__name}, species= {self.__species}, diet= {1}, dob= {'2020-01-01'})'

    @property
    def name(self) -> str:
        """Name property"""
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        """
        Validating name input to a-z letters only.
        :param name: str
        :return: None
        """
        # Name validation using while loop
        while True:
            if isinstance(name, str) and name.isalpha():
                print(f'{name} name created.')
                self.__name = name
                break
            else:
                name = input('Invalid input. Please try again using only letters: ')

    @property
    def species(self) -> str:
        """Species property"""
        return self.__species

    @species.setter
    def species(self, species: str) -> None:
        """
        Validating species input to a-z letters only and in italics.
        :param species: str
        :return: None
        """
        if isinstance(species, str) and (species == re.search(r'[a-zA-Z]', species)):
            print(f'{species} name created.')
            self.__species = species
        else:
            print(f'Invalid input, the name can only contain English alphabet letters.\n'
                  f'Temporary (\x1B[3m{species}\x1B[0m with Animal ID number) name used.')
            self.__species = f'\x1B[3mSpecies\x1B[0m' + str(self.ANIMAL_ID)

    @property
    def dob(self) -> str:
        """dob property"""
        return self.__dob

    @dob.setter
    def dob(self, dob: str) -> None:
        """
        setter for dob validated though the date_validation module
        :param dob: str
        :return: None
        """
        # Creating sets to compare dob against numbers 0-9 and'-'
        set1 = '0123456789-'

        # Validating numbers and format
        while True:
            if set(dob).issubset(set(set1)) and len(dob) == 10:
                dob_split = dob.split('-')
                dob_split_int = []
                for item in dob_split:
                    dob_split_int.append(item)
                # Validation date including no futures (not allowed).
                if (len(str(dob_split_int[0])) == 4
                        and len(str(dob_split_int[1])) == 2
                        and len(str(dob_split_int[2])) == 2):
                    # Validation date including no futures (not allowed).
                    self.__dob = date_validation.validate_dob(int(dob_split_int[0]),
                                                              int(dob_split_int[1]),
                                                              int(dob_split_int[2]))
                    break
            else:
                dob = input('Please input a valid date in the DD-MM-YYYY format: ')
        self.__age = self.__dob - date.today()

    @property
    def diet(self) -> str:
        """diet property"""
        return self.__diet

    @diet.setter
    def diet(self, diet: int) -> None:
        """
        Setter for validating the primary diet as per current ANIMAL.DIET dictionary
        :param diet: int
        :return: None
        """
        # Identifying the number of diets
        no_diets = len(Animal.DIET)

        # Printing diets to assist user selection
        for key, value in Animal.DIET.items():
            print(f'{key}:{value}')

        # Input validation using while loop
        while True:
            try:
                if diet == 0:
                    diet = input(f'Please enter a valid input.\n'
                                 f'Input needs to be between 1 and {no_diets}: ')
                diet = int(diet)
                if 1 <= diet <= no_diets:
                    print(f"{self.name}'s diet has been changed to {Animal.DIET[diet]}\n")
                    self.__diet = diet
                    # If successful, exit
                    break
                else:
                    diet = input(f'Please enter a valid input.\n'
                                 f'Input needs to be between 1 and {no_diets}: ')
            except ValueError:
                print("Invalid input. Please enter a valid number.\n")
                diet = input(f'Input needs to be between 1 and {no_diets}: ')

    @abstractmethod
    def actions(self):
        pass

    @abstractmethod
    def behaviours(self):
        pass

    @abstractmethod
    def traits(self):
        pass