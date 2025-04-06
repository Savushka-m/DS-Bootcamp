import sys

def all_stocks(s):
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
    s = s.replace(" ", "").split(",")
    if "" not in s:
        for i in s:
            entered_name = i.capitalize()
            if i.capitalize() in COMPANIES:
                print(f"{i.capitalize()} stock price is {STOCKS[COMPANIES[i.capitalize()]]}")
            elif i.upper() in STOCKS:
                for key, value in COMPANIES.items():
                    if value == i.upper():
                        print(f"{i.upper()} is a ticker symbol for {key}")
            else:
                print(f"{i} is an unknown company or an unknown ticker symbol")




if __name__ == "__main__":
    if len(sys.argv) == 2:
        arg = sys.argv[1]
        all_stocks(arg)