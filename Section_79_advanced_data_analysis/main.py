import pandas
import matplotlib.pyplot as pyplot
import seaborn

df = pandas.read_csv('nobel_prize_data.csv')
print(df.shape)
print(df.info())
print(df.describe())
print(df[df.duplicated() == True])
print(df.duplicated().values.any())
print(df[df.isna() == True])
print(df.isna().sum())

df['birth_date'] = pandas.to_datetime(df['birth_date'])
print(df['prize_share'])
prize_share = df['prize_share'].str.split("/", expand=True)
numerator = pandas.to_numeric(prize_share[0])
denominator = pandas.to_numeric(prize_share[1])
df['share_percent'] = numerator / denominator
print(df.info())
