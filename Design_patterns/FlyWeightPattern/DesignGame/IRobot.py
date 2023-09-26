from abc import ABC, abstractmethod


class IRobot(ABC):
    
    @abstractmethod
    def display(self, x, y):
        pass
