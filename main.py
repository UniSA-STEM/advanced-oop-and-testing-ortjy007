'''
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
'''

# Question 1
# Provide your Helmet class below. It should work with the following Armor class:

from abc import ABC, abstractmethod

class Armour(ABC):
    def __init__(self, material, defence, toughness, durability):
        self.__material = material
        self.__defence = defence
        self.__toughness = toughness
        self.__durability = durability
        print('0')
        self.__protection = self.calculate_protection()

    @abstractmethod
    def calculate_protection(self):
        print('1')
        pass

    def reduce_durability(self, amount):
        print(amount)
        print('2')
        self.__durability -= amount
        if self.__durability < 0:
            self.__durability = 0
        self.__protection = self.calculate_protection()

    def repair(self, amount):
        self.__durability += amount

    def is_broken(self):
        return self.__durability == 0

    def get_defence(self):
        return self.__defence

    def get_toughness(self):
        return self.__toughness

    def get_durability(self):
        return self.__durability

    defence = property(get_defence)
    toughness = property(get_toughness)
    durability = property(get_durability)

    def __str__(self):
        return f"---{self.__material.upper()} {self.__class__.__name__.upper()}---\nDefence:{self.__defence}\n" \
               f"Toughness: {self.__toughness}\nDurability: {self.__durability}\n" \
               f"{self.__class__.__name__} protection = {self.__protection}\n"

# The armour class has been included to ensure you are testing the abstract methods.

class Helmet(Armour):

    def __init__(self, material, defence, toughness, durability):
        super().__init__(material,defence,toughness,durability)

    def calculate_protection(self):
        print('3')
        return self.toughness + self.__durability

helmet = Helmet("Steel", 100, 100, 50)
helmet.reduce_durability(100)
print(helmet)