import plotly.graph_objects as go
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px

# Функция для построения графика линии
def plot_line_chart(data):
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data['Close'], label='Close Price')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Stock Closing Price Over Time')
    plt.legend()
    plt.show()

# Функция для построения гистограммы
def plot_histogram(data):
    plt.figure(figsize=(8, 6))
    plt.hist(data['Close'], bins=20, color='skyblue', edgecolor='black')
    plt.xlabel('Price')
    plt.ylabel('Frequency')
    plt.title('Distribution of Stock Closing Prices')
    plt.show()


# Функция для построения столбчатой диаграммы
def plot_bar_chart(data):
    plt.figure(figsize=(10, 6))
    plt.bar(data.index, data['Close'], color='skyblue')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Bar Chart of Stock Closing Prices')
    plt.show()


# Добавим новые типы графиков в список доступных
available_plots = {
    'Line Chart': plot_line_chart,
    'Histogram': plot_histogram,
    'Bar Chart': plot_bar_chart,
}

def plot_interactive_average_close(data):
    average_close = data['Close'].mean()

    fig = go.Figure(data=go.Scatter(x=data.index, y=data['Close'], mode='lines', name='Close Price'))
    fig.add_hline(y=average_close, line_dash="dot", line_color="red", annotation_text=f'Average Close: {average_close}',
                  annotation_position="bottom right")

    fig.update_layout(title="Interactive Plot of Close Price with Average Line",
                      xaxis_title="Date",
                      yaxis_title="Close Price")

    fig.show()
def create_and_save_plot(data, ticker, period, filename=None, plot_style='default'):
    plt.figure(figsize=(10, 6))
    plt.style.use(plot_style)

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['Close'].values, label='Close Price')
            plt.plot(dates, data['Moving_Average'].values, label='Moving Average')
            plt.plot(dates, data['Close_StdDev'].values, label='Close Price Standard Deviation')
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['Close'], label='Close Price')
        plt.plot(data['Date'], data['Moving_Average'], label='Moving Average')
        plt.plot(data['Date'], data['Close_StdDev'], label='Close Price Standard Deviation')

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


