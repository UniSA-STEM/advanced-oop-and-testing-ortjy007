# File          : animal.py
# Author        : Jorge Ortega
# Email id      : ortjy007@mymail.unisa.edu.au
# Description   : COMP 1048 advanced-oop-and-testing Assignment 2
#
# This is my own work as defined by the University's
# Academic Misconduct policy.
#
from abc import ABC, abstractmethod
import datetime
import pickle

import date_validation
import print_report
import reports
import validation
import animal_data
import enclosure_data

# Global Variables
DATE_FORMAT = '%Y-%m-%d'


class Animal(ABC):
    """
    100% StarDust: Zoo Management Software (ZMS)
    Created ByteWise Consulting.
    All rights unreserved.

    Abstract Animal class to be used as the parent class for the
    zoo project...
    Class attributes:
    DIET: dictionary with diets, additional information
    allowed in the child classes.
    HEALTH: dictionary with health conditions, additional information
    allowed in the child classes
    INJURY: dictionary with main injuries, additional information
    allowed in the child classes
    TREATMENT: dictionary with treatments, additional information
    allowed in the child classes
    ANIMAL_ID: Unique sequential number for each individual animal.
    ANIMAL_INVENTORY: List of all animals created using this class.

    Attributes (self-explanatory):
    name: str
    species: str
    dob: str = 2020-01-01 (Default)
    diet: str
    health: str
    injury: str
    treatment: str
    min_enclosure_size: int
    age: YYYY (calculated from dod to today's date)

    Methods w/decorators (all validating input):
    +name @property getter + setter
    +species @property getter + setter
    +dob @property getter + setter
    +diet @property getter + setter
    +health @property getter + setter
    +injury @property getter + setter
    +treatment @property getter + setter
    +min_encl_size @property getter + setter

    Abstract methods:
    +health_comments
    +dietary_comments
    """

    DIET = animal_data.DIET
    HEALTH = animal_data.HEALTH
    INJURY = animal_data.INJURY
    TREATMENT = animal_data.TREATMENT

    ANIMAL_ID = 0
    ANIMAL_INVENTORY = []

    def __init__(self, name: str, species: str, diet: str, health: str, injury: str,
                 treatment: str, min_encl_size: float, dob='2020-01-01'):

        self._name = validation.str_1(name, 'Name')
        self._species = validation.list_choice(animal_data.SPECIES, species)
        self._diet = diet

        # Validating date input, if invalid using default
        if dob != '2020-01-01':
            try:
                dob = datetime.datetime.strptime(dob, DATE_FORMAT)
                self._dob = dob.date()
            except ValueError:
                print('Incorrect date, default date used (2020-01-01).')
                self._dob = '2020-01-01'
        else:
            dob = datetime.datetime.strptime(dob, DATE_FORMAT)
            self._dob = dob.date()

        self._health = health
        self._injury = injury
        self._treatment = treatment
        self._min_encl_size = min_encl_size
        self._age = 0

        Animal.ANIMAL_ID += 1
        id_ = 'A' + str(f'{Animal.ANIMAL_ID:03d}')
        self.__id_ = id_

        Animal.ANIMAL_INVENTORY.append(self)
        print('100% StarDust: Zoo Management Software (ZMS).\n')

    def __str__(self) -> str:
        # Calculating age from DoB
        today = datetime.date.today()
        self._age = today.year - self._dob.year

        return (f'Name: {self._name}\n'
                f'Species: \x1B[3m{self._species}\x1B[0m\n'
                f'{'=' * 33}\n'
                f'Diet: {Animal.DIET[self._diet]}\n'
                f'Minium area/individual: {self._min_encl_size}m2\n'
                f'Health: {self._health}: {animal_data.HEALTH[self._health]}\n'
                f'Injuries: {self._injury}: {animal_data.INJURY[self._injury]}\n'
                f'In Treatment: {self._treatment}: {animal_data.TREATMENT[self._treatment]}\n'
                f'DoB: {self._dob}\n'
                f'Age: {self._age}\n'
                f'{'=' * 33}\n'
                )

    def __repr__(self) -> str:
        return (f'name= {self._name}, '
                f'Animal_ID= {self.__id_}, '
                f'species= {self._species}, '
                f'diet= {Animal.DIET[self._diet]}, '
                f'dob= {self._dob}, '
                f'health= {self._health}, '
                f'injury= {self._injury}, '
                f'treatment= {self._treatment}, '
                f'min encl size= {self._min_encl_size}'
                )

    @property
    def name(self) -> str:
        """Name property"""
        return self._name

    @name.setter
    def name(self, name_: str) -> None:
        """
        Validating name input to a-z letters only.
        :param name_: str
        :return: None
        """
        # Name validation using while loop
        while True:
            if isinstance(name_, str) and name_.isalpha():
                print(f'{name_} name created.')
                self._name = name_
                break
            else:
                name_ = input('Invalid input. Please try again using only letters: ')

    @property
    def species(self) -> str:
        """Species property"""
        return self._species

    @species.setter
    def species(self, species_: str) -> None:
        """
        Validating species input to a-z letters only and in italics.
        :param species_: str
        :return: None
        """
        if isinstance(species_, str) and all(char.isalpha() or char.isspace() for char in species_):
            print(f'{species_} species created.')
            self._species = species_
        else:
            print(f'Invalid input, the specie can only contain English alphabet letters.\n'
                  f'Temporary (\x1B[3m{species_}\x1B[0m with Animal ID number) name used.')
            self._species = f'\x1B[3mSpecies\x1B[0m' + str(self.ANIMAL_ID)

    @property
    def dob(self) -> 'datetime.date':
        """dob property"""
        return self._dob

    @dob.setter
    def dob(self, dob_: str) -> None:
        """
        setter for dob validated though the date_validation module
        :param dob_: str
        :return: None
        """
        # Creating sets to compare dob against numbers 0-9 and'-'
        set1 = '0123456789-'

        # Validating numbers and format
        while True:
            if set(dob_).issubset(set(set1)) and len(dob_) == 10:
                dob_split = dob_.split('-')
                dob_split_int = []
                for item in dob_split:
                    dob_split_int.append(item)
                # Validation date including no futures (not allowed).
                if (len(str(dob_split_int[0])) == 4
                        and len(str(dob_split_int[1])) == 2
                        and len(str(dob_split_int[2])) == 2):
                    # Validation date including no futures (not allowed).
                    self._dob = date_validation.validate_dob(int(dob_split_int[0]),
                                                             int(dob_split_int[1]),
                                                             int(dob_split_int[2]))
                    break
            else:
                dob_ = input('Please input a valid date in the DD-MM-YYYY format: ')
        today = datetime.datetime.today()
        today = today.date()
        self._age = self._dob - today

    @property
    def diet(self) -> str:
        """diet property"""
        return self._diet

    @diet.setter
    def diet(self, diet_: int) -> None:
        """
        Setter for validating the primary diet as per current ANIMAL.DIET dictionary
        :param diet_: int
        :return: None
        """

        # Validating diet input
        print('Animal diet: ')
        self._diet = validation.dict_choice(Animal.DIET, diet_)
        print(f"{self._name}'s diet updated to {self._diet}")

    @property
    def health(self) -> str:
        """health property"""
        return self._health

    @health.setter
    def health(self, health_: str) -> None:

        # Validating health input
        print('Animal health status: ')
        self._health = validation.dict_choice(Animal.HEALTH, health_)
        print(f"{self._name}'s health status updated to {self._health}\n")

    @property
    def injury(self) -> str:
        """injury property"""
        return self._injury

    @injury.setter
    def injury(self, injury_: str) -> None:

        # Validating injury input
        print('Animal injury status: ')
        self._injury = validation.dict_choice(Animal.INJURY, injury_)
        print(f"{self._name}'s injury status updated to {self._injury}\n")

    @property
    def treatment(self) -> str:
        """treatment property"""
        return self._treatment

    @treatment.setter
    def treatment(self, treatment_: str) -> None:
        """
        Treatment method for animals
        :param treatment_: str
        :return:
        """

        # Validating treatment input
        print('Animal injury status: ')
        self._treatment = validation.dict_choice(Animal.TREATMENT, treatment_)
        print(f"{self._name}'s injury status updated to {self._treatment}\n")

    @property
    def min_encl_size(self) -> float:
        """min_encl_size property"""
        return self._min_encl_size

    @min_encl_size.setter
    def min_encl_size(self, min_encl_size: float) -> None:
        self._min_encl_size = validation.digit_val_float(min_encl_size)

    @abstractmethod
    def health_comments(self):
        """
        Health comments for Parent Abstract Animal Class
        """
        pass

    @abstractmethod
    def dietary_comments(self):
        """
        Diet comments for Parent Abstract Animal Class
        """
        pass


