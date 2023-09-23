from collections import OrderedDict

from Design_patterns.parkingLot.exception.exceptions import ParkingLotException


class ParkingLotService:
    def __init__(self):
        self.parking_lot = None
        self.parking_strategy = None

    def create_parking_lot(self, parking_lot, parking_strategy):
        if self.parking_lot is not None:
            raise ParkingLotException("Parking lot already exists.")

        self.parking_lot = parking_lot
        self.parking_strategy = parking_strategy

        for i in range(1, parking_lot.capacity + 1):
            parking_strategy.add_slot(i)

    def park(self, car):
        self.validate_parking_lot_exists()
        next_free_slot = self.parking_strategy.get_next_slot()
        self.parking_lot.park(car, next_free_slot)
        self.parking_strategy.remove_slot(next_free_slot)
        return next_free_slot

    def make_slot_free(self, slot_number):
        self.validate_parking_lot_exists()
        self.parking_lot.make_slot_free(slot_number)
        self.parking_strategy.add_slot(slot_number)

    def get_occupied_slots(self):
        self.validate_parking_lot_exists()
        occupied_slots_list = []
        all_slots = self.parking_lot.get_slots()

        for i in range(1, self.parking_lot.capacity + 1):
            if i in all_slots:
                slot = all_slots[i]
                if not slot.is_slot_free():
                    occupied_slots_list.append(slot)

        return occupied_slots_list

    def validate_parking_lot_exists(self):
        if self.parking_lot is None:
            raise ParkingLotException("Parking lot does not exist to park.")

    def get_slots_for_color(self, color):
        occupied_slots = self.get_occupied_slots()
        return [slot for slot in occupied_slots if slot.parked_car.color == color]

