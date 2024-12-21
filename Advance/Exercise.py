import timeit
from functools import cache

def fibonacci_no_cache(n):
    if n <= 2:
        return n
    return fibonacci_no_cache(n - 1) + fibonacci_no_cache(n - 2)

@cache
def fibonacci_cache(n):
    if n <= 2:
        return n
    return fibonacci_cache(n - 1) + fibonacci_cache(n - 2)

def measure_time():
    n = 40
    no_cache_time = timeit.timeit(lambda: fibonacci_no_cache(n), number=1)
    cache_time = timeit.timeit(lambda: fibonacci_cache(n), number=1)

    print(f"Execution time without cache: {no_cache_time:4f} seconds")
    print(f"Execution time with cache: {cache_time:10f} seconds")

if __name__ == "__main__":
    measure_time()    