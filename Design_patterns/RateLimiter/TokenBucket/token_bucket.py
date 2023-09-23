import threading
import time

class TokenBucket:
    def __init__(self, bucket_capacity, refresh_rate):
        self.bucket_capacity = bucket_capacity
        self.refresh_rate = refresh_rate
        self.current_capacity = bucket_capacity
        self.last_updated_time = int(time.time() * 1000)

    def grant_access(self):
        self.refresh_bucket()
        if self.current_capacity > 0:
            self.current_capacity -= 1
            return True
        return False

    def refresh_bucket(self):
        current_time = int(time.time() * 1000)
        time_difference = current_time - self.last_updated_time
        additional_tokens = int((time_difference / 1000) * self.refresh_rate)
        current_capacity = min(self.current_capacity + additional_tokens, self.bucket_capacity)
        self.current_capacity = current_capacity
        self.last_updated_time = current_time

