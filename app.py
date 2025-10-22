# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template("index.html")

# if __name__ == '__main__':
#     app.run(debug=True)


##Api Key : SI1O16E6XH389GHD
from datetime import datetime
from flask inport Flask, render_template, request
#import pygal
from py

print("Stock Data Visualizer")
print("---------------------")

symbol = input("\nEnter the stock symbol you are looking for: ")

# Validate chart type
while True:
    print("\nChart Types")
    print("-------------")
    print("1. Bar")
    print("2. Line")
	
    chartType = input("\nEnter the chart type you want (1, 2): ")
	
    if chartType in ("1", "2"):
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

    timeSeries = input("\nEnter time series option (1, 2, 3, 4): ")

    if timeSeries in ("1", "2", "3", "4"):
        break

    print("\nInvalid selection. Please enter 1, 2, 3, or 4.")

# Validate start date
while True:
    startStr = input("\nEnter the start date (YYYY-MM-DD): ")
    try:
        startDate = datetime.strptime(startStr, "%Y-%m-%d").date()
        break
    except ValueError:
        print("\nInvalid date format. Please enter date as YYYY-MM-DD.")

# Validate end date (YYYY-MM-DD) and ensure it is not earlier than start_date
while True:
    endStr = input("\nEnter the end date (YYYY-MM-DD): ")
    try:
        endDate = datetime.strptime(endStr, "%Y-%m-%d").date()
    except ValueError:
        print("\nInvalid date format. Please enter date as YYYY-MM-DD.")
        continue

    if endDate < startDate:
        print("\nEnd date cannot be earlier than start date. Please enter a later or equal date.")
        continue

    break