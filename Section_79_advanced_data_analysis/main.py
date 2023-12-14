import pandas
import matplotlib.pyplot as pyplot
import seaborn

df = pandas.read_csv('nobel_prize_data.csv')
print(df.shape)
print(df.info())
print(df.describe())
print(df[df.duplicated() == True])
print(df[df.isna() == True])

