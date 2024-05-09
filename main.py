import data_download as dd
import data_plotting as dplt
import matplotlib.pyplot as plt

def main():
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print("Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print("Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.")

    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc): ")
    period = input("Введите период для данных (например, '1mo' для одного месяца): ")

    # Добавьте следующие две строки для ввода дат начала и окончания
    start_date = input("Введите начальную дату анализа (гггг-мм-дд): ")
    end_date = input("Введите конечную дату анализа (гггг-мм-дд): ")

    # Получение данных о биржевых ценных бумагах
    stock_data = dd.fetch_stock_data(ticker, period, start_date, end_date)

    # Добавление скользящей средней к данным
    stock_data = dd.add_moving_average(stock_data)

    # Расчет стандартного отклонения
    stock_data = dd.calculate_standard_deviation(stock_data)

    # Построение графика
    available_styles = plt.style.available
    print(f"Доступные стили: {', '.join(available_styles)}")
    plot_style = input(f"Выберите стиль графика (например, {', '.join(available_styles[:3])}): ")
    if plot_style not in available_styles:
        print(f"Неверный стиль '{plot_style}'. Используется стиль по умолчанию.")
        plot_style = 'default'
    dplt.create_and_save_plot(stock_data, ticker, period, plot_style=plot_style)

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
