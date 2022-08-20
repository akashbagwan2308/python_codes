# function caching

import time
from functools import lru_cache

@lru_cache(maxsize=3)
def some_work(n):
    # some task take n seconds
    time.sleep(n)
    return n

if __name__ == '__main__':
    print("Now running some work")
    some_work(3)
    print("Done... Calling again")
    some_work(3)
    print("Called Again")