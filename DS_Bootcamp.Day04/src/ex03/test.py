import pytest
from benchmark import sum_squares_loop, sum_squares_reduce, benchmark

def test_sum_squares_correct():
    """
    Проверяет, что для n = 5 обе функции возвращают корректное значение (55).
    """
    n = 5
    expected = 55
    result_loop = sum_squares_loop(n)
    result_reduce = sum_squares_reduce(n)
    assert result_loop == expected, "sum_squares_loop вернула неверное значение для n=5"
    assert result_reduce == expected, "sum_squares_reduce вернула неверное значение для n=5"

def test_identical_results():
    """
    Для n = 10 результаты функций sum_squares_loop и sum_squares_reduce должны совпадать.
    """
    n = 10
    result_loop = sum_squares_loop(n)
    result_reduce = sum_squares_reduce(n)
    assert result_loop == result_reduce, f"Результаты отличаются: loop={result_loop}, reduce={result_reduce}"

def test_benchmark_valid_names():
    """
    Проверяет, что benchmark для корректных имён ('loop' и 'reduce')
    возвращает число типа float и неотрицательное.
    Используется небольшое число итераций (10) для ускорения теста.
    """
    iterations = 10
    n = 5
    for func_name in ['loop', 'reduce']:
        time_spent = benchmark(func_name, iterations, n)
        assert isinstance(time_spent, float), f"Benchmark('{func_name}', {iterations}, {n}) не вернул float"
        assert time_spent >= 0, f"Benchmark('{func_name}', {iterations}, {n}) вернул отрицательное значение: {time_spent}"

def test_benchmark_invalid_name():
    """
    При передаче неправильного имени функции benchmark должна выбросить ValueError.
    """
    with pytest.raises(ValueError):
        benchmark("invalid", 10, 5)