class Ctenophora(Animal):
    """"
    Concrete Class Chordata, child class of Animal containing Vertebrae
    Class Attributes:
    CLASS: Chordata
    ORIGIN: dictionary with the 4 possible origins.
    CHORDATA_ID: Unique sequential number for each individual CHORDATA.
    CHORDATA_INVENTORY: List of all mammals created using this class.

    Attributes:
    As inherited from Animal Class plus:
    +Origin: int

    Methods:
    As inherited from Animal Class plus:
    +print_dietary_comments
    +print_health report
    """

    CLASS = animal_data.A_CLASS
    ORIGIN = animal_data.ORIGIN

    CTENOPHORA_ID = 0

    CTENOPHORA_INVENTORY = []  # Including animals as instances
    CTENOPHORA_DIRECTORY = []  # Including basic data as str

    def __init__(self, name, species, diet, health, injury, treatment,
                 min_encl_size, dob, class_, origin: str, sleep: bool):
        super().__init__(name, species, diet, health, injury, treatment,
                         min_encl_size, dob)

        self._class_ = class_
        self._origin = origin

        # Containers for reports
        self._dietary_comments = {}
        self._health_comments = {}

        self._own_sound = ''
        self._sleep = sleep

        Ctenophora.CTENOPHORA_ID += 1
        self._ID = 'CHO' + str(f'{Ctenophora.CTENOPHORA_ID:03}')
        Ctenophora.CTENOPHORA_INVENTORY.append(self)
        Ctenophora.CTENOPHORA_DIRECTORY.append((self.name, self.species))

    def __str__(self) -> str:
        return (f'{'=' * 33}\n'
                f'Class: {self._class_}: {Ctenophora.CLASS[self._class_]}\n'
                f'{super().__str__()}'
                f'Aves ID: {self._ID}\n'
                f'Origin: {self._origin}: {Ctenophora.ORIGIN[self.origin]}\n'
                f'Sleep: {self._sleep}'
                )

    def __repr__(self) -> str:
        return (f'{super().__repr__()}, '
                f'origin= {self._origin}, '
                f'sleep= {self._sleep},'
                )

    @property
    def class_(self) -> str:
        """Origin property"""
        return self._class_

    @class_.setter
    def class_(self, _class_: str) -> None:
        """
        Validating class input as per class list.
        :param _class_: int
        :return: None
        """
        print(f"{self.name}'s class: ")
        self._class_ = validation.dict_choice(animal_data.A_CLASS, _class_)
        print(f"\n{self.name}'s class updated to {self._class_}\n")

    @property
    def origin(self) -> str:
        """Origin property"""
        return self._origin

    @origin.setter
    def origin(self, origin_: str) -> None:
        """
        Validating origin input as per origin list.
        :param origin_: str
        :return: None
        """
        print(f"{self.name}'s origin: ")
        self._origin = validation.dict_choice(animal_data.ORIGIN, origin_)
        print(f"\n{self.name}'s origin updated to {self._origin}\n")

    @property
    def own_sound(self) -> str:
        """Own sound property"""
        return self._own_sound

    @own_sound.setter
    def own_sound(self, sound: str) -> None:
        """
        Ctenophora's own sound
        :param sound: str
        :return: None
        """
        self._own_sound = sound

    @property
    def sleeping(self) -> bool:
        """Sleeping property"""
        return self._sleep

    @sleeping.setter
    def sleeping(self, value) -> None:
        """
        Ctenophora's sleeping status
        :return: None
        """
        if value:
            print(f'{self.name} is awake\n'
                  f'{self._own_sound}')
        else:
            print(f'{self.name} is asleep\n'
                  f'zzzzzzzz')
        self._sleep = value

    def dietary_comments(self):
        """
        Dietary requirements
        A copy of the file as a dictionary is saved externally
        :return: None
        """
        self._dietary_comments = reports.basic_report('Dietary Requirements',
                                                      self._ID,
                                                      {})
        # Writing an external file for reference
        file_name = f'{self._ID}_dietary_comments'
        with open(file_name, 'wb') as f:
            pickle.dump(self._dietary_comments, f)

    def print_dietary_comments(self) -> None:
        """
        Printing dietary comments on file
        :return: None
        """
        print(f"{self._ID}'s dietary requirements:")
        print_report.print_b(self._dietary_comments)

    def health_comments(self) -> None:
        """
        Health requirements
        :return: None
        """
        health_format = reports.formats_available(3)
        self._health_comments = reports.basic_report('Health Requirements',
                                                      self._ID,
                                                      {})

        # Writing an external file for reference
        file_name = f'{self._ID}_health_requirements'
        with open(file_name, 'wb') as f:
            pickle.dump(self._health_comments, f)

    def print_health_report(self) -> None:
        """
        Printing health report comments on file
        :return: None
        """
        print(f"{self._ID}'s health requirements:")
        print_report.print_b(self._health_comments)

    @staticmethod
    def drifting():
        """
        Ctenophora particularity
        :return: None
        """
        print('... looking at the world from below... quietly')

    def actions(self) -> None:
        """
        Ctenophora actions
        """
        self.__actions = (f'cilia-powered movement', 'maintain orientation',
                          'passive drifting')
        print(f'{self.name} ctenophoras actions include:\n{', '.join(self.__actions)}\n')

    def behaviours(self) -> None:
        """
        Ctenophora behaviours
        """
        self.__behaviours = (f'tentacle capture', 'not social'
                                                  'lack of brain :) ', 'solitary')
        print(f'{self.name} ctenophoras behaviour include:\n{', '.join(self.__behaviours)}\n')

    def traits(self) -> None:
        """
        Ctenophora traits
        """
        self.__traits = (f'eight rows of ciliary combs', 'being biradial',
                         'having bioluminescence', 'having a clear gelatinous body')
        print(f'{self.name} ctenophoras traits include:\n{', '.join(self.__traits)}\n')


