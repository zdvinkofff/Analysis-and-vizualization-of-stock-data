import matplotlib.pyplot as plt
import pandas as pd


def create_and_save_plot(data, ticker, period, filename=None, style='seaborn'):
    plt.style.use(style)

    plt.figure(figsize=(10, 6))

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['Close'].values, label='Close Price')
            plt.plot(dates, data['Moving_Average'].values, label='Moving Average')
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['Close'], label='Close Price')
        plt.plot(data['Date'], data['Moving_Average'], label='Moving Average')

    plt.title(f"{ticker} Цена акций с течением времени")
    plt.xlabel("Дата")
    plt.ylabel("Цена")
    plt.legend()

    if filename is None:
        filename = f"{ticker}_{period}_stock_price_chart.png"

    plt.savefig(filename)
    print(f"График сохранен как {filename}")


def plot_rsi(data, ticker, period):
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data['RSI'], label='RSI', color='purple')
    plt.axhline(y=70, color='r', linestyle='--', label='Overbought (70)')
    plt.axhline(y=30, color='g', linestyle='--', label='Oversold (30)')
    plt.title(f"RSI для {ticker} за период: {period}")
    plt.xlabel("Date")
    plt.ylabel("RSI Value")
    plt.legend()
    plt.savefig(f"{ticker}_{period}_rsi_chart.png")
    print("График RSI сохранен")

def plot_macd(data, ticker, period):
    plt.figure(figsize=(12, 8))
    plt.plot(data.index, data['MACD'], label='MACD', color='blue')
    plt.plot(data.index, data['Signal_Line'], label='Signal Line', color='red')
    plt.title(f"MACD для {ticker} за период: {period}")
    plt.xlabel("Date")
    plt.ylabel("MACD Value")
    plt.legend()
    plt.savefig(f"{ticker}_{period}_macd_chart.png")
    print("График MACD сохранен")

