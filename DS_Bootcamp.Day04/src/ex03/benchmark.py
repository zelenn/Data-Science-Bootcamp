#!/usr/bin/env python3
import timeit
import sys
from functools import reduce

def add_square(acc, x):
    return acc + x * x

def sum_squares_loop(n):
    total = 0
    for i in range(1, n + 1):
        total = add_square(total, i)
    return total

def sum_squares_reduce(n):
    return reduce(add_square, range(1, n + 1), 0)

def benchmark(func_name, number, n):
    stmt_map = {
        'loop': "sum_squares_loop(num)",
        'reduce': "sum_squares_reduce(num)"
    }
    if func_name not in stmt_map:
        raise ValueError("Unknown function name")
    
    setup_code = f"""
from {__name__} import sum_squares_loop, sum_squares_reduce
num = {n}
"""
    t = timeit.timeit(stmt_map[func_name], setup=setup_code, number=number)
    return t

def main():
    args = sys.argv[1:]
    if len(args) == 3:
        func_name = args[0]
        number = int(args[1])
        n = int(args[2])
        print(benchmark(func_name, number, n))
    else:
        print("Usage: ./benchmark.py <loop|reduce> <number_of_calls> <n>")

if __name__ == '__main__':
    main()
