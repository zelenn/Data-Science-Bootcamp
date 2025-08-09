#!/usr/bin/env python3
import sys
import time
import requests
from bs4 import BeautifulSoup

def get_financial_data(ticker: str, field: str):
    """
    Делаем запрос к https://finance.yahoo.com/quote/{ticker}/financials?p={ticker}
    Ищем строку, где в первом столбце написано field
    Возвращаем кортеж значений (напр ('Total Revenue', '134,249,000', '125,843,000', ...))
    Если ничего не найдено, бросаем исключение.
    """

    url = f"https://finance.yahoo.com/quote/{ticker}/financials?p={ticker}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        raise ValueError(f"Invalid URL or ticker not found: {url}")

    # Парсим
    soup = BeautifulSoup(resp.text, "html.parser")

    # Ищем элемент, у которого rowTitle и нужное поле
    all_rows = soup.find_all("div", class_="row lv-0 yf-t22klz")
    for row in all_rows:
        title_div = row.find("div", class_="rowTitle")
        if title_div and title_div.text.strip().lower() == field.lower():
            number_divs = row.find_all("div", class_="column")
            # Удаляем лишни текст
            numbers = [
                div.text.strip()
                for div in number_divs
                if field.lower() not in div.text.strip().lower()
            ]
            return (field, *numbers)

    raise ValueError(f"Field '{field}' not found for ticker '{ticker}'")

    # Возвращаем кортеж значений
    return target_values

def main():
    if len(sys.argv) < 3:
        print("Usage: ./financial.py <TICKER> <FIELD>")
        sys.exit(1)

    ticker = sys.argv[1]
    field = sys.argv[2]

    # Делаем паузу спецом
    time.sleep(5)

    data = get_financial_data(ticker, field)
    print(data)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
