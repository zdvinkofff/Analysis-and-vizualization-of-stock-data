import data_download as dd
import data_plotting as dplt
import pandas as pd

def main():
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print("Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print("Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.")

    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc):»")
    period = input("Введите период для данных (например, '1mo' для одного месяца): ")

    # Fetch stock data
    stock_data = dd.fetch_stock_data(ticker, period)

    # Add moving average to the data
    stock_data = dd.add_moving_average(stock_data)

    # Plot the data
    dplt.create_and_save_plot(stock_data, ticker, period)

    def calculate_and_display_average_price(data):
       average_price = stock_data['Close'].mean()
       print(f"Средняя цена закрытия акций за заданный период: {average_price}")

    def notify_if_strong_fluctuations(data, threshold):
        price_max = data['Close'].max()
        price_min = data['Close'].min()
        price_range = price_max - price_min
        fluctuation = (price_range / price_min) * 100

        if fluctuation > threshold:
            print(f"Цена акций колебалась более чем на {threshold}% за заданный период.")
        else:
            print("Цена акций не колебалась на заданный процент за заданный период.")

    def export_data_to_csv(data, filename):
        try:
            data.to_csv(filename, index=False)
            print(f"Данные успешно экспортированы в файл: {filename}")
        except Exception as e:
            print(f"Произошла ошибка при экспорте данных в CSV: {e}")

if __name__ == "__main__":
    main()




