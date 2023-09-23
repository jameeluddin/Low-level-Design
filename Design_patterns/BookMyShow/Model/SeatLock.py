from dataclasses import dataclass
from datetime import datetime, timedelta
from .Seat import Seat
from .Show import Show

@dataclass
class SeatLock:
    seat: Seat
    show: Show
    timeout_in_seconds: int
    lock_time: datetime
    locked_by: str

    def is_lock_expired(self):
        lock_instant = self.lock_time + timedelta(seconds=self.timeout_in_seconds)
        current_instant = datetime.now()
        return lock_instant < current_instant
