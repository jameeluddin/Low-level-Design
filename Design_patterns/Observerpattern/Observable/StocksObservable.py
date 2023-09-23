from abc import ABC, abstractmethod
from random import randrange
from typing import List


class StocksObservable(ABC):

    @abstractmethod
    def add(self, observor):
        pass

    @abstractmethod
    def remove(self, observor):
        pass

    @abstractmethod
    def notify_subscribers(self):
        pass

    @abstractmethod
    def set_stock_count(self, new_stock_added):
        pass

    @abstractmethod
    def get_stock_count(self):
        pass

    @abstractmethod
    def set_stock_count_to_zero(self):
        pass