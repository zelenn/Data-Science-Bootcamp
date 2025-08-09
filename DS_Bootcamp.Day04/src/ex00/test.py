import pytest
from benchmark import get_gmails_loop, get_gmails_comprehension, get_emails

def test_ex00_results_identical():
    """
    Проверяем, что обе функции (с циклом и генератором списков) возвращают корректный итоговый список.
    Ожидаемый список – это те же Gmail-адреса, которые получаются из базового списка:
    базовые email:
        ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']
    Из них только:
        'john@gmail.com', 'james@gmail.com', 'philipp@gmail.com'
    Повторённые 5 раз (25 элементов исходного списка дает 15 корректных адресов).
    """
    emails = get_emails()
    result_loop = get_gmails_loop(emails)
    result_comp = get_gmails_comprehension(emails)
    expected = ['john@gmail.com', 'james@gmail.com', 'philipp@gmail.com'] * 5

    assert result_loop == expected, "Результат функции с циклом не соответствует ожидаемому."
    assert result_comp == expected, "Результат функции с list comprehension не соответствует ожидаемому."
    assert result_loop == result_comp, "Результаты функций (цикл и генератор списков) не идентичны."
