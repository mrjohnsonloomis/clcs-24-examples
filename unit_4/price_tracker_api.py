import requests
import matplotlib.pyplot as plt

symbol = input('Which stock would you like to follow? (Enter stock symbol): ')
num_days = int(input('How many days back? : '))

API_KEY = 'WQT4AM73F83AQIO6'
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}'

response = requests.get(url)
table = response.json()

if 'Time Series (Daily)' not in table:
    print("Error: No data available for this symbol.")
else:
    time_series_daily = table['Time Series (Daily)']
    dates = list(time_series_daily.keys())[:num_days]
    close_values = [float(time_series_daily[date]['4. close']) for date in dates]

    plt.figure(figsize=(10, 8))
    plt.tight_layout()
    plt.title(f'{symbol} price from past {num_days} days starting {dates[0]}')
    plt.xlabel('Dates')
    plt.ylabel(f'Price of {symbol} in USD')
    plt.xticks(range(num_days), dates, rotation=45)
    plt.grid()
    plt.plot(dates, close_values)
    plt.show()
