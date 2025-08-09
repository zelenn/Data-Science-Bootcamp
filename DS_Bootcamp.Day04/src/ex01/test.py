import pytest
from benchmark import get_gmails_loop, get_gmails_comprehension, get_gmails_map, get_emails

def test_ex01_results_identical():
    """
    Проверяем, что все три функции (цикл, list comprehension, map) возвращают одинаковый итоговый список.
    Также убеждаемся, что функция, использующая map, не содержит None в результате.
    Ожидаемый список – это повтор базовых Gmail адресов:
        ['john@gmail.com', 'james@gmail.com', 'philipp@gmail.com'] * 5
    """
    emails = get_emails()
    result_loop = get_gmails_loop(emails)
    result_comp = get_gmails_comprehension(emails)
    result_map = get_gmails_map(emails)
    expected = ['john@gmail.com', 'james@gmail.com', 'philipp@gmail.com'] * 5

    assert result_loop == expected, "Результат функции с циклом не соответствует ожидаемому."
    assert result_comp == expected, "Результат функции с list comprehension не соответствует ожидаемому."
    assert result_map == expected, "Результат функции с map не соответствует ожидаемому."
    assert all(x is not None for x in result_map), "Функция с map вернула None в итоговом списке."

def test_ex01_non_empty_results():
    """
    Дополнительная проверка – при пустом списке функция должна вернуть пустой список.
    """
    empty_emails = []
    assert get_gmails_loop(empty_emails) == []
    assert get_gmails_comprehension(empty_emails) == []
    assert get_gmails_map(empty_emails) == []
