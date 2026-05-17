from datetime import datetime, timedelta
import requests

API_Key = '8f04dd3659a444fac15eed8194568b41'

# url = requests.get(f"http://api.marketstack.com/v1/tickers?access_key={API_Key}")
# print(url.json())

def get_stock_data1(symbol, date):
    response1 = requests.get(f"https://api.marketstack.com/v2/eod/{date}?access_key={API_Key}&symbols={symbol}")
    return response1.json()  

def get_stock_data2(symbol, date_minus_7):
    response2 = requests.get(f"https://api.marketstack.com/v2/eod/{date_minus_7}?access_key={API_Key}&symbols={symbol}")
    return response2.json()

def calculate_percent_change(stock_data1, stock_data2):
    number_change = ((stock_data1['data'][0]['close'] - stock_data2['data'][0]['close']) / stock_data2['data'][0]['close']) 
    percent_change = number_change * 100 
    return percent_change

while True:
    try:
        input_symbol = input("Enter the stock symbol: (Upper-case) ")

        inputted_date = input("Enter yesterdays date (YYYY-MM-DD): ")
        date_minus_number = int(input("Enter the number of days to subtract from the date: "))

        stock_data1 = get_stock_data1(input_symbol, inputted_date)
        date_minus = (datetime.strptime(inputted_date, "%Y-%m-%d") - timedelta(days=date_minus_number)).strftime("%Y-%m-%d")
        stock_data2 = get_stock_data2(input_symbol, date_minus)
        percent_change = calculate_percent_change(stock_data1, stock_data2)

        print(f"Percent change: {percent_change:.2f}%")
    except Exception as e:
        print(f"Invalid input {e}")

    input ("Press Enter to exit...")