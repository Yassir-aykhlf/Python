import sys
import time
import tracemalloc

def range_gen(start, stop, step=1):
    if step == 0:
        raise ValueError("step must not be zero")
    current = start
    if step > 0:
        while current < stop:
            yield current
            current += step
    else:
        while current > stop:
            yield current
            current += step

def countdown_gen(n):
    while n >= 0:
        yield n
        n -= 1