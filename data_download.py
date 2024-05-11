import yfinance as yf
import pandas as pd
import numpy as np


def fetch_stock_data(ticker, period='1mo', start_date=None, end_date=None):
    stock = yf.Ticker(ticker)
    if start_date and end_date:
        data = stock.history(start=start_date, end=end_date)  # Использование дат начала и окончания для получения данных за конкретный период
    else:
        data = stock.history(period=period)
    return data

def add_moving_average(data, window_size=5):
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data

def calculate_standard_deviation(data):
    data['Close_StdDev'] = data['Close'].rolling(window=30).std()
    return data

def export_data_to_csv(data, filename):
    try:
        data.to_csv(filename, index=False)
        print(f"Данные успешно экспортированы в файл: {filename}")
    except Exception as e:
        print(f"Произошла ошибка при экспорте данных в CSV: {e}")

def calculate_and_display_average_price(data: pd.DataFrame):
    average_price = data['Close'].mean()
    print(f"Средняя цена закрытия акций за заданный период: {average_price}")

def notify_if_strong_fluctuations(data: pd.DataFrame, threshold: float):
    price_max = data['Close'].max()
    price_min = data['Close'].min()
    price_range = price_max - price_min
    fluctuation = (price_range / price_min) * 100

    if fluctuation > threshold:
        print(f"Цена акций колебалась более чем на {threshold}% за заданный период.")
    else:
        print("Цена акций не колебалась на заданный процент за заданный период.")

def calculate_rsi(data, period=14):
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    data['RSI'] = rsi
    return data

def calculate_macd(data, short_period=12, long_period=26, signal_period=9):
    data['Short_MA'] = data['Close'].ewm(span=short_period, adjust=False).mean()
    data['Long_MA'] = data['Close'].ewm(span=long_period, adjust=False).mean()
    data['MACD'] = data['Short_MA'] - data['Long_MA']
    data['Signal_Line'] = data['MACD'].ewm(span=signal_period, adjust=False).mean()
    return data

