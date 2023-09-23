from abc import ABC, abstractmethod


class EmployeeDao(ABC):

    @abstractmethod
    def create(self, client, obj):
        pass

    @abstractmethod
    def delete(self, client, empid):
        pass

    @abstractmethod
    def get(self, client, empid):
        pass
