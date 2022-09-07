
from tradingview_ta import TA_Handler, Interval, Exchange
from spisok_crypto import cryptog


# class Recomend:
#     def Proverka(q,s,g):
#         tesla = TA_Handler(
#             symbol=q,
#             screener=s,
#             exchange=g,
#             interval=Interval.INTERVAL_1_MINUTE,
#         )
#         return tesla.get_analysis().summary

# qf = input('Введите название продукта "TSLA": ' )
# s = input('Введит категорию биржи "america": ' )
# gg = input('Введите название биржи "NASDAQ": ' )
# # print(Recomend.Proverka(qf,s,gg))

# while True:
#     if Recomend.Proverka(qf,s,gg) == 'STRONG BUY' or Recomend.Proverka(qf,s,gg) == 'BUY':
#         print('вы купили криптовалюту')
#     if Recomend.Proverka(qf,s,gg) == 'STRONG SELL' or Recomend.Proverka(qf,s,gg) == 'SELL':
#         print('Не покупать криптовалюту')
#     if Recomend.Proverka(qf,s,gg) == 'NEUTRAL':
#         print('нейтральная значение')


for i in cryptog:
    try:
        tesla = TA_Handler(
            symbol=i,
            screener="crypto",
            exchange="bybit",
            interval=Interval.INTERVAL_1_MINUTE,
        )
        a = tesla.get_analysis().summary
        if a['RECOMMENDATION'] == 'STRONG BUY':
        # if a['RECOMMENDATION'] == 'BUY' or a['RECOMMENDATION'] == 'STRONG BUY':
            print(tesla.get_analysis().time)
            print(f'вы купили криптовалюту')
            print(tesla.get_analysis().symbol)
            print(f'индикатор открытия: {tesla.get_analysis().indicators["open"]}')
            print(f'импульс: {tesla.get_analysis().indicators["Mom"]}')
            print(f'индекс относительной силы: {tesla.get_analysis().indicators["RSI"]}')
            print('──────────────────')

        if a['RECOMMENDATION'] == 'SELL' or a['RECOMMENDATION'] == 'STRONG SELL':
            print(f'Пора продавать криптовалюту')
            print(tesla.get_analysis().time)
            print(tesla.get_analysis().symbol)
            print(f'индикатор закрытия: {tesla.get_analysis().indicators["close"]}')
            print(f'импульс: {tesla.get_analysis().indicators["Mom"]}')
            print(f'индекс относительной силы: {tesla.get_analysis().indicators["RSI"]}')
            print('──────────────────')

        if a['RECOMMENDATION'] == 'NEUTRAL':
            print('нейтральная значение')
            print(tesla.get_analysis().time)
            print(tesla.get_analysis().symbol)
            print(f'импульс: {tesla.get_analysis().indicators["Mom"]}')
            print(f'индекс относительной силы: {tesla.get_analysis().indicators["RSI"]}')
            print('──────────────────')
    except:
        pass


# tesla = TA_Handler(
#     symbol="DARUSDT",
#     screener="crypto",
#     exchange="bybit",
#     interval=Interval.INTERVAL_1_MINUTE
# )
# a = tesla.get_analysis().indicators["open"]
# b = tesla.get_analysis().indicators["close"]
# v = tesla.get_analysis().indicators["Mom"]
# g = tesla.get_analysis().indicators["RSI"]
# print(f'индикатор открытия: {a}\nиндикатор закрытия: {b}\nимпульс: {v}\nиндекс относительной силы: {g}')



# Логика торгового бота:
# Брать из базы данных все названия валют(symbol) и вставлять в переменную 'symbol='
# И крутить все 'symbol' по циклу пока значения одного из валют не совпадут с условием(STRONG BUY)
# и дальше после выбора покупки он должен ждать следуйшего условия на продажу(SELL или же STRONG SELL) 
# при этом цикл должен дальше продолжаться пока в другой валюте не появится значение(STRONG BUY) 
# бот не может покупать уже купленные ранее валюты пока он их не продал если продал то может покупать заново

# так же бот будет вести учет по торговле, каждой сделки:
# 1. дата покупки
# 2. по какой цене купил
# 3. дата продажи
# 4. по какой цене продал
# 5. процент маржи от сделки
# 6. время общей торговли(сколько времени он торговал)
