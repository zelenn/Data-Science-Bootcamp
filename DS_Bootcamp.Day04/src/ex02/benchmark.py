#!/usr/bin/env python3
import timeit
import sys

def get_emails():
    base_emails = [
        'john@gmail.com',
        'james@gmail.com',
        'alice@yahoo.com',
        'anna@live.com',
        'philipp@gmail.com'
    ]
    return base_emails * 5

def get_gmails_loop(emails):
    gmails = []
    for e in emails:
        if e.endswith("@gmail.com"):
            gmails.append(e)
    return gmails

def get_gmails_comprehension(emails):
    return [e for e in emails if e.endswith("@gmail.com")]

def get_gmails_map(emails):
    mapped = map(lambda e: e if e.endswith("@gmail.com") else None, emails)
    return [x for x in mapped if x is not None]

def get_gmails_filter(emails):
    return list(filter(lambda e: e.endswith("@gmail.com"), emails))

def benchmark(func_name, number):
    """
    замеряет время выполнения выбранной функции
    """
    stmt_map = {
        'loop': "get_gmails_loop(emails)",
        'list_comprehension': "get_gmails_comprehension(emails)",
        'map': "get_gmails_map(emails)",
        'filter': "get_gmails_filter(emails)"
    }
    
    if func_name not in stmt_map:
        raise ValueError("Unknown function name")
    
    setup_code = f"""
from {__name__} import get_gmails_loop, get_gmails_comprehension, get_gmails_map, get_gmails_filter, get_emails
emails = get_emails()
"""
    t = timeit.timeit(stmt_map[func_name], setup=setup_code, number=number)
    return t


def main():
    args = sys.argv[1:]
    if len(args) == 2:
        func_name = args[0]
        number = int(args[1])
        print(benchmark(func_name, number))
    else:
        # если аргументы не заданы — сравниваем все варианты.
        number = 10000#000
        variants = ['loop', 'list_comprehension', 'map', 'filter']
        results = []
        for v in variants:
            t = benchmark(v, number)
            results.append((v, t))
        # сортируем результаты по времени (от меньшего к большему)
        results.sort(key=lambda x: x[1])
        for v, t in results:
            print(f"{v}: {t}")

if __name__ == '__main__':
    main()
