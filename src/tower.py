from abc import ABC, abstractmethod

class Tower(ABC):
    @property
    @abstractmethod
    def legs(self):
        pass

    @legs.setter
    @abstractmethod
    def legs(self, value):
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
    
    def __init__(self):
        pass
        
    @property
    def legs(self):
        return self.__leg_type

    @legs.setter
    def legs(self, value):
        self.__leg_type = value
    
    @property
    def towerNumber(self):
        return self.__tower_number

    @towerNumber.setter
    def towerNumber(self, value):
        self.__tower_number = value

class DeadEnd(Tower):

    def __init__(self):
       pass

    @property
    def legs(self):
        return self.__leg_type

    @legs.setter
    def legs(self, value):
        self.__leg_type = value

    @property
    def towerNumber(self):
        return self.__tower_number

    @towerNumber.setter
    def towerNumber(self, value):
        self.__tower_number = value

class TowerBuilder(object):
    @classmethod
    def createTower(cls, towerType, tower_number, legType):
        t = towerType()
        t.tower_number = tower_number
        t.legs = legType
        return t 
    
#    def createTower(self, towerType, tower_number, legType):
#        return towerType(tower_number).legs(legType)


