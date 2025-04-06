#!/usr/bin/env python3
import timeit

def loop(emails):
    a = []
    for i in emails:
        if i[-10:] == "@gmail.com":
            a.append(i)
    return a

def list_comprehension(emails):
    a = [i for i in emails if i[-10:] == "@gmail.com"]
    return a

def map_function(emails):
    a = list(map(lambda x: x if x[-10:] == "@gmail.com" else None, emails))
    return a


if __name__ == '__main__':
    setup_code = """
from __main__ import loop, list_comprehension, map_function
emails = ["john@gmail.com", "james@gmail.com", "alice@yahoo.com", "anna@live.com", "philipp@gmail.com"] * 5
    """
    loop_time = timeit.timeit(setup = setup_code, stmt = "loop(emails)", number = 90_000_000)
    list_comprehension_time = timeit.timeit(setup = setup_code, stmt = "list_comprehension(emails)", number = 90_000_000)
    map_function_time = timeit.timeit(setup = setup_code, stmt = "map_function(emails)", number = 90_000_000)
    time = [loop_time, list_comprehension_time, map_function_time]
    time.sort()
    if list_comprehension_time == min(time):
        print("It is better to use a list comprehension")
        print(f"{time[0]} vs {time[1]} vs {time[2]}")
    elif loop == min(time):
        print("It is better to use a loop")
        print(f"{time[0]} vs {time[1]} vs {time[2]}")
    else:
        print("It is better to use a map")
        print(f"{time[0]} vs {time[1]} vs {time[2]}")
