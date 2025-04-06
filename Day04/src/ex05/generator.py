#!/usr/bin/env python3
import resource
import sys

def read_return(path):
    try:
        with open(path, 'r') as file:
            for line in file:
                yield line
    except:
        print("Произошла ошибка при открытии файла")

if __name__ == '__main__':
    if len(sys.argv) == 2:
        file = read_return(sys.argv[1])
        for line in file:
            pass
        usage = resource.getrusage(resource.RUSAGE_SELF)
        peak_memory_usage = usage.ru_maxrss / (1024**2)
        user_time = usage.ru_utime
        system_time = usage.ru_stime
        print(f"Peak Memory Usage = {peak_memory_usage} GB")
        print(f"User Mode Time + System Mode Time = {user_time+system_time}s")
    else:
        print("Неверное число аргументов")