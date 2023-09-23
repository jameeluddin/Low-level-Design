from abc import ABC
from queue import Queue
from Design_patterns.RateLimiter.rate_limiter import RateLimiter


class LeakyBucket(RateLimiter):
    def __init__(self, capacity):
        self.queue = Queue(maxsize=capacity)

    def grant_access(self):
        if not self.queue.full():
            self.queue.put(1)
            return True
        return False
