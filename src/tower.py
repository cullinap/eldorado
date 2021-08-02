
from abc import ABC, abstractmethod

class Tower(ABC):
    @abstractmethod
    def legs(self):
        pass

class Tangent(Tower):
    def legs(self, legType):
        print(f'Tangent leg type {legType} is created')

class DeadEnd(Tower):
    def legs(self, legType):
        print(f'DeadEnd leg type {legType} is created')

class TowerBuilder(object):
    @classmethod
    def createTower(cls, towerType, legType):
        return towerType().legs(legType)
