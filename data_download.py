import yfinance as yf
import pandas as pd


def fetch_stock_data(ticker, period='1mo'):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def add_moving_average(data, window_size=5):
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
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
