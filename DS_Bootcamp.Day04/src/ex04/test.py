import pytest
from benchmark import my_count, counter_count, my_top, counter_top

@pytest.fixture
def test_list():
    """
    Фикстура для детерминированного тестового списка.
    Здесь используем небольшой список, чтобы легко предсказать результаты:
      - Число 10 встречается 1 раз
      - Число 20 — 2 раза
      - Число 30 — 3 раза
      - Число 40 — 4 раза
    """
    return [10, 20, 20, 30, 30, 30, 40, 40, 40, 40]

def test_my_count_vs_counter_count(test_list):
    """
    Проверяет, что функция my_count (сделанная вручную) и функция counter_count (с использованием Counter)
    возвращают идентичные словари с подсчётом вхождений.
    Ожидаемый результат:
      {10: 1, 20: 2, 30: 3, 40: 4}
    """
    expected = {10: 1, 20: 2, 30: 3, 40: 4}
    result_manual = my_count(test_list)
    result_counter = counter_count(test_list)
    assert result_manual == expected, f"my_count вернула {result_manual}, ожидается {expected}"
    assert result_counter == expected, f"counter_count вернула {result_counter}, ожидается {expected}"
    assert result_manual == result_counter, "Результаты my_count и counter_count не совпадают"

def test_my_top_vs_counter_top(test_list):
    """
    Проверяет, что функция my_top (топ-10, реализованная вручную) и функция counter_top (с most_common(10))
    возвращают идентичный список из кортежей.
    Для тестового списка ожидается:
      [(40, 4), (30, 3), (20, 2), (10, 1)]
    """
    expected_top = [(40, 4), (30, 3), (20, 2), (10, 1)]
    result_my_top = my_top(test_list)
    result_counter_top = counter_top(test_list)
    assert result_my_top == expected_top, f"my_top вернула {result_my_top}, ожидается {expected_top}"
    assert result_counter_top == expected_top, f"counter_top вернула {result_counter_top}, ожидается {expected_top}"
    # проверяем идентичность результатов обеих функций
    assert result_my_top == result_counter_top, "Результаты my_top и counter_top не совпадают"