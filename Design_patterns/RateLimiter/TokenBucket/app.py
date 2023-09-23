import threading
import time

from Design_patterns.RateLimiter.TokenBucket.token_bucket import TokenBucket


def thread_function(thread_id, token_bucket):
    if token_bucket.grant_access():
        print(f"Thread {thread_id} - Access Granted")
    else:
        print(f"Thread {thread_id} - Access Denied")
    time.sleep(1)  # Sleep for 1 second


def main():
    token_bucket = TokenBucket(bucket_capacity=1, refresh_rate=2)
    threads = []

    for i in range(12):
        thread = threading.Thread(target=thread_function, args=(i + 1, token_bucket))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("All threads have finished.")


if __name__ == "__main__":
    main()
