# File          : staff_v9.7.py
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
import personal_data
import staff_data
import datetime


class Person(ABC):
    """
    100% StarDust: Zoo Management Software (ZMS)
    Created ByteWise Consulting.
    All rights unreserved.

    Abstract Person class to be used as the parent class for the
    zoo project...

    Class attributes:
    WORK_RIGHTS: dictionary with the types of work rights
    available
    GENDER: dictionary with gender options

    Attributes (self-explanatory):
    -name: str
    -last_name: str
    -dob: str
    -gender: str
    -work_r: srt

    Methods w/decorators (all inputs validated):
    +name @property getter + setter
    +last_name @property getter + setter
    +dob @property getter + setter
    +gender @property getter + setter
    +work_r @property getter + setter

    Abstract methods:
    +wants_to_work
    """
    # General personal data
    WORK_RIGHTS = personal_data.WORK_RIGHTS
    GENDER = personal_data.GENDER

    def __init__(self, name: str, last_name: str, dob: str, gender: str, work_r: str):

        self._name = name
        self._last_name = last_name
        self._dob = dob
        self._gender = gender
        self._work_r = work_r

    def __str__(self):
        return (f'Name: {self._name}\n'
                f'Last Name: {self._last_name}\n'
                f'DoB: {self._dob}\n'
                f'Gender: {self._gender}\n'
                f'Work Rights: {self._work_r}\n'
                )

    def __repr__(self):
        return (f'name= {self.name}, '
                f'last_name= {self._last_name}, '
                f'dob= {self._dob}, '
                f'gender= {self._gender}, '
                f'work_r= {self._work_r}'
                )

    @property
    def name(self) -> str:
        """
        Name property
        :return: None
        """
        return self._name

    @name.setter
    def name(self, name_: str) -> None:
        self._name = (validation.str_1(name_, 'Name')).capitalize()

    @property
    def last_name(self) -> str:
        """
        last name property
        :return: None
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name_: str) -> None:
        self._last_name = (validation.str_1(last_name_, 'Last name')).capitalize()

    @property
    def dob(self) -> str:
        """
        date of birth dob property
        :return: None
        """
        return self._dob

    @dob.setter
    def dob(self, dob_: str) -> None:
        """
        setter for dob validated though the date_validation module
        :param dob_: str
        :return: None
        """

        while dob_:
            if dob_ != '2020-01-01':
                date_format = '%Y-%m-%d'
                try:
                    datetime.datetime.strptime(dob_, date_format)
                    self._dob = dob_
                    break
                except ValueError:
                    dob_ = input('Incorrect date, please try again using the YYYY-MM-DD format: ')
            print(f'DoB set to {dob_}\n')

    @property
    def gender(self) -> str:
        """
        gender property
        :return: None
        """
        return self._gender

    @gender.setter
    def gender(self, gender_: str) -> None:

        print("Person's gender: ")
        self._gender = validation.dict_choice(personal_data.GENDER, gender_)
        print(f"Person's gender updated to {self._gender}\n")

    @property
    def work_r(self) -> str:
        """
        work rights work-r property
        :return: None
        """
        return self._work_r

    @work_r.setter
    def work_r(self, work_r_: str) -> None:

        print('Staff working rights: ')
        self._work_r = validation.dict_choice(personal_data.WORK_RIGHTS, work_r_)
        print(f'Staff working rights updated to {self._work_r}\n')

    @abstractmethod
    def wants_to_work(self, value):
        """
        Abstract method for implementation in child class
        :param value:
        """
        pass


class Staff(Person):
    """
    100% StarDust: Zoo Management Software (ZMS)
    Created ByteWise Consulting.
    All rights unreserved.

    Concrete Person ZooEnclosure class

    Class attributes:
    QUALIFICATIONS: dictionary with the types of qualifications
    available

    REMUNERATION: dictionary with the remuneration levels
    available

    Attributes (self-explanatory):
    -staff_IDs: str

    Methods w/decorators (all inputs validated):
    +staff_IDs @property getter + setter
    +qualifications @property getter + setter
    +remuneration @property getter + setter

    Methods:
    +wants_to_work
    """

    # General Staff data
    QUALIFICATIONS = staff_data.QUALIFICATIONS
    REMUNERATION = staff_data.REMUNERATION

    # Unique number for ID
    ID_COUNTER = 0

    # Container for all instances
    STAFF_LIST = []

    def __init__(self, name, last_name, dob, gender, work_r, qualifications: str, remuneration: str):
        super().__init__(name, last_name, dob, gender, work_r)

        Staff.ID_COUNTER += 1
        # Creating unique ID per staff
        if self.name is None or self.name == 0 or self.name == '':
            str_ = input(f'Your Name and Last Name can not be empty.\nA temporary'
                         f' ID number has been created.')
            staff_ID = f'ZooS.Temp_ID.{Staff.ID_COUNTER:03d}'
            print(self.__staff_ID)
            self.__staff_ID = staff_ID
        else:
            staff_ID = f'ZooS.{self.name[0].capitalize()}{self.last_name[0].capitalize()}.{Staff.ID_COUNTER:03d}'

        self.__staff_ID = staff_ID
        self._qualifications = qualifications
        self.__remuneration = remuneration

        # Assigned team
        self.care_team: int

    def __str__(self):
        return (f'Staff ID= {self.__staff_ID}\n'
                f'{'=' * 25}\n'
                f'{super().__str__()}\n'
                f'{'=' * 25}\n'
                f'Qualification= {self._qualifications}\n'
                f'Remuneration= \x1B[3m{'Private, please contact HR'}\x1B[0m\n'
                )

    def __repr__(self):
        return f'Staff ID: {self.__staff_ID}, qualifications= {self._qualifications}, Remuneration= {self.__remuneration}'

    @property
    def staff_ID(self):
        """
        staff_id property
        :return: None
        """
        return self.__staff_ID

    @staff_ID.setter
    def staff_ID(self, value: None):
        """
        staff_ID setter
        :param value: None
        :return: ID returned
        """

        # Creating unique ID per staff
        if self.name is None or self.name == 0 or self.name == '':
            str_ = input(f'Your Name and Last Name can not be empty.\nA temporary'
                         f' ID number has been created.')
            staff_ID = f'ZooS.Temp_ID.{Staff.ID_COUNTER:03d}'
            print(self.__staff_ID)
            self.__staff_ID = staff_ID
        else:
            staff_ID = f'ZooS.{self.name[0].capitalize()}{self.last_name[0].capitalize()}.{Staff.ID_COUNTER:03d}'

    @property
    def qualifications(self) -> str:
        """
        qualifications property
        :return: None
        """
        return self._qualifications

    @qualifications.setter
    def qualifications(self, qualifications_: str) -> None:

        print('Staff Qualifications: ')
        self._qualifications = validation.dict_choice(staff_data.QUALIFICATIONS, qualifications_)
        print(f'Qualifications updated to {self._qualifications}\n')

    @property
    def remuneration(self) -> str:
        """
        remuneration property
        :return: None
        """
        return self.__remuneration

    @remuneration.setter
    def remuneration(self, _remuneration: str) -> None:

        # for testing only
        # self.__remuneration = validation.dict_choice(staff_data.REMUNERATION, _remuneration)

        # Update before release
        password_ = input('HR "protected", enter password to proceed: ')
        if password_ == 'Passw00rd':
            self.__salary = validation.dict_choice(staff_data.REMUNERATION, _remuneration)
            print(f'Remuneration updated to {self.__remuneration}\n')
        else:
            print(f'Sorry, wrong password. Contact HR.\n')

    def wants_to_work(self, value: str) -> None:

        value = validation.str_YN_val_uc(value)
        if value == 'Y':
            print('Staff wants to work!')
        else:
            print('Staff wants does not want to work! Buuuu')


#s1 = Staff('Tony', 'Stark','2000-01-05', 'G2', 'W1', 'Q3', 'R1')
#print(s1)

#print(type(s1))


