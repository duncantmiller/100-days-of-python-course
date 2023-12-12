import pandas
import matplotlib.pyplot as pyplot
import matplotlib.dates as mdates

df_tesla = pandas.read_csv('TESLA Search Trend vs Price.csv')
df_unemployment = pandas.read_csv('UE Benefits Search vs UE Rate 2004-20.csv')
df_btc_price = pandas.read_csv('Daily Bitcoin Price.csv')
df_btc_search = pandas.read_csv('Bitcoin Search Trend.csv')

years = mdates.YearLocator()
months = mdates.MonthLocator()
years_formatted = mdates.DateFormatter('%Y')

print(df_btc_price[df_btc_price.isna().any(axis=1)])
print(df_btc_price.isna().sum())
df_tesla.dropna(inplace=True)
df_unemployment.dropna(inplace=True)
df_btc_price.dropna(inplace=True)
df_btc_search.dropna(inplace=True)

df_tesla['MONTH'] = pandas.to_datetime(df_tesla['MONTH'])
df_unemployment['MONTH'] = pandas.to_datetime(df_unemployment['MONTH'])
df_btc_price['DATE'] = pandas.to_datetime(df_btc_price['DATE'])
df_btc_search['MONTH'] = pandas.to_datetime(df_btc_search['MONTH'])

print(type(df_tesla['MONTH'][0]))
df_btc_monthly = df_btc_price.resample('M', on="DATE").last()
print(df_btc_monthly)

print(df_tesla.head())
pyplot.figure(figsize=(14, 9), dpi=120)
pyplot.title('Tesla Web Search vs Price', fontsize=18)
pyplot.xticks(fontsize=14, rotation=45)
axis_1 = pyplot.gca()
axis_1.xaxis.set_major_locator(years)
axis_1.xaxis.set_minor_locator(months)
axis_1.xaxis.set_major_formatter(years_formatted)
axis_1.set_xlim([df_tesla['MONTH'].min(), df_tesla["MONTH"].max()])
axis_1.plot(df_tesla['MONTH'], df_tesla['TSLA_WEB_SEARCH'], linewidth=3)
axis_2 = axis_1.twinx()
axis_2.plot(df_tesla['MONTH'], df_tesla['TSLA_USD_CLOSE'], color="Red", linewidth=3)
axis_1.set_ylabel('TSLA Stock Price', fontsize=14)
axis_2.set_ylabel('Search Trend', color="Red", fontsize=14)

pyplot.show()

