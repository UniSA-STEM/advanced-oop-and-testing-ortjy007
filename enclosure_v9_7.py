# File          : enclosure_v9_7.py
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

from abc import ABC, abstractmethod

import validation
import enclosure_data
import zoo_zones
import enclosure_features

# Global variable
DATE_FORMAT = '%Y-%m-%d'

class Enclosure(ABC):
    """
    100% StarDust: Zoo Management Software (ZMS)
    Created ByteWise Consulting.
    All rights unreserved.

   Abstract Enclosure class to be used as the parent class for the
    zoo project...
    Class attributes:
    ZOO_ZONES: Zones a per current Zoo Facilities.
    ENCLOSURE-TYPE: dictionary with the types of enclosures
    available
    CLEANING_STATUS: dictionary with cleaning levels
    MAINTENANCE_STATUS: dictionary with maintenance levels

    ENCLOSURE_INVENTORY: List of all enclosures created using this class.
    MAX_ARE: Maximum enclosure size

    Attributes (self-explanatory):
    -location: str
    -type: str
    -multi_species: bool
    -cleaning: str
    -maintenance: srt
    -area: int

    Methods w/decorators (all inputs validated):
    +location @property getter + setter
    +type_ @property getter + setter
    +multi_species @property getter + setter
    +cleaning @property getter + setter
    +maintenance @property getter + setter
    +area @property getter + setter

    Abstract methods:
    +checking
    """

    # General enclosure data
    ZOO_ZONES = zoo_zones.ZOO_ZONES
    ENCLOSURE_TYPE = enclosure_data.ENCLOSURE_TYPE
    CLEANING_STATUS = enclosure_data.CLEANING_STATUS
    MAINTENANCE_STATUS = enclosure_data.MAINTENANCE_STATUS

    # Container for all instances
    ENCLOSURE_INVENTORY = []

    # Max enclosure area
    MAX_AREA = 500

    def __init__(self, location: str, type_: str, multi_species: bool, cleaning: int,
                 maintenance: int, area: int):

        self._location = location
        self._type_ = type_
        self._multi_species = multi_species
        self._cleaning = cleaning
        self._maintenance = maintenance
        self._area = area

        # Care team for the enclosure:
        self.care_team: int

        # Animals in the enclosure:
        self.animals = []

    def __str__(self):
        return (f'Location: {zoo_zones.ZOO_ZONES[self._location]}\n'
                f'Type: {enclosure_data.ENCLOSURE_TYPE[self._type_]}\n'
                f'Is Multi Species: {self._multi_species}\n'
                f'Area: {self._area}m2\n'
                f'Clean Status: {enclosure_data.CLEANING_STATUS[self._cleaning]}\n'
                f'Maintenance Status: {enclosure_data.MAINTENANCE_STATUS[self._maintenance]}\n'
                )

    def __repr__(self):
        return (f'location= {self.location}, '
                f'type= {self._type_}, '
                f'multi_species= {self._multi_species}, '
                f'cleaning= {self._cleaning}, '
                f'maintenance= {self._maintenance},'
                f' area = {self._area}'
                )

    @property
    def location(self) -> str:
        return self._location

    @location.setter
    def location(self, _location: str) -> None:

        # Validating Enclosure Location
        if _location == 'Z0':
            self._location = _location
        else:
            print('Enclosure location: ')
            self._location = validation.dict_choice(Enclosure.ZOO_ZONES, _location)
            print(f'Enclosure location updated to {self._location}\n')

    @property
    def type_(self) -> str:
        return self._type_

    @type_.setter
    def type_(self, _type: str) -> None:

        # Validating Enclosure type
        if _type == 'E0':
            self._type_ = _type
        else:
            # Validating user input
            print('Enclosure type: ')
            self._type_ = validation.dict_choice(Enclosure.ZOO_ZONES, _type)
            print(f'Enclosure type updated to {self._type_}\n')

    @property
    def multi_species(self) -> bool:
        return self._multi_species

    @multi_species.setter
    def multi_species(self, _multi_species: bool) -> None:

        # Validating multi species input:
        if _multi_species:
            self._multi_species = _multi_species
        else:
            print('Is the enclosure multi species?: ')
            self._multi_species = validation.bool_TF_val(_multi_species)

    @property
    def cleaning(self) -> int:
        return self._cleaning

    @cleaning.setter
    def cleaning(self, _cleaning: int) -> None:

        # Validating user input
        print('Cleaning status of the enclosure: ')
        self._cleaning = validation.dict_choice(Enclosure.ZOO_ZONES, _cleaning)
        print(f'Enclosure Cleaning status set to {self._cleaning}\n')

    @property
    def maintenance(self) -> int:
        return self._maintenance

    @maintenance.setter
    def maintenance(self, _maintenance: str) -> None:

        # Validating user input
        print('Maintenance status of the enclosure: ')
        self._maintenance = validation.dict_choice(Enclosure.ZOO_ZONES, _maintenance)
        print(f'Enclosure Maintenance status set to {self._maintenance}\n')

    @property
    def area(self) -> float:
        return self._area

    @area.setter
    def area(self, area_: str) -> None:

        # Validating user input
        print('Enclosure area: ')
        self._area = validation.digit_val_float(Enclosure.MAX_AREA)
        print(f'Area of the enclosure has been set to {self._area}\n')

    @abstractmethod
    def checking(self, status) -> None:
        pass

