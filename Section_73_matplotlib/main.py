import pandas

column_names = ['Date', 'Tag', 'Posts']
data_frame = pandas.read_csv('QueryResults.csv', names=column_names).dropna()
print(data_frame.head())
print(data_frame.shape)
print(data_frame.groupby('Tag').sum())
print(data_frame.groupby('Tag').sum().idxmax())

print(type(data_frame['Date'][1]))

data_frame['Date'] = pandas.to_datetime(data_frame['Date'])
print(type(data_frame['Date'][1]))