class Chordata(Animal):
    """"
    Concrete Class Chordata, child class of Animal containing Vertebrae
    Class Attributes:
    CLASS: Chordata
    ORIGIN: dictionary with the 4 possible origins.
    CHORDATA_ID: Unique sequential number for each individual CHORDATA.
    CHORDATA_INVENTORY: List of all mammals created using this class.

    Attributes:
    As inherited from Animal Class plus:
    +Origin: int

    Methods:
    As inherited from Animal Class plus:
    +print_dietary_comments
    +print_health report
    """

    CLASS = animal_data.A_CLASS
    ORIGIN = animal_data.ORIGIN

    MAMMAL_INVENTORY = []
    MAMMAL_DIRECTORY = []

    AVES_INVENTORY = []
    AVES_DIRECTORY = []

    REPTILIA_INVENTORY = []
    REPTILIA_DIRECTORY = []

    CHORDATA_INVENTORY = []
    CHORDATA_DIRECTORY = []

    CHORDATA_ID = 0

    def __init__(self, name, species, diet, health, injury, treatment,
                 min_encl_size, dob, class_, origin: str, sleep: bool):
        super().__init__(name, species, diet, health, injury, treatment,
                         min_encl_size, dob)

        self._class_ = class_
        self._origin = origin

        # If Mammalia
        if self._class_ == 'A1':
            Chordata.CHORDATA_ID += 1
            self._ID = 'A1' + str(f'{Chordata.CHORDATA_ID:03}')
            Chordata.MAMMAL_INVENTORY.append(self)
            Chordata.MAMMAL_DIRECTORY.append((self.name, self.species))

        # If Aves
        elif self._class_ == 'A2':
            Chordata.CHORDATA_ID += 1
            self._ID = 'A2' + str(f'{Chordata.CHORDATA_ID:03}')
            Chordata.AVES_INVENTORY.append(self)
            Chordata.AVES_DIRECTORY.append((self.name, self.species))

        # If Reptilia
        elif self._class_ == 'A3':
            Chordata.CHORDATA_ID += 1
            self._ID = 'A3' + str(f'{Chordata.CHORDATA_ID:03}')
            Chordata.REPTILIA_INVENTORY.append(self)
            Chordata.REPTILIA_DIRECTORY.append((self.name, self.species))

        else:
            Chordata.CHORDATA_ID += 1
            self._ID = 'Ax' + str(f'{Chordata.CHORDATA_ID:03}')
            Chordata.CHORDATA_INVENTORY.append(self)
            Chordata.CHORDATA_DIRECTORY.append((self.name, self.species))

        #Chordata.health_comments(self)
        #Chordata.dietary_comments(self)

        self._own_sound = ''
        self._sleep = sleep

    def __str__(self) -> str:
        return (f'{'=' * 33}\n'
                f'Class: {self._class_}: {Chordata.CLASS[self._class_]}\n'
                f'{super().__str__()}'
                f'Chordata ID: {self._ID}\n'
                f'Origin: {self._origin}: {Chordata.ORIGIN[self.origin]}\n'
                f'Sleep: {self._sleep}'
                )

    def __repr__(self) -> str:
        return (f'_ID: {self._ID}, '
                f'{super().__repr__()}, '
                f'origin= {self._origin}, '
                f'sleep= {self._sleep}'
                )

    @property
    def class_(self) -> str:
        """Origin property"""
        return self._class_

    @class_.setter
    def class_(self, _class_: str) -> None:
        """
        Validating class input as per class list.
        :param _class_: int
        :return: None
        """
        print(f"{self.name}'s class: ")
        self._class_ = validation.dict_choice(animal_data.A_CLASS, _class_)
        print(f"{self.name}'s class updated to {self._class_}\n")

    @property
    def origin(self) -> str:
        """Origin property"""
        return self._origin

    @origin.setter
    def origin(self, origin_: str) -> None:
        """
        Validating origin input as per origin list.
        :param origin_: str
        :return: None
        """
        print(f"{self.name}'s origin: ")
        self._origin = validation.dict_choice(animal_data.ORIGIN, origin_)
        print(f"{self.name}'s origin updated to {self._origin}\n")

    @property
    def own_sound(self) -> str:
        """Own sound property"""
        return self._own_sound

    @own_sound.setter
    def own_sound(self, sound: str) -> None:
        """
        Aves's own sound
        :param sound: str
        :return: None
        """
        self._own_sound = sound

    @property
    def sleeping(self) -> bool:
        """Sleeping property"""
        return self._sleep

    @sleeping.setter
    def sleeping(self, value) -> None:
        """
        Aves's sleeping status
        :return: None
        """
        if value:
            print(f'{self.name} is awake\n'
                  f'{self._own_sound}')
        else:
            print(f'{self.name} is asleep\n'
                  f'zzzzzzzz')
        self._sleep = value

    def dietary_comments(self) -> None:
        """
        Dietary requirements
        A copy of the file as a dictionary is saved externally
        :return: None
        """
        self._dietary_comments = reports.basic_report('Dietary Requirements',
                                                      self._ID,
                                                      {})
        # Writing an external file for reference
        file_name = f'{self._ID}_dietary_comments'
        with open(file_name, 'wb') as f:
            pickle.dump(self._dietary_comments, f)


    def print_dietary_comments(self) -> None:
        """
        Printing dietary comments on file
        :return: None
        """
        print(f"{self.name}'s dietary requirement:")
        print_report.print_b(self._dietary_comments)

    def health_comments(self) -> None:
        """
        Health requirements
        :return: None
        """
        health_format = reports.formats_available(3)
        self._health_comments = reports.basic_report('Health requirements', self._ID, {})

        # Writing an external file for reference
        file_name = f'{self._ID}_health_comments'
        with open(file_name, 'wb') as f:
            pickle.dump(self._health_comments, f)

    def print_health_report(self) -> None:
        """
        Printing health report comments on file
        :return: None
        """
        print(f"{self.name}'s health report:")
        print_report.print_b(self._health_comments)


