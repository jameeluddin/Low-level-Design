from .car import Car


class Slot:
    def __init__(self, slot_number):
        self.slot_number = slot_number
        self.parked_car = None

    def get_slot_number(self):
        return self.slot_number

    def get_parked_car(self):
        return self.parked_car

    def is_slot_free(self):
        return self.parked_car is None

    def assign_car(self, car):
        self.parked_car = car

    def unassign_car(self):
        self.parked_car = None