class ZooEnclosure(Enclosure):
    """
    100% StarDust: Zoo Management Software (ZMS)
    Created ByteWise Consulting.
    All rights unreserved.

    Concrete ZooEnclosure class

    Class attributes:
    BASIC_FEATURES: placeholder for environmental conditions
    when required
    ANIMALS container for all species initiated

    Attributes (self-explanatory):
    +features: str

    Methods w/decorators (all inputs validated):
    +date_built @property getter + setter

    Methods:
    +print_features
    +add_animals
    +remove_animals
    +add_care_team
    +remove_care_team
    checking
    """
    # Default values for Zoo Enclosures
    BASIC_FEATURES = {'C': 'Temperate',
                      'V1': 'Forest',
                      'B2': 'Lake',
                      'W2': 'Freshwater',
                      'f3': 'No dry season'
                      }

    # Unique number for ID
    ID_COUNTER = 0

    # Container for all instances
    ANIMALS = []

    def __init__(self, location, type_, multi_species, cleaning, maintenance, area, features):
        super().__init__(location, type_, multi_species, cleaning, maintenance, area)

        # Creating unique ID per enclosure
        ZooEnclosure.ID_COUNTER += 1
        self.id_ = f'ZooE.{location}.{ZooEnclosure.ID_COUNTER:03d}'

        # Using default values for enclosure features if needed
        if features == 'F0':
            self._features = ZooEnclosure.BASIC_FEATURES
        else:
            print('Enclosure features: ')
            self._features = enclosure_features.assembly()

        # Dictionary for animal collection
        self._animals = {}

        # Dictionary for carers
        self._care_team = {}

        Enclosure.ENCLOSURE_INVENTORY.append(self)
        print('100% StarDust: Zoo Management Software (ZMS).\n')

    def __str__(self):
        return (f'Enclosure ID: {self.id_}\n'
                f'{'=' * 25}\n'
                f'{super().__str__()}'
                f'{'=' * 25}\n'
                f'Enclosure features:\n{(str(self._features).replace("'", '')
                                         .replace("{", '').replace("}", ''))}'
                )

    def __repr__(self):
        return (f'id= {self.id_},'
                f'{super().__repr__()},'
                f'features = {'XXX'}'
                )

    def print_features(self) -> None:
        for key, value in self._features.items():
            print(f'{key} {value}')

    def add_animals(self):
        pass
        """
        # Current animals in the enclosure
        print('Current animals are in the enclosure: ')
        print_report.print_b(ZooEnclosure.ANIMALS)
        
        # Current animals in the zoo
        print('Current animals in the zoo: ')
        print_report.print_b(animals_current.current_animals)
        
        # Validating the animal selection 
        tmp_animal = input('Select the animal for the animal list to be housed in this enclosure: ')
        animal = validation.dict_choice(Enclosure.ZOO_ZONES, tmp_animal)
        
        # Adding animal to enclosure        
        ZooEnclosure.ANIMALS[animal.name] = animal
        """

    def remove_animals(self):
        pass

    def add_care_team(self):
        pass

    def remove_care_team(self):
        pass

    def checking(self, value) -> None:
        print('Checking status')


#e1 = ZooEnclosure('Z1', 'E2', True, 1, 2, 125, '')
#print(e1)

# e1.location = ''
# e1.type_ = ''
# e1.multi_species = ''
# e1.cleaning = ''
# e1.maintenance = ''
# e1.area = ''
# e1._features = ''
#
# print(e1)
