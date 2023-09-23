from abc import ABC, abstractmethod


class ParkingStrategy(ABC):
    """
    Strategy interface for deciding how slots will be used to park the car.
    """

    @abstractmethod
    def add_slot(self, slot_number):
        """
        Add a new slot to the parking strategy. After adding, this new slot will become available for future parkings.

        :param slot_number: Slot number to be added.
        """
        pass

    @abstractmethod
    def remove_slot(self, slot_number):
        """
        Removes a slot from the parking strategy. After removing, this slot will not be used for future parkings.

        :param slot_number: Slot number to be removed.
        """
        pass

    @abstractmethod
    def get_next_slot(self):
        """
        Get the next free slot as per the parking strategy.

        :return: Next free slot number.
        """
        pass
