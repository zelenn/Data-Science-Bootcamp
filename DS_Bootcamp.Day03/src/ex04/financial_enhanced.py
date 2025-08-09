#!/usr/bin/env python3
import sys
import httpx
from bs4 import BeautifulSoup


def get_financial_data_enhanced(ticker: str, field: str):
    url = f"https://finance.yahoo.com/quote/{ticker}/financials?p={ticker}"

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/122.0.0.0 Safari/537.36"
        )
    }

    with httpx.Client(headers=headers, follow_redirects=True, timeout=10.0) as client:
        resp = client.get(url)

    if resp.status_code != 200:
        raise ValueError(f"Invalid URL or ticker not found: {url}")

    soup = BeautifulSoup(resp.text, "html.parser")

    all_rows = soup.find_all("div", class_="row lv-0 yf-t22klz")
    for row in all_rows:
        title_div = row.find("div", class_="rowTitle")
        if title_div and title_div.text.strip().lower() == field.lower():
            number_divs = row.find_all("div", class_="column")
            numbers = [
                div.text.strip()
                for div in number_divs
                if field.lower() not in div.text.strip().lower()
            ]
            return (field, *numbers)

    raise ValueError(f"Field '{field}' not found for ticker '{ticker}'")


def main():
    if len(sys.argv) < 3:
        print("Usage: ./financial_enhanced.py <TICKER> <FIELD>")
        sys.exit(1)

    ticker = sys.argv[1]
    field = sys.argv[2]

    result = get_financial_data_enhanced(ticker, field)
    print(result)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
