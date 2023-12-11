import pandas
import matplotlib.pyplot as pyplot

column_names = ['Date', 'Tag', 'Posts']
data_frame = pandas.read_csv('QueryResults.csv', names=column_names).dropna()
print(data_frame.head())
print(data_frame.shape)
print(data_frame.groupby('Tag').sum())
print(data_frame.groupby('Tag').sum().idxmax())

print(type(data_frame['Date'][1]))

data_frame['Date'] = pandas.to_datetime(data_frame['Date'])
print(type(data_frame['Date'][1]))

reshaped_data_frame = data_frame.pivot(index='Date', columns='Tag', values='Posts')
print(reshaped_data_frame.head())
print(reshaped_data_frame.columns)

rolling_data_frame = reshaped_data_frame.rolling(window=6).mean()

pyplot.figure(figsize=(16, 10))
pyplot.xlabel('Date', fontsize=14)
pyplot.ylabel('Posts', fontsize=14)
pyplot.ylim(0, 35000)
for column in rolling_data_frame.columns:
    pyplot.plot(rolling_data_frame.index, rolling_data_frame[column], linewidth=3, label=rolling_data_frame[column].name)
pyplot.legend(fontsize=16)
pyplot.show()
