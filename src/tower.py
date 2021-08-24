from abc import ABC, abstractmethod
from .hardware import Assembly_Builder, Tangent_Assembly

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

class Tangent(Tower, Assembly_Builder):
    
    def __init__(self, ahead=None):
        self.ahead = ahead
        #self.__hardware = hardware
    
    def __iter__(self):
        for item in self.__hardware:
            yield item
    
    def __str__(self):
        return f'{self.__hardware.shackle}'
            
    def create_I_string(self):
        return  Assembly_Builder.createAssembly(Tangent_Assembly) 

    def add_hardware(self, number, hw_assm):
        hw = []
        for i in range(number):
            hw.append(hw_assm)
        
        self.hardware = hw    
       
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

    def __init__(self, ahead=None, hardware=None):
       self.ahead = ahead
       self.hardware = hardware

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


