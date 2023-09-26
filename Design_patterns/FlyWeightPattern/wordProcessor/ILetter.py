from abc import ABC, abstractmethod


class ILetter(ABC):

    @abstractmethod
    def display(self, row, col):
        pass