from abc import ABC, abstractmethod

class Assembly(ABC):
    @property
    @abstractmethod
    def assembly_type(self):
        pass

class Tangent_Assembly(Assembly):
    
    def __init__(self, tower_number):
        self.__tower_number = tower_number





