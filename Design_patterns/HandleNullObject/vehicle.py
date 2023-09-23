from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def getTankCapacity(self):
        pass
    
    @abstractmethod
    def getSeatingCapacity(self):
        pass