class Mammal(Chordata):
    """"
    Concrete Class Aves, child class of Chordata containing Vertebrae
    Mammalians. Around 6,640 documented species.

    Class Attributes:
    -Enclosure

    Attributes:
    As inherited from Chordata Class plus:
    +Origin: int

    Methods:
    As inherited from Chordata Class plus:
    +actions
    +behaviours
    +traits

    Static Method:
    Particular to Mammals:
    +Suckling
    """

    CURRENT_ENCLOSURES = enclosure_data.CURRENT_ENCLOSURES

    def __init__(self, name, species, diet, health, injury, treatment,
                 min_encl_size, dob, class_, origin, sleep, enclosure):
        super().__init__(name, species, diet, health, injury, treatment,
                         min_encl_size, dob, class_, origin, sleep)

        self._enclosure = enclosure
        self.actions = self.actions()
        self.behaviours = self.behaviours()
        self.traits = self.traits()

    def __str__(self) -> str:
        return (f'{super().__str__()}\n'
                f'{'=' * 33}\n'
                f'Enclosure: {self._enclosure}\n'
                )

    def __repr__(self) -> str:
        return (f'{super().__repr__()}, '
                f'enclosure= {self._enclosure}'
                )

    @property
    def enclosure(self) -> str:
        """enclosure property"""
        return self._enclosure

    @enclosure.setter
    def enclosure(self, enclosure_: str) -> None:
        """
        Validating enclosure input as per enclosure list.
        :param enclosure_: int
        :return: None
        """

        # Validating origin input
        print(f'New enclosure for {self._name}: ')
        self._enclosure = validation.list_choice_enum(Mammal.CURRENT_ENCLOSURES, enclosure_)
        print(f"{self._name}'s new home is {self._enclosure}\n")

    def print_dietary_comments(self) -> None:
        """
        Printing dietary comments on file
        :return: None
        """
        print(f"{self._ID}'s dietary requirements:")
        print_report.print_b(self._dietary_comments)

    def print_health_report(self) -> None:
        """
        Printing health report comments on file
        :return: None
        """
        print(f"{self._ID}'s health requirements:")
        print_report.print_b(self._health_comments)

    @staticmethod
    def suckling() -> None:
        """
        Mammals particularity
        :return: None
        """
        print(f'... having a nurturing breakfast...\n')

    def actions(self) -> None:
        """
       Mammals  actions
        """
        self.__actions = f'live birth to live offsprings'
        print(f'{self.name} mammals actions include:\n{self.__actions}\n')

    def behaviours(self) -> None:
        """
        Mammals behaviours
        """
        self.__behaviours = 'social bonding', 'communications through ', 'vocalizations and scent', 'territorial'
        print(f'{self.name} mammals behaviours include:\n {', '.join(self.__behaviours)}\n')

    def traits(self) -> None:
        """
        Mammals  traits
        """
        self.__traits = 'endotherm', 'have hair or fur', 'have three middle ear bones'
        print(f'{self.name} mammals traits include:\n{', '.join(self.__traits)}\n')


