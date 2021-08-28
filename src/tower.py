from dataclasses import dataclass
from abc import ABC, abstractmethod
from .hardware import Assembly_Builder, Tangent_Assembly


@dataclass
class Tower(ABC):
    
    towerNumber: int = None 
    ahead: int = None


#    @property
#    @abstractmethod
#    def legs(self):
#        pass
#
#    @legs.setter
#    @abstractmethod
#    def legs(self, value):
#        pass
#
#    @property
#    @abstractmethod
#    def towerNumber(self):
#        pass
#
#    @towerNumber.setter
#    @abstractmethod
#    def towerNumber(self, value):
#        pass


# TODO make a basic tower class and then make tangent and DE inehrit
class Tangent(Tower):
    
#    def __init__(self, ahead=None, tower_type):
#        self.ahead = ahead
#        self.towerNumber = towerNumber
        #self.__hardware = hardware
        

    def __iter__(self):
        for item in self.__hardware:
            yield item
    
#    def __str__(self):
#        return f'{self.__hardware.shackle}'
            
    def add_hardware(self, number, hw_assm):
        hw = []
        for i in range(number + 1):
            hw.append(hw_assm)
        
        self.hardware = hw    
       
#    @property
#    def legs(self):
#        return self.__leg_type
#
#    @legs.setter
#    def legs(self, value):
#        self.__leg_type = value
#    
#    @property
#    def towerNumber(self):
#        return self.__tower_number
#
#    @towerNumber.setter
#    def towerNumber(self, value):
#        self.__tower_number = value

class DeadEnd(Tower):

#    def __init__(self, ahead=None):
#        self.ahead = ahead
        #self.__hardware = hardware
    
    def __iter__(self):
        for item in self.__hardware:
            yield item
    
#    def __str__(self):
#        return f'{self.__hardware.shackle}'
            
    def add_hardware(self, number, hw_assm):
        hw = []
        for i in range(number):
            hw.append(hw_assm)
        
        self.hardware = hw    
       
#    @property
#    def legs(self):
#        return self.__leg_type
#
#    @legs.setter
#    def legs(self, value):
#        self.__leg_type = value
#    
#    @property
#    def towerNumber(self):
#        return self.__tower_number
#
#    @towerNumber.setter
#    def towerNumber(self, value):
#        self.__tower_number = value

# TODO change legType to towerType
class TowerBuilder(object):
    @classmethod
    def createTower(cls, towerType, legType):
        t = towerType()
        t.legs = legType
        return t 

@dataclass
class IndividualTower(Tangent, DeadEnd):
    
    towerNumber: int = None
    towerType: Tower = None
        



