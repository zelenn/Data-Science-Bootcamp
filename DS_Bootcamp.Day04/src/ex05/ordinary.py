#!/usr/bin/env python3
import sys
import resource

def read_file_into_list(path):
    """
    читает весь файл по указанному пути в список строк.
    """
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return lines

def main():
    if len(sys.argv) < 2:
        print("Usage: python ordinary.py <path_to_file>")
        sys.exit(1)
    
    path = sys.argv[1]
    
    lines = read_file_into_list(path)
    
    for line in lines:
        pass

    usage = resource.getrusage(resource.RUSAGE_SELF)
    peak_memory_kb = usage.ru_maxrss
    peak_memory_gb = peak_memory_kb / (1024 * 1024)
    cpu_time = usage.ru_utime + usage.ru_stime

    print("Peak Memory Usage = {:.3f} GB".format(peak_memory_gb))
    print("User Mode Time + System Mode Time = {:.2f}s".format(cpu_time))

if __name__ == '__main__':
    main()
