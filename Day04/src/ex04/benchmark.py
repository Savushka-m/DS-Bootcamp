#!/usr/bin/env python3
import timeit
import random
from collections import Counter

def my_function(sp):
    dct = {i: 0 for i in range(101)}
    for i in sp:
        dct[i] += 1
    return dct

def top_10_my_function(sp):
    dct = my_function(sp)
    top_10 = sorted(dct.items(), key=lambda x: x[1], reverse=True)[:10]
    return top_10

def Counter_function(sp):
    dct = Counter(sp)
    return dct

def top_10_Counter_function(sp):
    dct = Counter_function(sp)
    top_10 = dct.most_common(10)
    return top_10
    
if __name__ == '__main__':
    setup_code = """
import random
from __main__ import my_function, top_10_my_function, Counter_function, top_10_Counter_function
sp = [random.randint(0, 100) for i in range(1_000_000)]
    """
    time = timeit.timeit(setup = setup_code, stmt = "my_function(sp)", number = 1)
    print(f"my function: {time}")
    time = timeit.timeit(setup = setup_code, stmt = "top_10_my_function(sp)", number = 1)
    print(f"Counter: {time}")
    time = timeit.timeit(setup = setup_code, stmt = "Counter_function(sp)", number = 1)
    print(f"my top: {time}")
    time = timeit.timeit(setup = setup_code, stmt = "top_10_Counter_function(sp)", number = 1)
    print(f"Counter's top: {time}")