import pandas

df = pandas.read_csv('cost_revenue_dirty.csv')
print(df.shape)
df_clean = df.dropna()
df_clean.drop_duplicates(inplace=True)
print(df_clean.head())

chars_to_remove = [',', '$']
columns_to_clean = ['USD_Production_Budget',
                    'USD_Worldwide_Gross',
                    'USD_Domestic_Gross']

for column in columns_to_clean:
    for character in chars_to_remove:
        df_clean[column] = df_clean[column].astype(str).str.replace(character, "")
    df_clean[column] = pandas.to_numeric(df_clean[column])

df_clean['Release_Date'] = pandas.to_datetime(df_clean['Release_Date'])

print(df_clean.info())

print(df_clean['USD_Production_Budget'].mean())
print(df_clean['USD_Worldwide_Gross'].mean())
print(df_clean['USD_Worldwide_Gross'].min())
print(df_clean['USD_Domestic_Gross'].min())

df_clean['Profit'] = df_clean['USD_Worldwide_Gross'] + df_clean['USD_Domestic_Gross'] - df_clean['USD_Production_Budget']

print(df_clean.sort_values('Profit').head(25))

print(df_clean[df_clean['USD_Domestic_Gross'] == 0])
