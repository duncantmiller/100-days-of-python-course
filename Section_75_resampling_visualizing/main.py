import pandas

df_tesla = pandas.read_csv('TESLA Search Trend vs Price.csv')
df_unemployment = pandas.read_csv('UE Benefits Search vs UE Rate 2004-20.csv')
df_btc_price = pandas.read_csv('Daily Bitcoin Price.csv')
df_btc_search = pandas.read_csv('Bitcoin Search Trend.csv')

print(df_btc_price[df_btc_price.isna().any(axis=1)])
print(df_btc_price.isna().sum())
df_tesla.dropna(inplace=True)
df_unemployment.dropna(inplace=True)
df_btc_price.dropna(inplace=True)
df_btc_search.dropna(inplace=True)

print(pandas.to_datetime(df_tesla['MONTH']))
print(pandas.to_datetime(df_unemployment['MONTH']))
print(pandas.to_datetime(df_btc_price['DATE']))
print(pandas.to_datetime(df_btc_search['MONTH']))
