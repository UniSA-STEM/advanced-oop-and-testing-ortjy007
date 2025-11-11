# File          : animal.py
# Author        : Jorge Ortega
# Email id      : ortjy007@mymail.unisa.edu.au
# Description   : COMP 1048 advanced-oop-and-testing Assignment 2
#
# This is my own work as defined by the University's
# Academic Misconduct policy.
#
from abc import ABC, abstractmethod
from datetime import date
import re
import pickle

import date_validation
import print_report
import reports
import pos_dig_val
from pprint import pprint


class Animal(ABC):
    """
    100% StarDust: Zoo Management Software (ZMS)
    Created ByteWise Consulting.
    All rights unreserved.

    Abstract Animal class to be used as the parent class for the
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
    health: bool
    injury: bool
    treatment: bool

    Methods w/decorators (all validating input):
    +name @property getter + setter
    +species @property getter + setter
    +dob @property getter + setter
    +diet @property getter + setter
    +health @property getter + setter
    +injury @property getter + setter
    +treatment @property getter + setter

    Abstract methods:
    +health_comments
    +actions
    +behaviours
    +traits

    External modules used (purposedly created):
    +date_validation

    """
    DIET = {1: 'Omnivore',
            2: 'Herbivore',
            3: 'Carnivore'
            }
    ANIMAL_ID = 0
    ANIMAL_INVENTORY = []

    def __init__(self, name: str, species: str, diet=1, dob='2020-01-01',
                 health=True, injury=False, treatment=False, min_encl_size=0):
        self.__name = name
        self.__species = species
        self.__dob = dob
        self.__diet = diet
        self.__health = health
        self.__injury = injury
        self.__treatment = treatment
        self.__min_encl_size = min_encl_size
        self.__age = 0

        self.ANIMAL_ID += 1
        Animal.ANIMAL_INVENTORY.append(self)
        print('100% StarDust: Zoo Management Software (ZMS).\n')

    def __str__(self) -> str:
        # Calculating age from DoB
        today = date.today()
        tmp_age = date(int(self.__dob[0:4]),
                       int(self.__dob[5:7]),
                       int(self.__dob[8:]))
        self.__age = today.year - tmp_age.year

        return (f'Name: {self.__name}\n'
                f'Species: \x1B[3m{self.__species}\x1B[0m\n'
                f'Diet: {Animal.DIET[self.__diet]}\n'
                f'Health: {self.__health}\n'
                f'Injuries: {self.__injury}\n'
                f'In Treatment: {self.__treatment}\n'
                f'DoB: {self.__dob}\n'
                f'Age: {self.__age}\n'
                f'Animal ID: {self.ANIMAL_ID:04d}\n')

    def __repr__(self):
        return (f'Animal(name= {self.__name}, species= {self.__species}, '
                f'diet= {1}, dob= {'2020-01-01'}, health= {True}, injury= {False}, treatment= {False})')

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

    @property
    def health(self) -> bool:
        """health property"""
        return self.__health

    @health.setter
    def health(self, health: bool) -> None:
        # Simple boolean operation to invert value
        if not health:
            self.__health = True
        else:
            self.__health = False

    @property
    def injury(self) -> bool:
        """injury property"""
        return self.__injury

    @injury.setter
    def injury(self, injury: bool) -> None:
        # Simple boolean operation to invert value
        if not injury:
            self.__injury = True
        else:
            self.__injury = False

    @property
    def treatment(self) -> bool:
        """treatment property"""
        return self.__treatment

    @treatment.setter
    def treatment(self, treatment: bool) -> None:

        # Simple boolean operation to invert value
        if not treatment:
            self.__treatment = True
        else:
            self.__treatment = False


    @property
    def min_encl_size(self) -> float:
        """min_encl_size property"""
        return self.__min_encl_size

    @min_encl_size.setter
    def min_encl_size(self, min_encl_size: float) -> None:
        self.__min_encl_size = pos_dig_val.digit_val_float(min_encl_size)

    @abstractmethod
    def health_comments(self):
        pass

    @abstractmethod
    def actions(self):
        pass

    @abstractmethod
    def behaviours(self):
        pass

    @abstractmethod
    def traits(self):
        pass


