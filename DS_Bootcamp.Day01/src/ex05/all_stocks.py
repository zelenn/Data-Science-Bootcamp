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

def all_stocks():
    if len(sys.argv) != 2:
        return
    expressions = sys.argv[1].split(',')
    if any(expr.strip() == "" for expr in expressions):
        return
    for expr in expressions:
        expr = expr.strip()
        ticker = expr.upper()
        if ticker in STOCKS:
            company = next((c for c, t in COMPANIES.items() if t.upper() == ticker), None)
            if company:
                print(f"{ticker} is a ticker symbol for {company}")
            else:
                print(f"{ticker} is an unknown company or an unknown ticker symbol")

        else:
            found = False
            for company, t in COMPANIES.items():
                if company.lower() == expr.lower():
                    print(f"{company} stock price is {STOCKS[t]}")
                    found = True 
                    break
            if not found:
                print(f"{expr} is an unknown company or an unknown ticker symbol")

if __name__ == '__main__':
    all_stocks()