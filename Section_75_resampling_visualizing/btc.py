import pandas
import matplotlib.pyplot as pyplot

df_btc_price = pandas.read_csv('Daily Bitcoin Price.csv')
df_btc_search = pandas.read_csv('Bitcoin Search Trend.csv')

df_btc_price.dropna(inplace=True)
df_btc_search.dropna(inplace=True)

df_btc_price['DATE'] = pandas.to_datetime(df_btc_price['DATE'])
df_btc_search['MONTH'] = pandas.to_datetime(df_btc_search['MONTH'])

df_btc_monthly = df_btc_price.resample('M', on="DATE").last()
print(df_btc_search)

print(df_btc_monthly.head())
# pyplot.figure(figsize=(14, 9), dpi=120)
pyplot.title('Bitcoin News Search vs Resampled Price', fontsize=18)
pyplot.xticks(fontsize=14, rotation=45)
axis_1 = pyplot.gca()
axis_1.plot(df_btc_search['MONTH'], df_btc_search['BTC_NEWS_SEARCH'], linewidth=3)
axis_2 = axis_1.twinx()
axis_2.plot(df_btc_monthly.index, df_btc_monthly['CLOSE'], color="Red", linewidth=3, linestyle='dashed')
axis_1.set_ylabel('BTC Price', fontsize=14)
axis_2.set_ylabel('Search Trend', color="Red", fontsize=14)

pyplot.show()
