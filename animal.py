# File          : animal.py
# Author        : Jorge Ortega
# Email id      : ortjy007@mymail.unisa.edu.au
# Description   : COMP 1048 advanced-oop-and-testing Assignment 2
#
# This is my own work as defined by the University's
# Academic Misconduct policy.
#
from abc import ABC, abstractmethod
from datetime import datetime
import re

class Animal(ABC):

    DIET = {1:'Omnivore',
            2:'Herbivore',
            3:'Carnivore'}
    ANIMAL_ID = 0

    def __init__(self, name: str, species: str, dob: str, diet: int):
        self.__name = name
        self.__species = species
        self.__dob = dob
        self.__diet = diet
        self.ANIMAL_ID += 1

    def __str__(self):
        pass

    def __repr__(self):
        pass

    @property
    def name(self) -> str:
        """Name property"""
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        if isinstance(name, str) and (name == re.search(r'[a-zA-Z]', name)):
            print(f'{name} name created.')
            self.__name = name
        else:
            print('Invalid input, the name can only contain English alphabet letters.\n'
                  'Temporary (Animal with Animal ID number) name used.')
            self.__name = 'Animal' + str(self.ANIMAL_ID)

    @property
    def species(self) -> str:
        """Species property"""
        return self.__species

    @species.setter
    def species(self, species: str) -> None:
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
        self.__dob = dob

    @property
    def diet(self) -> str:
        """dietary_needs property"""
        return self.__diet

    @diet.setter
    def diet(self, diet: str) -> None:
        self.__diet = diet
