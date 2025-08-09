import sys

COMPANIES = {
    'Apple': 'AAPL',
    'Microsoft': 'MSFT',
    'Netflix': 'NFLX',
    'Tesla': 'TSLA',
    'Nokia': 'NOK'
}

STOCKS = {
    'AAPL': 287.73,
    'MSFT': 173.79,
    'NFLX': 416.90,
    'TSLA': 724.88,
    'NOK': 3.37
}

def ticker_symbols():
    if len(sys.argv) != 2:
        return
    ticker_input = sys.argv[1].upper()

    for company, ticker in COMPANIES.items():
        if ticker.upper() == ticker_input:
            print(f"{company} {STOCKS[ticker_input]}")
            return
    print("Unknown ticker")

if __name__ == '__main__':
    ticker_symbols()