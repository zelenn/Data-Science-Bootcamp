import pytest
from financial import get_financial_data

def test_total_revenue_valid():
    """
    Проверяем, что при валидном тикере (например, MSFT) и поле 'Total Revenue'
    функция возвращает непустой кортеж и первый элемент равен 'Total Revenue' (с учётом регистра).
    """
    result = get_financial_data("MSFT", "Total Revenue")
    assert isinstance(result, tuple), "Результат должен быть кортежем"
    assert len(result) > 1, "В кортеже должны быть данные"
    # первый элемент — имя поля, может отличаться регистром
    assert result[0].lower() == "total revenue".lower()

def test_return_type_tuple():
    """
    Проверяем тип возвращаемого значения (должен быть tuple).
    """
    result = get_financial_data("MSFT", "Operating Income")
    assert isinstance(result, tuple), "Ожидаем tuple!"

def test_invalid_ticker():
    """
    Проверяем, что при невалидном тикере функция выбрасывает исключение.
    """
    with pytest.raises(ValueError):
        get_financial_data("ZZZZZZZZ", "Total Revenue")
