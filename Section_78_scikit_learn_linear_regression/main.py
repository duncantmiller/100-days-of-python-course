import pandas
import matplotlib.pyplot as pyplot
import seaborn

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

print(df_clean.describe())

int_releases = df_clean.query('USD_Worldwide_Gross != 0 and USD_Domestic_Gross == 0')
print(len(int_releases))
print(int_releases)

scraped = pandas.Timestamp('2018-5-1')
future_releases = df_clean[df_clean['Release_Date'] >= scraped]

df_clean_past = df_clean.drop(future_releases.index)

# pyplot.figure(figsize=(8,4), dpi=200)

# with seaborn.axes_style('darkgrid'):
#     ax = seaborn.scatterplot(
#         data=df_clean_past,
#         x='USD_Production_Budget',
#         y='USD_Worldwide_Gross',
#         hue='USD_Worldwide_Gross',
#         size='USD_Worldwide_Gross'
#     )

#     ax.set(ylim=(0, 3000000000),
#         xlim=(0, 450000000),
#         ylabel='Revenue in $ billions',
#         xlabel='Budget in $100 millions'
#     )

# pyplot.show()

date_data = pandas.DatetimeIndex(df_clean_past['Release_Date'])
year = date_data.year
df_clean_past['Decade'] = year//10*10
print(df_clean_past.head())

old_films = df_clean_past[df_clean_past['Decade'] <= 1960]
new_films = df_clean_past[df_clean_past['Decade'] > 1960]
print(old_films)
print(old_films.shape)
print(new_films.shape)

pyplot.figure(figsize=(8,4), dpi=200)
with seaborn.axes_style("whitegrid"):
    seaborn.regplot(data=old_films,
                    x='USD_Production_Budget',
                    y='USD_Worldwide_Gross',
                    scatter_kws={'alpha': 0.4},
                    line_kws={'color': 'black'}
    )
    pyplot.show()
