from abc import ABC, abstractmethod


class CommandExecutor(ABC):
    def __init__(self, parking_lot_service, output_printer):
        self.parking_lot_service = parking_lot_service
        self.output_printer = output_printer

    @abstractmethod
    def validate(self, command):
        pass

    @abstractmethod
    def execute(self, command):
        pass
