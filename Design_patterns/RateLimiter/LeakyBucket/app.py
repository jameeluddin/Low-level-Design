import threading
from concurrent.futures.thread import ThreadPoolExecutor
from Design_patterns.RateLimiter.LeakyBucket.user_bucker_creator import UserBucketCreator


def main():
    leaky_bucket = UserBucketCreator(1)
    threads = []

    for i in range(12):
        thread = threading.Thread(target=leaky_bucket.access_application, args=(i + 1, 1))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("All threads have finished.")


if __name__ == "__main__":
    main()