class Mammal(Animal):
    """"
    Concrete Class Mammal, child class of Animal containing Vertebrae
    Mammalians. Around 6,640 documented species.

    Class Attributes:
    CLASS: Mammalia
    ORIGIN: dictionary with the 4 possible origins.
    MAMMAL_ID: Unique sequential number for each individual mammal.
    MAMMAL_INVENTORY: List of all mammals created using this class.

    Attributes:
    As inherited from Animal Class plus:
    +Origin: int

    Methods:
    As inherited from Animal Class plus:
    +print_dietary_comments
    +print_health report

    Static Method:
    Particular to Mammals:
    +Suckling


    External modules used (purposedly created):
    +date_validation
    +reports
    +print_reports
    """
    CLASS = 'Mammalia'
    ORIGIN = {1: 'Wild Captured',
              2: 'Bred Locally',
              3: 'Bred Elsewhere',
              4: 'On loan'}
    MAMMAL_ID = 0
    MAMMAL_INVENTORY = []

    def __init__(self, name, species, diet, dob, health, injury, treatment,
                 min_encl_size,origin=2, sleep=False):
        super().__init__(name, species, diet, dob, health, injury, treatment,
                         min_encl_size)
        self.__class_ = Mammal.CLASS
        self.__origin = origin
        self.__dietary_comments = {}
        self.__health_comments = {}
        self.__actions = []
        self.__behaviours = []
        self.__traits = []
        self.__own_sound = ''
        self.__sleep = sleep

        self.MAMMAL_ID += 1
        Mammal.MAMMAL_INVENTORY.append(self)

    def __str__(self) -> str:
        return (f'Class: {Mammal.CLASS}\n'
                f'{super().__str__()}'
                f'Mammal ID: {self.MAMMAL_ID:04d}\n'
                f'Origin: {Mammal.ORIGIN[int(self.__origin)]}')

    def __repr__(self):
        return (f'Mammal(name= {self.name},'
                f'species= {self.species},'
                f'diet= {1},'
                f'dob= {'2020-01-01'},'
                f'health = {2},'
                f'injury = {False},'
                f'treatment = {True},'
                f'origin= {2})'
                f'sleep= {False}'
                )

    @property
    def origin(self) -> int:
        """Origin property"""
        return self.__origin

    @origin.setter
    def origin(self, origin: int) -> None:
        """
        Validating origin input as per origin list.
        :param origin: int
        :return: None
        """

        # Identifying the number of origins
        no_origins = len(Mammal.ORIGIN)
        print()

        # Printing origin dictionary to assist user selection
        for key, value in Mammal.ORIGIN.items():
            print(f'{key}:{value}')

        # Input validation using while loop and try/except forms
        while True:
            try:
                if origin == 0 or origin == '' or type(origin) == True:
                    origin = input(f'Please enter a valid input.\n'
                                   f'Input needs to be between 1 and '
                                   f'{no_origins}: ')
                origin = int(origin)
                if 1 <= origin <= no_origins:
                    print(f"{self.name}'s origin has been changed "
                          f"to {Mammal.ORIGIN[origin]}\n")
                    self.__origin = origin
                    # If successful, exit
                    break
                else:
                    origin = input(f'Please enter a valid input.\n'
                                   f'Input needs to be between 1 and '
                                   f'{no_origins}: ')
            except ValueError:
                print(f"Error.\nOnly integers between 1 and {no_origins} "
                      f"are valid.")
                origin = input('Please try again: ')

    @property
    def own_sound(self) -> str:
        """Own sound property"""
        return self.__own_sound

    @own_sound.setter
    def own_sound(self, sound: str) -> None:
        """
        Mammal's own sound
        :param sound: str
        :return: None
        """
        self.__own_sound = sound

    @property
    def sleeping(self) -> bool:
        """Sleeping property"""
        return self.__sleep

    @sleeping.setter
    def sleeping(self, value) -> None:
        """
        Mammal's sleeping status
        :return: None
        """
        if value:
            print(f'{self.name} is awake\n'
                  f'{self.__own_sound}')
        else:
            print(f'{self.name} is asleep\n'
                  f'zzzzzzzz')
        self.__sleep = value

    def dietary_comments(self):
        """
        Dietary requirements
        A copy of the file as a dictionary is saved externally
        :return: None
        """
        self.__dietary_comments = reports.basic_report('Dietary Requirements',
                                                       self.name,
                                                       {})
        # Writing an external file for reference
        file_name = f'{self.name}_dietary_comments'
        with open(file_name, 'wb') as f:
            pickle.dump(self.__dietary_comments, f)

    def print_dietary_comments(self) -> None:
        """
        Printing dietary comments on file
        :return: None
        """
        print(f"{self.name}'s dietary requirement:")
        print_report.print_b(self.__dietary_comments)

    def health_comments(self) -> None:
        """
        Health requirements
        :return: None
        """
        health_format = reports.formats_available(3)
        self.__health_comments = reports.extended_report(self.name, 3,
                                                         'health report')

        # Writing an external file for reference
        file_name = f'{self.name}_health_report'
        with open(file_name, 'wb') as f:
            pickle.dump(self.__health_comments, f)

    def print_health_report(self) -> None:
        """
        Printing health report comments on file
        :return: None
        """
        print(f"{self.name}'s health report:")
        print_report.print_b(self.__health_comments)

    @staticmethod
    def suckling() -> None:
        """
        Mammals particularity
        :return: None
        """
        print('... having a nurturing breakfast...')

    def actions(self):
        """
        Mammal actions
        """
        self.__actions = ['give birth to live of springs']
        print(f'{self.__actions}')

    def behaviours(self):
        """
        Mammal behaviours
        """
        self.__behaviours = ['social bonding', 'communications through '
                                               'vocalizations and scent', 'territorial']
        print(f'{self.__behaviours}')

    def traits(self):
        """
        Mammal traits
        """
        self.__traits = ['endoterm', 'have hair or fur',
                         'have three middle ear bones']
        print(f'{self.__traits}')


