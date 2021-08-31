from dataclasses import dataclass
from abc import ABC, abstractmethod
from .hardware import Assembly_Builder, Tangent_Assembly


@dataclass
class Tower(ABC):
    
    towerNumber: int = None 
    ahead: int = None

    @abstractmethod
    def add_hardware(self, number, hw_assm):
        '''add hardware assembly'''

class Tangent(Tower):
    
    def add_hardware(self, number, hw_assm):
        hw = []
        for i in range(number + 1):
            hw.append(hw_assm)
        
        self.hardware = hw    
       
class DeadEnd(Tower):

    def add_hardware(self, number, hw_assm):
        hw = []
        for i in range(number):
            hw.append(hw_assm)
        
        self.hardware = hw    
       
# TODO change legType to towerType
class TowerBuilder(object):
    @classmethod
    def createTower(cls, towerType, legType):
        t = towerType()
        t.legs = legType
        return t 

class Tline:    

    def __init__(self):
        self.head = IndividualTower()
        self.line_name = None

    def addTower(self, data):
        new_node = data
        cur = self.head 
        while cur.nextTower != None:
            cur = cur.nextTower
        cur.nextTower = IndividualTower()     


@dataclass
class IndividualTower(Tangent, DeadEnd):
    
    towerNumber: int = None
    towerType: Tower = None
    nextTower: Tower = None
        



