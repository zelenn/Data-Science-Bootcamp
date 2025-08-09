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

def stock_prices():
    if len(sys.argv) != 2:
        return
    company_input = sys.argv[1]

    for company, ticker in COMPANIES.items():
        if company.lower() == company_input.lower():
            print(STOCKS[ticker])
            return
    print("Unknown company")


if __name__ == '__main__':
    stock_prices()