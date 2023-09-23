from .car import Car
from .slot import Slot
from ..exception.exceptions import ParkingLotException, InvalidSlotException, SlotAlreadyOccupiedException


class ParkingLot:
    MAX_CAPACITY = 100000

    def __init__(self, capacity):
        if capacity > self.MAX_CAPACITY or capacity <= 0:
            raise ParkingLotException("Invalid capacity given for parking lot.")

        self.capacity = capacity
        self.slots = {}

    def get_capacity(self):
        return self.capacity

    def get_slots(self):
        return self.slots

    def get_slot(self, slot_number):
        if slot_number > self.capacity or slot_number <= 0:
            raise InvalidSlotException()

        if slot_number not in self.slots:
            self.slots[slot_number] = Slot(slot_number)

        return self.slots[slot_number]

    def park(self, car, slot_number):
        slot = self.get_slot(slot_number)
        if not slot.is_slot_free():
            raise SlotAlreadyOccupiedException()

        slot.assign_car(car)
        return slot

    def make_slot_free(self, slot_number):
        slot = self.get_slot(slot_number)
        slot.unassign_car()
        return slot
