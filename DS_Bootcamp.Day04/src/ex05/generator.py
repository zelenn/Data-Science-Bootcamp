#!/usr/bin/env python3
import sys
import resource

def read_file_generator(path):
    """
    генератор который читает файл построчно.
    """
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            yield line

def main():
    if len(sys.argv) < 2:
        print("Usage: python generator.py <path_to_file>")
        sys.exit(1)
    
    path = sys.argv[1]
    
    line_generator = read_file_generator(path)
    
    for line in line_generator:
        pass

    usage = resource.getrusage(resource.RUSAGE_SELF)
    peak_memory_kb = usage.ru_maxrss
    peak_memory_gb = peak_memory_kb / (1024 * 1024)
    cpu_time = usage.ru_utime + usage.ru_stime

    print("Peak Memory Usage = {:.3f} GB".format(peak_memory_gb))
    print("User Mode Time + System Mode Time = {:.2f}s".format(cpu_time))

if __name__ == '__main__':
    main()
