#!/usr/bin/env python3
import timeit

def loop(emails):
    a = []
    for i in emails:
        if i[-10] == "@gmail.com":
            a.append(i)
    return a

def list_comprehension(emails):
    a = [i for i in emails if i[-10] == "@gmail.com"]
    return a


if __name__ == '__main__':
    setup_code = """
from __main__ import loop, list_comprehension
emails = ["john@gmail.com", "james@gmail.com", "alice@yahoo.com", "anna@live.com", "philipp@gmail.com"] * 5
    """
    loop_time = timeit.timeit(setup = setup_code, stmt = "loop(emails)", number = 90_000_000)
    list_comprehension_time = timeit.timeit(setup = setup_code, stmt = "list_comprehension(emails)", number = 90_000_000)
    if loop_time > list_comprehension_time:
        print("It is better to use a list comprehension")
        print(f"{list_comprehension_time} vs {loop_time}")
    else:
        print("It is better to use a loop")
        print(f"{loop_time} vs {list_comprehension_time}")