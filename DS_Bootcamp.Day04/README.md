# Intro to Python: Efficient Code Practices

This project was developed as part of a Python fundamentals module, focusing on optimizing code performance through functional programming patterns, built-in tools, and memory-efficient techniques. 

The complete task specifications are available in [this document](README-full.md)


## Project Structure

### 00: List Comprehensions
- Compare loop vs list comprehension for filtering Gmail addresses
- Benchmark 90M iterations
- Output fastest method with timing

### 01: Map
- Add `map()` implementation to previous exercise
- Compare three methods (loop, comprehension, map)
- Output performance results sorted by speed

### 02: Filter
- Implement `filter()` solution
- Refactor to accept function name and iteration count as args
- Return execution time for specified function

### 03: Reduce
- Calculate sum of squares using:
  - Traditional loop
  - `reduce()` from functools
- Benchmark with customizable iterations and input number

### 04: Counter
- Generate 1M random numbers (0-100)
- Compare custom counting vs `collections.Counter`
- Time both implementations for:
  - Full count dictionary
  - Top 10 frequent numbers

### 05: Generator
- Process MovieLens dataset (ratings.csv)
- Compare memory/performance of:
  - Regular list loading (`ordinary.py`)
  - Generator approach (`generator.py`)
- Measure peak memory and CPU time


## Efficiency Principles
- "Efficiency is doing things right"
- Balance speed and memory usage
- Leverage Python built-ins and stdlib
- Prefer functional programming patterns when appropriate