class Aves(Animal):
    """"
    Concrete Class Aves, child class of Animal containing warm-blooded
    theropod dinosaurs commonly called Birds. Around 11,000 documented species.

    Class Attributes:
    CLASS: Aves
    ORIGIN: dictionary with the 4 possible origins.
    AVES_ID: Unique sequential number for each individual birds.
    AVES_INVENTORY: List of all birds created using this class.

    Attributes:
    As inherited from Animal Class plus:
    +Origin: int

    Methods:
    As inherited from Animal Class plus:
    +print_dietary_comments
    +print_health report

    Static Method:
    Particular to Aves:
    +Flying

    External modules used (purposedly created):
    +date_validation
    +reports
    +print_reports
    """
    CLASS = 'Aves'
    ORIGIN = {1: 'Wild Captured',
              2: 'Bred Locally',
              3: 'Bred Elsewhere',
              4: 'On loan'}
    AVES_ID = 0
    AVES_INVENTORY = []

    def __init__(self, name, species, diet, dob, health, injury, treatment,
                 min_encl_size, origin=2, sleep=False):
        super().__init__(name, species, diet, dob, health, injury, treatment,
                         min_encl_size)
        self.__class_ = Aves.CLASS
        self.__origin = origin
        self.__dietary_comments = {}
        self.__health_comments = {}
        self.__actions = []
        self.__behaviours = []
        self.__traits = []
        self.__own_sound = ''
        self.__sleep = sleep

        self.AVES_ID += 1
        Aves.AVES_INVENTORY.append(self)

    def __str__(self) -> str:
        return (f'Class: {Aves.CLASS}\n'
                f'{super().__str__()}'
                f'Reptile ID: {self.AVES_ID:04d}\n'
                f'Origin: {Aves.ORIGIN[int(self.__origin)]}')

    def __repr__(self):
        return (f'Aves (name= {self.name},'
                f'species= {self.species},'
                f'diet= {1},'
                f'dob= {'2020-01-01'},'
                f'health = {2},'
                f'injury = {False},'
                f'treatment = {True},'
                f'origin= {2})'
                f'sleep = {False}'
                )

    @property
    def origin(self) -> int:
        """Origin property"""
        return self.__origin

    @origin.setter
    def origin(self, origin: int) -> None:
        """
        Validating origin input as per origin list.
        :param origin: int
        :return: None
        """

        # Identifying the number of origins
        no_origins = len(Aves.ORIGIN)
        print()

        # Printing origin dictionary to assist user selection
        for key, value in Aves.ORIGIN.items():
            print(f'{key}:{value}')

        # Input validation using while loop and try/except forms
        while True:
            try:
                if origin == 0 or origin == '' or type(origin) == True:
                    origin = input(f'Please enter a valid input.\n'
                                   f'Input needs to be between 1 and {no_origins}: ')
                origin = int(origin)
                if 1 <= origin <= no_origins:
                    print(f"{self.name}'s origin has been changed to {Aves.ORIGIN[origin]}\n")
                    self.__origin = origin
                    # If successful, exit
                    break
                else:
                    origin = input(f'Please enter a valid input.\n'
                                   f'Input needs to be between 1 and {no_origins}: ')
            except ValueError:
                print(f"Error.\nOnly integers between 1 and {no_origins} are valid.")
                origin = input('Please try again: ')

    @property
    def own_sound(self) -> str:
        """Own sound property"""
        return self.__own_sound

    @own_sound.setter
    def own_sound(self, sound: str) -> None:
        """
        Aves's own sound
        :param sound: str
        :return: None
        """
        self.__own_sound = sound

    @property
    def sleeping(self) -> bool:
        """Sleeping property"""
        return self.__sleep

    @sleeping.setter
    def sleeping(self, value) -> None:
        """
        Aves's sleeping status
        :return: None
        """
        if value:
            print(f'{self.name} is awake\n'
                  f'{self.__own_sound}')
        else:
            print(f'{self.name} is asleep\n'
                  f'zzzzzzzz')
        self.__sleep = value

    def dietary_comments(self):
        """
        Dietary requirements
        A copy of the file as a dictionary is saved externally
        :return: None
        """
        self.__dietary_comments = reports.basic_report('Dietary Requirements',
                                                       self.name,
                                                       {})
        # Writing an external file for reference
        file_name = f'{self.name}_dietary_comments'
        with open(file_name, 'wb') as f:
            pickle.dump(self.__dietary_comments, f)

    def print_dietary_comments(self) -> None:
        """
        Printing dietary comments on file
        :return: None
        """
        print(f"{self.name}'s dietary requirement:")
        print_report.print_b(self.__dietary_comments)

    def health_comments(self) -> None:
        """
        Health requirements
        :return: None
        """
        health_format = reports.formats_available(3)
        self.__health_comments = reports.extended_report(self.name, 3,
                                                         'health report')

        # Writing an external file for reference
        file_name = f'{self.name}_health_report'
        with open(file_name, 'wb') as f:
            pickle.dump(self.__health_comments, f)

    def print_health_report(self) -> None:
        """
        Printing health report comments on file
        :return: None
        """
        print(f"{self.name}'s health report:")
        print_report.print_b(self.__health_comments)

    @staticmethod
    def flying():
        """
        Aves particularity
        :return: None
        """
        print('... looking at the world from above...')

    def actions(self):
        """
        Aves actions
        """
        self.__actions = ['flight', 'perching', 'preening']
        print(f'{self.__actions}')

    def behaviours(self):
        """
        Aves behaviours
        """
        self.__behaviours = ['cooperative breeding', 'social learning'
                                                     'pair bonds', 'flocking']
        print(f'{self.__behaviours}')

    def traits(self):
        """
        Aves traits
        """
        self.__traits = ['have feathers', 'beak without teeth',
                         'wings', 'bipedal']
        print(f'{self.__traits}')


