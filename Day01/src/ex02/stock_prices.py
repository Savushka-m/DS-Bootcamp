import sys
def stock_prices(company_name):
    COMPANIES = {
    'Apple': 'AAPL',
    'Microsoft': 'MSFT',
    'Netflix': 'NFLX',
    'Tesla': 'TSLA',
    'Nokia': 'NOK'}

    STOCKS = {
    'AAPL': 287.73,
    'MSFT': 173.79,
    'NFLX': 416.90,
    'TSLA': 724.88,
    'NOK': 3.37}
    res = 0
    if company_name in COMPANIES:
        res = STOCKS[COMPANIES[company_name]]
    else:
        res = "Unknown company"
    return res


if __name__ == "__main__":
    if len(sys.argv) == 2:
        arg = sys.argv[1]
        print(stock_prices(arg.capitalize()))
