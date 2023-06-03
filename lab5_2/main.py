# Zbadaj przyspieszenie związane z zastosowaniem pamięci podręcznej
# na wybranych przykładzie funkcji rekurencyjnej (np. ciągu _Fibonacciego_).

import time
from functools import lru_cache, cached_property
import matplotlib.pyplot as plt


@cached_property
def fib_result():
    return fib(5)


@lru_cache(maxsize=100)
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def fib_no_cache(n):
    if n < 2:
        return n
    else:
        return fib_no_cache(n - 1) + fib_no_cache(n - 2)


def time_execution(f, arg):
    start = time.time()
    f(arg)
    end = time.time()
    return end - start


if __name__ == '__main__':

    ''' To compare the difference in execution time between the two functions, 
        I have plotted the execution time of each function'''

    # Run functions
    values = list(range(1, 100))
    fib_times = [time_execution(fib, n) for n in values]
    fib_no_cache_times = [time_execution(fib_no_cache, n) for n in values]

    # Plot results
    plt.figure(figsize=(8, 6))
    plt.bar(values, fib_times, label='Fibonacci - with caching')
    plt.bar(values, fib_no_cache_times, label='Fibonacci - no caching')
    plt.xlabel('Value of n')
    plt.ylabel('Execution Time')
    plt.title('Comparison of execution time between Fibonacci functions')
    plt.legend()
    plt.show()