class Reptilia(Animal):
    """"
    Concrete Class Reptilia, child class of Animal containing Vertebrae
    Reptiles. Around 12,000 documented species.

    Class Attributes:
    CLASS: Reptilia
    ORIGIN: dictionary with the 4 possible origins.
    REPTILE_ID: Unique sequential number for each individual reptile.
    REPTILE_INVENTORY: List of all reptiles created using this class.

    Attributes:
    As inherited from Animal Class plus:
    +Origin: int

    Methods:
    As inherited from Animal Class plus:
    +print_dietary_comments
    +print_health report

    Static Method:
    Particular to Reptiles:
    +basking

    External modules used (purposedly created):
    +date_validation
    +reports
    +print_reports
    """
    CLASS = 'Reptilia'
    ORIGIN = {1: 'Wild Captured',
              2: 'Bred Locally',
              3: 'Bred Elsewhere',
              4: 'On loan'}
    REPTILE_ID = 0
    REPTILE_INVENTORY = []

    def __init__(self, name, species, diet, dob, health, injury, treatment,
                 min_encl_size, origin=2, sleep=False):
        super().__init__(name, species, diet, dob, health, injury, treatment,
                         min_encl_size)
        self.__class_ = Reptilia.CLASS
        self.__origin = origin
        self.__dietary_comments = {}
        self.__health_comments = {}
        self.__actions = []
        self.__behaviours = []
        self.__traits = []
        self.__own_sound = ''
        self.__sleep = sleep

        self.REPTILE_ID += 1
        Reptilia.REPTILE_INVENTORY.append(self)

    def __str__(self) -> str:
        return (f'Class: {Reptilia.CLASS}\n'
                f'{super().__str__()}'
                f'Reptile ID: {self.REPTILE_ID:04d}\n'
                f'Origin: {Reptilia.ORIGIN[int(self.__origin)]}'
                )

    def __repr__(self):
        return (f'Reptilia(name= {self.name},'
                f'species= {self.species},'
                f'diet= {1},'
                f'dob= {'2020-01-01'},'
                f'health = {2},'
                f'injury = {False},'
                f'treatment = {True},'
                f'origin= {2})'
                f'sleep= {False}'
                )

    @property
    def origin(self) -> int:
        """Origin property"""
        return self.__origin

    @origin.setter
    def origin(self, origin: int) -> None:
        """
        Validating origin input as per origin list.
        :param origin: int
        :return: None
        """

        # Identifying the number of origins
        no_origins = len(Reptilia.ORIGIN)
        print()

        # Printing origin dictionary to assist user selection
        for key, value in Reptilia.ORIGIN.items():
            print(f'{key}:{value}')

        # Input validation using while loop and try/except forms
        while True:
            try:
                if origin == 0 or origin == '' or type(origin) == True:
                    origin = input(f'Please enter a valid input.\n'
                                   f'Input needs to be between 1 '
                                   f'and {no_origins}: ')
                origin = int(origin)
                if 1 <= origin <= no_origins:
                    print(f"{self.name}'s origin has been changed "
                          f"to {Reptilia.ORIGIN[origin]}\n")
                    self.__origin = origin
                    # If successful, exit
                    break
                else:
                    origin = input(f'Please enter a valid input.\n'
                                   f'Input needs to be between 1 '
                                   f'and {no_origins}: ')
            except ValueError:
                print(f"Error.\nOnly integers between 1 and {no_origins} "
                      f"are valid.")
                origin = input('Please try again: ')

    @property
    def own_sound(self) -> str:
        """Own sound property"""
        return self.__own_sound

    @own_sound.setter
    def own_sound(self, sound: str) -> None:
        """
        Reptilia's own sound
        :param sound: str
        :return: None
        """
        self.__own_sound = sound

    @property
    def sleeping(self) -> bool:
        """Sleeping property"""
        return self.__sleep

    @sleeping.setter
    def sleeping(self, value) -> None:
        """
        Reptilia's sleeping status
        :return: None
        """
        if value:
            print(f'{self.name} is awake\n'
                  f'{self.__own_sound}')
        else:
            print(f'{self.name} is asleep\n'
                  f'zzzzzzzz')
        self.__sleep = value

    def dietary_comments(self):
        """
        Dietary requirements
        A copy of the file as a dictionary is saved externally
        :return: None
        """
        self.__dietary_comments = reports.basic_report('Dietary Requirements',
                                                       self.name,
                                                       {})
        # Writing an external file for reference
        file_name = f'{self.name}_dietary_comments'
        with open(file_name, 'wb') as f:
            pickle.dump(self.__dietary_comments, f)

    def print_dietary_comments(self) -> None:
        """
        Printing dietary comments on file
        :return: None
        """
        print(f"{self.name}'s dietary requirement:")
        print_report.print_b(self.__dietary_comments)

    def health_comments(self) -> None:
        """
        Health requirements
        :return: None
        """
        health_format = reports.formats_available(3)
        self.__health_comments = reports.extended_report(self.name, 3,
                                                         'health report')

        # Writing an external file for reference
        file_name = f'{self.name}_health_report'
        with open(file_name, 'wb') as f:
            pickle.dump(self.__health_comments, f)

    def print_health_report(self) -> None:
        """
        Printing health report comments on file
        :return: None
        """
        print(f"{self.name}'s health report:")
        print_report.print_b(self.__health_comments)

    @staticmethod
    def basking():
        """
        Reptiles particularity
        :return: None
        """
        print('... hopefully from direct sunlight...')

    def actions(self):
        """
        Reptile actions
        """
        self.__actions = ['aggressive hunters', 'threat displays',
                          'physical defense']
        print(f'{self.__actions}')

    def behaviours(self):
        """
        Reptile behaviours
        """
        self.__behaviours = ['thermoregulation', 'defensive displays'
                             'mostly solitary', 'group hibernation']
        print(f'{self.__behaviours}')

    def traits(self):
        """
        Reptile traits
        """
        self.__traits = ['ectothermic', 'dry-scaly skin',
                         'have lungs for breathing', 'tetrapods']
        print(f'{self.__traits}')


