from .parking_strategy import ParkingStrategy
from ...exception.exceptions import NoFreeSlotAvailableException


class NaturalOrderingParkingStrategy(ParkingStrategy):
    def __init__(self):
        self.slot_set = set()
        self.current_slot = 1

    def add_slot(self, slot_number):
        self.slot_set.add(slot_number)

    def remove_slot(self, slot_number):
        self.slot_set.discard(slot_number)

    def get_next_slot(self):
        if not self.slot_set:
            raise NoFreeSlotAvailableException()

        next_slot = self.current_slot
        while next_slot in self.slot_set:
            next_slot += 1

        return min(self.slot_set)