class Aves(Chordata):
    """"
    Concrete Class AvesAves, child class of Chordata containing Vertebrae
    Aves. Around 6,640 documented species.

    Class Attributes:
    -Enclosure

    Attributes:
    As inherited from Chordata Class plus:
    +Origin: int

    Methods:
    As inherited from Chordata Class plus:
    +actions
    +behaviours
    +traits

    Static Method:
    Particular to Aves:
    +Flying
    """

    CURRENT_ENCLOSURES = enclosure_data.CURRENT_ENCLOSURES

    def __init__(self, name, species, diet, health, injury, treatment,
                 min_encl_size, dob, class_, origin, sleep, enclosure):
        super().__init__(name, species, diet, health, injury, treatment,
                         min_encl_size, dob, class_, origin, sleep)

        self._enclosure = enclosure

    def __str__(self) -> str:
        return (f'{super().__str__()}\n'
                f'{'=' * 33}\n'
                f'Enclosure: {self._enclosure}\n'
                )

    def __repr__(self) -> str:
        return (f'{super().__repr__()}, '
                f'enclosure= {self._enclosure}'
                )

    @property
    def enclosure(self) -> str:
        """enclosure property"""
        return self._enclosure

    @enclosure.setter
    def enclosure(self, enclosure_: str) -> None:
        """
        Validating enclosure input as per enclosure list.
        :param enclosure_: int
        :return: None
        """

        # Validating origin input
        print(f'New enclosure for {self._name}: ')
        self._enclosure = validation.list_choice_enum(Aves.CURRENT_ENCLOSURES, enclosure_)
        print(f"{self._name}'s new home is {self._enclosure}\n")

    def print_dietary_comments(self) -> None:
        """
        Printing dietary comments on file
        :return: None
        """
        print(f"{self._ID}'s dietary requirements:")
        print_report.print_b(self._dietary_comments)

    def print_health_report(self) -> None:
        """
        Printing health report comments on file
        :return: None
        """
        print(f"{self._ID}'s health requirements:")
        print_report.print_b(self._health_comments)

    @staticmethod
    def flying() -> None:
        """
        Aves particularity
        :return: None
        """
        print(f'... looking at the world from above...')

    def actions(self) -> None:
        """
        Aves actions
        """
        self.__actions = (f'flying', 'perching', 'preening')
        print(f'{self.name} aves actions include:\n{', '.join(self.__actions)}\n')

    def behaviours(self) -> None:
        """
        Aves behaviours
        """
        self.__behaviours = 'cooperative breeding', 'social learning', 'pair bonds', 'flocking'
        print(f'{self.name} aves behaviours include:\n{', '.join(self.__behaviours)}\n')

    def traits(self) -> None:
        """
        Aves traits
        """
        self.__traits = 'have feathers', 'beak without teeth', 'having wings', 'being bipedal'
        print(f'{self.name} aves traits include:\n{', '.join(self.__traits)}\n')


