#!/usr/bin/env python3
import timeit
import sys

def loop_function(emails):
    a = []
    for i in emails:
        if i[-10:] == "@gmail.com":
            a.append(i)
    return a

def list_comprehension_function(emails):
    a = [i for i in emails if i[-10:] == "@gmail.com"]
    return a

def map_function(emails):
    a = list(map(lambda x: x if x[-10:] == "@gmail.com" else None, emails))
    return a

def filter_function(emails):
    a = list(filter(lambda x: x[-10:] == "@gmail.com", emails))
    return a

def benchmark(name, calls):
    try:
        calls = int(calls)
    except:
        raise Exception("Введите корректное число вызовов")
    if name not in ["loop", "list_comprehension", "map", "filter"]:
        raise Exception("Введите корректное название функции")
    setup_code = """
from __main__ import loop_function, list_comprehension_function, map_function, filter_function
emails = ["john@gmail.com", "james@gmail.com", "alice@yahoo.com", "anna@live.com", "philipp@gmail.com"] * 5
    """
    time = timeit.timeit(setup = setup_code, stmt = f"{name}_function(emails)", number = calls)
    print(time)
    
if __name__ == '__main__':
    if len(sys.argv) == 3:
        benchmark(sys.argv[1], sys.argv[2])