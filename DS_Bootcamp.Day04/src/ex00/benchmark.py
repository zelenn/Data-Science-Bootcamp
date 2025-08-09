#!/usr/bin/env python3

import timeit

def get_emails():
    return [
        'john@gmail.com',
        'james@gmail.com',
        'alice@yahoo.com',
        'anna@live.com',
        'philipp@gmail.com'
    ] * 5

def get_gmails_loop(emails):
    gmails = []
    for e in emails:
        if e.endswith("@gmail.com"):
            gmails.append(e)
    return gmails

def get_gmails_comprehension(emails):
    return [e for e in emails if e.endswith("@gmail.com")]

def main():
    number_of_calls = 90000#000
    setup_code = """
from __main__ import get_gmails_loop, get_gmails_comprehension, get_emails
EMAILS = get_emails()
"""
    time_loop = timeit.timeit(
        "get_gmails_loop(EMAILS)",
        setup=setup_code,
        number=number_of_calls
    )

    time_list_comp = timeit.timeit(
        "get_gmails_comprehension(EMAILS)",
        setup=setup_code,
        number=number_of_calls
    )

    if time_list_comp <= time_loop:
        print("it is better to use a list comprehension")
    else:
        print("it is better to use a loop")

    sorted_times = sorted([time_loop, time_list_comp])
    print(f"{sorted_times[0]} vs {sorted_times[1]}")

if __name__ == '__main__':
    main()
