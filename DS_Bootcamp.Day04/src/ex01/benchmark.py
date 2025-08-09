#!/usr/bin/env python3
import timeit

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
    mapped = map(
        lambda e: e if e.endswith('@gmail.com') else None,
        emails
    )
    return [x for x in mapped if x is not None]

def main():
    number_of_calls = 900000#00

    setup_code = """
from __main__ import get_gmails_loop, get_gmails_comprehension, get_gmails_map, get_emails
emails = get_emails()
"""

    # засекаем время для loop
    time_loop = timeit.timeit(
        "get_gmails_loop(emails)",
        setup=setup_code,
        number=number_of_calls
    )

    # засекаем время для list comprehension
    time_list_comp = timeit.timeit(
        "get_gmails_comprehension(emails)",
        setup=setup_code,
        number=number_of_calls
    )

    # засекаем время для map
    time_map = timeit.timeit(
        "get_gmails_map(emails)",
        setup=setup_code,
        number=number_of_calls
    )

    # определяем, какая функция быстрее
    min_time = min(time_loop, time_list_comp, time_map)
    if min_time == time_loop:
        print("it is better to use a loop")
    elif min_time == time_list_comp:
        print("it is better to use a list comprehension")
    else:
        print("it is better to use a map")

    # выводим все три времени по возр
    sorted_times = sorted([time_loop, time_list_comp, time_map])
    print(f"{sorted_times[0]} vs {sorted_times[1]} vs {sorted_times[2]}")

if __name__ == '__main__':
    main()
