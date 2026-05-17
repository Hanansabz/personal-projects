import requests
from datetime import datetime, timedelta


API_Key = '8f04dd3659a444fac15eed8194568b41'


def get_latest_stock_data(symbol):
    response = requests.get(f"https://api.marketstack.com/v2/eod/latest?access_key={API_Key}&symbols={symbol}")
    return response.json()




def get_stocksymbol_data_date1(symbol, date):
    response1 = requests.get(f"https://api.marketstack.com/v2/eod/{date}?access_key={API_Key}&symbols={symbol}")
    return response1.json()  


def get_stocksymbol_data_date2(symbol, date_minus):
    response2 = requests.get(f"https://api.marketstack.com/v2/eod/{date_minus}?access_key={API_Key}&symbols={symbol}")
    return response2.json()


def calculate_percent_change(stock_data1, stock_data2):
    number_change = ((stock_data1['data'][0]['close'] - stock_data2['data'][0]['close']) / stock_data2['data'][0]['close']) 
    percentage = number_change * 100 
    return percentage





# def get_stock_data_date1(date):
#     pass

# def get_stock_data_date2(date_minus_7):
#     pass

# def get_top_stocks_percent_change(stockprice1, stockprice2, percent_change_filter):
#     pass

    

while True:
    try:
        options = input("What would u like to do? (1) get LATEST stock data (2) get stock RANGE percentage change: {1 / 2}: ")
        if options == "1":
            symbol = input("Enter the stock symbol: ")
            symbol_data = get_latest_stock_data(symbol)
            print(f"~~~{symbol}~~~ Open: {symbol_data['data'][0]['open']}$, Close: {symbol_data['data'][0]['close']}$, High: {symbol_data['data'][0]['high']}$, Low: {symbol_data['data'][0]['low']}$")

        elif options == "2":
            input_symbol = input("Enter the stock symbol of choice: ")
            inputted_date = input("Enter specific date / yesterdays date / last stock movement date (YYYY-MM-DD): ")
            date_minus_number = int(input("Enter the number of days to subtract from the date: (to see percentage change from that day): "))

            stock_data1 = get_stocksymbol_data_date1(input_symbol, inputted_date)
            date_minus = (datetime.strptime(inputted_date, "%Y-%m-%d") - timedelta(days=date_minus_number)).strftime("%Y-%m-%d")
            stock_data2 = get_stocksymbol_data_date2(input_symbol, date_minus)
            percent_change = calculate_percent_change(stock_data1, stock_data2)

            print(f"~~~{input_symbol}~~~ Percent change: {percent_change:.2f}%")

        else:
            print("Invalid option")

    except Exception as e:
        print(f"Invalid input {e}")