class Reptilia(Chordata):
    """"
    Concrete Class Reptilia, child class of Chordata containing Vertebrae
    Reptilia. Around 6,640 documented species.

    Class Attributes:
    -Enclosure

    Attributes:
    As inherited from Chordata Class plus:
    +Origin: int

    Methods:
    As inherited from Chordata Class plus:
    +actions
    +behaviours
    +traits

    Static Method:
    Particular to Reptiles:
    +Basking
    """

    CURRENT_ENCLOSURES = enclosure_data.CURRENT_ENCLOSURES

    def __init__(self, name, species, diet, health, injury, treatment,
                 min_encl_size, dob, class_, origin, sleep, enclosure):
        super().__init__(name, species, diet, health, injury, treatment,
                         min_encl_size, dob, class_, origin, sleep)

        self._enclosure = enclosure

    def __str__(self) -> str:
        return (f'{super().__str__()}\n'
                f'{'=' * 33}\n'
                f'Enclosure: {self._enclosure}\n'
                )

    def __repr__(self) -> str:
        return (f'{super().__repr__()}, '
                f'enclosure= {self._enclosure}'
                )

    @property
    def enclosure(self) -> str:
        """enclosure property"""
        return self._enclosure

    @enclosure.setter
    def enclosure(self, enclosure_: str) -> None:
        """
        Validating enclosure input as per enclosure list.
        :param enclosure_: int
        :return: None
        """

        # Validating origin input
        print(f'New enclosure for {self._name}: ')
        self._enclosure = validation.list_choice_enum(Reptilia.CURRENT_ENCLOSURES, enclosure_)
        print(f"{self._name}'s new home is {self._enclosure}\n")

    def print_dietary_comments(self) -> None:
        """
        Printing dietary comments on file
        :return: None
        """
        print(f"{self._ID}'s dietary requirements:")
        print_report.print_b(self._dietary_comments)

    def print_health_report(self) -> None:
        """
        Printing health report comments on file
        :return: None
        """
        print(f"{self._ID}'s health requirements:")
        print_report.print_b(self._health_comments)

    @staticmethod
    def basking() -> None:
        """
        Reptilia particularity
        :return: None
        """
        print('... hopefully from direct sunlight...')

    def actions(self) -> None:
        """
        Reptiles actions
        """
        self.__actions = (f'aggressive hunters', 'threat displays', 'physical defense')
        print(f'{self.name} reptile actions include:\n{', '.join(self.__actions)}\n')

    def behaviours(self) -> None:
        """
        Reptiles behaviours
        """
        self.__behaviours = 'thermoregulation', 'defensive displays', 'mostly solitary', 'group hibernation'
        print(f'{self.name} aves behaviours include:\n{', '.join(self.__behaviours)}\n')

    def traits(self) -> None:
        """
        Aves traits
        """
        self.__traits = 'ectothermic', 'dry-scaly skin', 'have lungs for breathing', 'tetrapods'
        print(f'{self.name} aves traits include:\n{', '.join(self.__traits)}\n')

m1 =  Mammal('Tigger', 'Panthera Tigris', 'D1', 'H1','J1', 'T0', 50,'2020-03-02','A1','R1',False,'ZooE_Z0_001')
