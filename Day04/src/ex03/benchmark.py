#!/usr/bin/env python3
import timeit
import sys
from functools import reduce

def loop_function(number):
    sum = 0
    for i in range(1, number + 1):
        sum += i * i
    return sum

def reduce_function(number):
    sum = reduce(lambda x, y: x + y*y, [i for i in range(number+1)])
    return sum

def benchmark(name, calls, number):
    try:
        calls = int(calls)
        number = int(number)
    except:
        raise Exception("Введите корректное число")
    if name not in ["loop", "reduce"]:
        raise Exception("Введите корректное название функции")
    setup_code = """
from __main__ import loop_function, reduce_function
    """
    time = timeit.timeit(setup = setup_code, stmt = f"{name}_function({number})", number = calls)
    print(time)
    
if __name__ == '__main__':
    if len(sys.argv) == 4:
        benchmark(sys.argv[1], sys.argv[2], sys.argv[3])