#!/usr/bin/env python3
import timeit
import random
from collections import Counter

def generate_list():
    """
    генерирует список из 1,000,000 случайных чисел в диапазоне от 0 до 100
    """
    return [random.randint(0, 100) for _ in range(1000000)]

def my_count(lst):
    """
    считает вручную количество вхождений каждого числа в списке
    
    возвращает словарь, где ключи – числа (0-100), а значения – их количество
    """
    counts = {}
    for num in lst:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    return counts

def counter_count(lst):
    """
    считает количество вхождений чисел с использованием Counter
    
    возвращает словарь, созданный из объекта Counter
    """
    return dict(Counter(lst))

def my_top(lst):
    """
    определяет топ-10 наиболее часто встречающихся чисел в списке, используя my_count()
    
    сначала получает словарь с подсчётом, затем сортирует его элементы по убыванию количества и возвращает первые 10 пар
    """
    counts = my_count(lst)
    sorted_items = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_items[:10]

def counter_top(lst):
    """
    определяет топ-10 наиболее часто встречающихся чисел с использованием Counter
    
    возвращает результат вызова метода most_common(10)
    """
    return Counter(lst).most_common(10)

def main():
    setup_code_my_count = f"""
from __main__ import generate_list, my_count
lst = generate_list()
"""
    time_my_count = timeit.timeit("my_count(lst)", setup=setup_code_my_count, number=1)

    setup_code_counter = f"""
from __main__ import generate_list, counter_count
lst = generate_list()
"""
    time_counter = timeit.timeit("counter_count(lst)", setup=setup_code_counter, number=1)

    setup_code_my_top = f"""
from __main__ import generate_list, my_top
lst = generate_list()
"""
    time_my_top = timeit.timeit("my_top(lst)", setup=setup_code_my_top, number=1)

    setup_code_counter_top = f"""
from __main__ import generate_list, counter_top
lst = generate_list()
"""
    time_counter_top = timeit.timeit("counter_top(lst)", setup=setup_code_counter_top, number=1)

    print(f"my function: {time_my_count}")
    print(f"Counter: {time_counter}")
    print(f"my top: {time_my_top}")
    print(f"Counter's top: {time_counter_top}")

if __name__ == '__main__':
    main()
