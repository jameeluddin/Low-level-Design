import threading
import time
from queue import Queue


class SlidingWindow:
    def __init__(self, time_window_in_seconds, bucket_capacity):
        self.time_window_in_seconds = time_window_in_seconds
        self.bucket_capacity = bucket_capacity
        self.sliding_window = Queue()

    def grant_access(self):
        current_time = int(time.time() * 1000)
        self.check_and_update_queue(current_time)
        if self.sliding_window.qsize() < self.bucket_capacity:
            self.sliding_window.put(current_time)
            return True
        return False

    def check_and_update_queue(self, current_time):
        while not self.sliding_window.empty():
            calculated_time = (current_time - self.sliding_window.queue[0]) / 1000
            if calculated_time >= self.time_window_in_seconds:
                self.sliding_window.get()
            else:
                break
