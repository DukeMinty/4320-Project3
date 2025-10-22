# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template("index.html")

# if __name__ == '__main__':
#     app.run(debug=True)

from datetime import datetime
import requests
import pygal
import webbrowser
import os

api_key = "SI1O16E6XH389GHD"

print("Stock Data Visualizer")
print("---------------------")

symbol = input("\nEnter the stock symbol you are looking for: ")

# Validate chart type
while True:
    print("\nChart Types")
    print("-------------")
    print("1. Bar")
    print("2. Line")
	
    chart_type = input("\nEnter the chart type you want (1, 2): ")

    if chart_type in ("1", "2"):
        break
	
    print("\nInvalid selection. Please enter 1 or 2.")

# Validate time series
while True:
    print("\nSelect the Time Series of the chart you want to Generate")
    print("----------------------------------------------------------")
    print("1. Intraday")
    print("2. Daily")
    print("3. Weekly")
    print("4. Monthly")

    time_series = input("\nEnter time series option (1, 2, 3, 4): ")

    if time_series in ("1", "2", "3", "4"):
        break

    print("\nInvalid selection. Please enter 1, 2, 3, or 4.")

# Validate start date
while True:
    start_str = input("\nEnter the start date (YYYY-MM-DD): ")
    try:
        start_date = datetime.strptime(start_str, "%Y-%m-%d").date()
        break
    except ValueError:
        print("\nInvalid date format. Please enter date as YYYY-MM-DD.")

# Validate end date (YYYY-MM-DD) and ensure it is not earlier than start_date
while True:
    end_str = input("\nEnter the end date (YYYY-MM-DD): ")
    try:
        end_date = datetime.strptime(end_str, "%Y-%m-%d").date()
    except ValueError:
        print("\nInvalid date format. Please enter date as YYYY-MM-DD.")
        continue

    if end_date < start_date:
        print("\nEnd date cannot be earlier than start date. Please enter a later or equal date.")
        continue

    break

if time_series == "1":
    function = "TIME_SERIES_INTRADAY"
    interval = "5min"
    url = f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&interval={interval}&apikey={api_key}'
elif time_series == "2":
    function = "TIME_SERIES_DAILY"
    url = f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&apikey={api_key}'
elif time_series == "3":
    function = "TIME_SERIES_WEEKLY"
    url = f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&apikey={api_key}'
elif time_series == "4":
    function = "TIME_SERIES_MONTHLY"
    url = f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&apikey={api_key}'

r = requests.get(url)
data = r.json()

#Checking for valid data
time_series_key = None
for key in data:
    if "Time Series" in key:
        time_series_key = key
        break

if not time_series_key:
    print("Error: Time series data not found in the response.")
    exit(1)

#Format data for chart
raw_series = data[time_series_key]

dates = []
open_prices = []
high_prices = []
low_prices = []
close_prices = []

for date_str in sorted(raw_series.keys(), reverse=False):
    if time_series == "1":
        dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    else:
        dt = datetime.strptime(date_str, "%Y-%m-%d")

    if start_date <= dt.date() <= end_date:
        dates.append(date_str)
        open_prices.append(float(raw_series[date_str]['1. open']))
        high_prices.append(float(raw_series[date_str]['2. high']))
        low_prices.append(float(raw_series[date_str]['3. low']))
        close_prices.append(float(raw_series[date_str]['4. close']))

# Create chart
if chart_type == "1":
    chart = pygal.Bar(x_label_rotation=20)
else:
    chart = pygal.Line(x_label_rotation=20)

chart.title = f"Stock Data for {symbol.upper()}: {start_date} to {end_date}"
chart.x_labels = dates
chart.add('Open', open_prices)
chart.add('High', high_prices)
chart.add('Low', low_prices)
chart.add('Close', close_prices)

# Render to file and open in browser
chart_file = 'stock_chart.svg'
chart.render_to_file(chart_file)

# Open in default browser
file_url = 'file://' + os.path.realpath(chart_file)
webbrowser.open(file_url)

print(f"\nChart generated and opened in browser: {chart_file}")

