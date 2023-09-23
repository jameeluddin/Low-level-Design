from abc import ABC, abstractmethod


class WeightMachineAdapter(ABC):
    @abstractmethod
    def get_weight_in_kg(self):
        pass