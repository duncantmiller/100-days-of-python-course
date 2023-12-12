import pandas

df_tesla = pandas.read_csv('TESLA Search Trend vs Price.csv')
df_unemployment = pandas.read_csv('UE Benefits Search vs UE Rate 2004-20.csv')
df_btc_price = pandas.read_csv('Daily Bitcoin Price.csv')
df_btc_search = pandas.read_csv('Bitcoin Search Trend.csv')

print(df_btc_price[df_btc_price.isna().any(axis=1)])
print(df_btc_price.isna().sum())

df_tesla_cl = df_tesla.dropna()
df_unemployment_cl = df_unemployment.dropna()
df_btc_price_cl = df_btc_price.dropna()
df_btc_search_cl = df_btc_search.dropna()

