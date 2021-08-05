from abc import ABC, abstractmethod

class Tower(ABC):
    @abstractmethod
    def legs(self):
        pass

    @property
    @abstractmethod
    def towerNumber(self):
        pass

    @towerNumber.setter
    @abstractmethod
    def towerNumber(self, value):
        pass

class Tangent(Tower):
    
    def __init__(self, tower_number):
        self.__tower_number = tower_number

    def legs(self, legType):
        print(f'Tangent leg type {legType} is created')
    
    @property
    def towerNumber(self):
        return self.__tower_number

    @towerNumber.setter
    def towerNumber(self, value):
        self.__tower_number = value

class DeadEnd(Tower):

    def __init__(self, tower_number):
        self.__tower_number = tower_number

    def legs(self, legType):
        print(f'DeadEnd leg type {legType} is created')

    @property
    def towerNumber(self):
        return self.__tower_number

    @towerNumber.setter
    def towerNumber(self, value):
        self.__tower_number = value

class TowerBuilder(object):
    @classmethod
    def createTower(cls, towerType, legType, tower_number):
        return towerType(tower_number).legs(legType)
