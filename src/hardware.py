from abc import ABC, abstractmethod

class Assembly(ABC):
    @property
    @abstractmethod
    def clamp(self):
        pass
    
    @clamp.setter
    @property
    def clamp(self):
        pass


class Tangent_Assembly(Assembly):
    
    def __init__(self, tower_number):
        self.__tower_number = tower_number

    @property
    def clamp(self):
        return self.__clamp
    
    @clamp.setter
    def clamp(self, value):
        self.__clamp = value





