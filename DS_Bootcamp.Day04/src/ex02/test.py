import pytest
from benchmark import (
    get_gmails_loop,
    get_gmails_comprehension,
    get_gmails_map,
    get_gmails_filter,
    get_emails,
    benchmark
)

def test_gmail_functions_results():
    """
    Проверяем, что все четыре функции возвращают корректный итоговый список Gmail-адресов,
    и что результаты всех функций идентичны.
    Ожидаемый результат:
       ['john@gmail.com', 'james@gmail.com', 'philipp@gmail.com'] * 5
    """
    emails = get_emails()
    expected = ['john@gmail.com', 'james@gmail.com', 'philipp@gmail.com'] * 5

    result_loop = get_gmails_loop(emails)
    result_comp = get_gmails_comprehension(emails)
    result_map = get_gmails_map(emails)
    result_filter = get_gmails_filter(emails)

    assert result_loop == expected, "Функция get_gmails_loop возвращает неверный результат"
    assert result_comp == expected, "Функция get_gmails_comprehension возвращает неверный результат"
    assert result_map == expected, "Функция get_gmails_map возвращает неверный результат"
    assert result_filter == expected, "Функция get_gmails_filter возвращает неверный результат"

    assert result_loop == result_comp == result_map == result_filter, "Результаты функций не совпадают"

def test_benchmark_valid_names():
    """
    Проверяем, что benchmark для каждого допустимого имени функции ('loop', 'list_comprehension', 'map', 'filter')
    возвращает число типа float, а также что число не отрицательно.
    Для ускорения теста используется небольшое число итераций.
    """
    for func_name in ['loop', 'list_comprehension', 'map', 'filter']:
        t = benchmark(func_name, 10)
        assert isinstance(t, float), f"benchmark('{func_name}', 10) не возвращает float"
        assert t >= 0, f"benchmark('{func_name}', 10) вернул отрицательное значение: {t}"

def test_benchmark_invalid_name():
    """
    Проверяем, что функция benchmark выбрасывает ValueError,
    если передано неверное имя функции.
    """
    with pytest.raises(ValueError):
        benchmark("nonexistent", 10)
