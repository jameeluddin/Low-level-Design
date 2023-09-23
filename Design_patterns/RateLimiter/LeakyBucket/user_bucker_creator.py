from Design_patterns.RateLimiter.LeakyBucket.leaky_bucket import LeakyBucket
import threading


class UserBucketCreator:
    def __init__(self, id):
        self.bucket = {id: LeakyBucket(10)}

    def access_application(self, thread_id, id):
        if self.bucket.get(id).grant_access():
            print(f"{thread_id} -> able to access the application")
        else:
            print(f"{thread_id} -> Too many requests, Please try after some time")