class Ctenophora(Animal):
    """"
    Concrete Class Ctenophora, child class of Animal containing marine invertebrates,
    commonly known as comb jellies. Around 186 documented species.

    Class Attributes:
    CLASS: Ctenophora
    ORIGIN: dictionary with the 4 possible origins.
    CTENOPHORA_ID: Unique sequential number for each individual Ctenophora.
    CTENOPHORA_INVENTORY: List of all Ctenophorae created using this class.

    Attributes:
    As inherited from Animal Class plus:
    +Origin: int

    Methods:
    As inherited from Animal Class plus:
    +print_dietary_comments
    +print_health report

    Static Method:
    Particular to Aves:
    +drifting

    External modules used (purposedly created):
    +date_validation
    +reports
    +print_reports
    """
    CLASS = 'Ctenophora'
    ORIGIN = {1: 'Wild Captured',
              2: 'Bred Locally',
              3: 'Bred Elsewhere',
              4: 'On loan'}
    CTENOPHORA_ID = 0
    CTENOPHORA_INVENTORY = []

    def __init__(self, name, species, diet, dob, health, injury, treatment,
                 min_encl_size, origin=2):
        super().__init__(name, species, diet, dob, health, injury, treatment,
                         min_encl_size)
        self.__class_ = Ctenophora.CLASS
        self.__origin = origin
        self.__dietary_comments = {}
        self.__health_comments = {}
        self.__actions = []
        self.__behaviours = []
        self.__traits = []
        self.__own_sound = ''
        self.__sleep = False

        self.CTENOPHORA_ID += 1
        Ctenophora.CTENOPHORA_INVENTORY.append(self)

    def __str__(self) -> str:
        return (f'Class: {Ctenophora.CLASS}\n'
                f'{super().__str__()}'
                f'Ctenophora ID: {self.CTENOPHORA_ID:04d}\n'
                f'Origin: {Ctenophora.ORIGIN[int(self.__origin)]}')

    def __repr__(self):
        return (f'Ctenophora(name= {self.name},'
                f'species= {self.species},'
                f'diet= {1},'
                f'dob= {'2020-01-01'},'
                f'health = {2},'
                f'injury = {False},'
                f'treatment = {True},'
                f'origin= {2})')

    @property
    def origin(self) -> int:
        """Origin property"""
        return self.__origin

    @origin.setter
    def origin(self, origin: int) -> None:
        """
        Validating origin input as per origin list.
        :param origin: int
        :return: None
        """

        # Identifying the number of origins
        no_origins = len(Ctenophora.ORIGIN)
        print()

        # Printing origin dictionary to assist user selection
        for key, value in Ctenophora.ORIGIN.items():
            print(f'{key}:{value}')

        # Input validation using while loop and try/except forms
        while True:
            try:
                if origin == 0 or origin == '' or type(origin) == True:
                    origin = input(f'Please enter a valid input.\n'
                                   f'Input needs to be between 1 '
                                   f'and {no_origins}: ')
                origin = int(origin)
                if 1 <= origin <= no_origins:
                    print(f"{self.name}'s origin has been changed "
                          f"to {Ctenophora.ORIGIN[origin]}\n")
                    self.__origin = origin
                    # If successful, exit
                    break
                else:
                    origin = input(f'Please enter a valid input.\n'
                                   f'Input needs to be between 1 '
                                   f'and {no_origins}: ')
            except ValueError:
                print(f"Error.\nOnly integers between 1 and {no_origins} "
                      f"are valid.")
                origin = input('Please try again: ')

    @property
    def own_sound(self) -> str:
        """Own sound property"""
        return self.__own_sound

    @own_sound.setter
    def own_sound(self, sound: str) -> None:
        """
        Ctenophora's own sound
        :param sound: str
        :return: None
        """
        self.__own_sound = sound

    @property
    def sleeping(self) -> bool:
        """Sleeping property"""
        return self.__sleep

    @sleeping.setter
    def sleeping(self, value) -> None:
        """
        Ctenophora's sleeping status
        :return: None
        """
        if value:
            print(f'{self.name} is awake\n'
                  f'{self.__own_sound}')
        else:
            print(f'{self.name} is asleep\n'
                  f'zzzzzzzz')
        self.__sleep = value

    def dietary_comments(self):
        """
        Dietary requirements
        A copy of the file as a dictionary is saved externally
        :return: None
        """
        self.__dietary_comments = reports.basic_report('Dietary Requirements',
                                                       self.name,
                                                       {})
        # Writing an external file for reference
        file_name = f'{self.name}_dietary_comments'
        with open(file_name, 'wb') as f:
            pickle.dump(self.__dietary_comments, f)

    def print_dietary_comments(self) -> None:
        """
        Printing dietary comments on file
        :return: None
        """
        print(f"{self.name}'s dietary requirement:")
        print_report.print_b(self.__dietary_comments)

    def health_comments(self) -> None:
        """
        Health requirements
        :return: None
        """
        health_format = reports.formats_available(3)
        self.__health_comments = reports.extended_report(self.name, 3,
                                                         'health report')

        # Writing an external file for reference
        file_name = f'{self.name}_health_report'
        with open(file_name, 'wb') as f:
            pickle.dump(self.__health_comments, f)

    def print_health_report(self) -> None:
        """
        Printing health report comments on file
        :return: None
        """
        print(f"{self.name}'s health report:")
        print_report.print_b(self.__health_comments)

    @staticmethod
    def drifting():
        """
        Ctenophora particularity
        :return: None
        """
        print('... looking at the world from below... quietly')

    def actions(self):
        """
        Ctenophora actions
        """
        self.__actions = ['cilia-powered movement', 'maintain orientation',
                          'passive drifting']
        print(f'{self.__actions}')

    def behaviours(self):
        """
        Ctenophora behaviours
        """
        self.__behaviours = ['tentacle capture', 'not social'
                             'lack of brain', 'solitary']
        print(f'{self.__behaviours}')

    def traits(self):
        """
        Ctenophora traits
        """
        self.__traits = ['eight rows if ciliary combs', 'biradial',
                         'bioluminescence', 'clear gelatinous body']
        print(f'{self.__traits}')