import sys
def ticker_symbols(short_company_name):
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
    res = ""
    short_company_name = short_company_name.upper()
    for key, value in COMPANIES.items():
        if value == short_company_name:
            res = key
            res += " " + str(STOCKS[short_company_name])
            break
        else:
            res = "Unknown ticker"
    return res


if __name__ == "__main__":
    if len(sys.argv) == 2:
        arg = sys.argv[1]
        print(ticker_symbols(arg))
