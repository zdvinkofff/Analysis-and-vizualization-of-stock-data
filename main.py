import data_download as dd
import data_plotting as dplt


def main():
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print(
        "Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print(
        "Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.")

    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc): ")
    period = input("Введите период для данных (например, '1mo' для одного месяца): ")
    start_date = input("Введите дату начала анализа (формат ГГГГ-ММ-ДД): ")
    end_date = input("Введите дату окончания анализа (формат ГГГГ-ММ-ДД): ")
    style = input("Введите стиль графика (например: 'ggplot', 'fivethirtyeight', 'tableau-colorblind10'): ")

    # Получение данных о биржевых ценных бумагах
    stock_data = dd.fetch_stock_data(ticker, start_date, end_date)

    # Добавление скользящей средней к данным
    stock_data = dd.add_moving_average(stock_data)

    # Построение графика
    dplt.create_and_save_plot(stock_data, ticker, period, style=style)

    dd.calculate_and_display_average_price(stock_data)
    dd.notify_if_strong_fluctuations(stock_data, 5)
    dd.export_data_to_csv(stock_data, "stock_data.csv")

    # Расчет и визуализация RSI
    stock_data = dd.calculate_rsi(stock_data)
    dplt.plot_rsi(stock_data, ticker, period)

    # Расчет и визуализация MACD
    stock_data = dd.calculate_macd(stock_data)
    dplt.plot_macd(stock_data, ticker, period)


if __name__ == "__main__":
    main()
