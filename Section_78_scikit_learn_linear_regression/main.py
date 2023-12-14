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

print(df_clean.info())
