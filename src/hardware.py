from abc import ABC, abstractmethod

class Assembly(ABC):
    @property
    @abstractmethod
    def shackle(self):
        pass
    
    @shackle.setter
    @property
    def shackle(self):
        pass

    @property
    @abstractmethod
    def insulator(self):
        pass

    @insulator.setter
    @property
    def insulator(self):
        pass
    
    @property
    @abstractmethod
    def clevis(self):
        pass

    @clevis.setter
    @property
    def clevis(self):
        pass

    @property
    @abstractmethod
    def clamp(self):
        pass
    
    @clamp.setter
    @property
    def clamp(self):
        pass

class Tangent_Assembly(Assembly):
    
    def __init__(self, tower_number=None):
        self.__tower_number = tower_number

    @property
    def shackle(self):
        return self.__shackle

    @shackle.setter
    def shackle(self, value):
        self.__shackle = value

    @property
    def insulator(self):
        return self.__insulator

    @insulator.setter
    def insulator(self, value):
        self.__insulator = value

    @property
    def clevis(self):
        return self.__clevis

    @clevis.setter
    def clevis(self, value):
        self.__clevis = value

    @property
    def clamp(self):
        return self.__clamp
    
    @clamp.setter
    def clamp(self, value):
        self.__clamp = value


class DeadEnd_Assembly(Assembly):

    def __init__(self, tower_number=None):
        self.__tower_number = tower_number

    @property
    def shackle(self):
        return self.__shackle

    @shackle.setter
    def shackle(self, value):
        self.__shackle = value
        

    @property
    def insulator(self):
        return self.__insulator

    @insulator.setter
    def insulator(self, value):
        self.__insulator = value

    @property
    def clevis(self):
        return self.__clevis

    @clevis.setter
    def clevis(self, value):
        self.__clevis = value

    @property
    def clamp(self):
        return self.__clamp
    
    @clamp.setter
    def clamp(self, value):
        self.__clamp = value

class Assembly_Builder(object):
    @classmethod
    def createAssembly(cls, assemblyType):
        a = assemblyType()
        return a





'''www.preformed.com/vn/energy/transmission/string-assemblies-hardware/string-assemblies/single-twin-conductor-tangent-suspensions/i-string-assembly-tangent-suspension-twin-bundle-conductor-25k'''
