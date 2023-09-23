from datetime import datetime, timedelta
from Design_patterns.BookMyShow.Exceptions.SeatTemporaryUnavailableException import SeatTemporaryUnavailableException
from Design_patterns.BookMyShow.Model.SeatLock import SeatLock


class InMemorySeatLockProvider:

    def __init__(self, lock_timeout):
        self.lock_timeout = lock_timeout
        self.locks = {}

    def lock_seats(self, show, seats, user):
        for seat in seats:
            if self.is_seat_locked(show, seat):
                raise SeatTemporaryUnavailableException()

        for seat in seats:
            self.lock_seat(show, seat, user, self.lock_timeout)

    def unlock_seats(self, show, seats, user):
        for seat in seats:
            if self.validate_lock(show, seat, user):
                self.unlock_seat(show, seat)

    def validate_lock(self, show, seat, user):
        if show in self.locks and seat in self.locks[show]:
            return self.locks[show][seat].locked_by == user
        return False

    def get_locked_seats(self, show):
        print("31", self.locks)
        print("32", show)
        if self.locks.get(show):
            locked_seats = [seat for seat in self.locks[show] if not self.locks[show][seat].is_lock_expired()]
            return locked_seats
        return tuple()

    def unlock_seat(self, show, seat):
        if show in self.locks:
            self.locks[show].pop(seat, None)

    def lock_seat(self, show, seat, user, timeout_in_seconds):
        if show not in self.locks:
            self.locks[show] = {}

        lock_time = datetime.now()
        lock = SeatLock(seat, show, timeout_in_seconds, lock_time, user)
        self.locks[show][seat] = lock

    def is_seat_locked(self, show, seat):
        if show in self.locks and seat in self.locks[show]:
            return not self.locks[show][seat].is_lock_expired()
        return False

