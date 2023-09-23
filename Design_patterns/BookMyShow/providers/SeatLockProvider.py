from abc import ABC, abstractmethod


class SeatLockProvider(ABC):

    @abstractmethod
    def lock_seats(self, show, seats, user):
        pass

    @abstractmethod
    def unlock_seats(self, show, seats, user):
        pass

    @abstractmethod
    def validate_lock(self, show, seat, user):
        pass

    @abstractmethod
    def get_locked_seats(self, show):
        pass
