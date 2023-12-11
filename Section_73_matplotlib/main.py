import pandas

column_names = ['Date', 'Tag', 'Posts']
data_frame = pandas.read_csv('QueryResults.csv', names=column_names).dropna()
print(data_frame.head())
print(data_frame.shape)
print(data_frame.groupby('Tag').sum())
print(data_frame.groupby('Tag').sum().idxmax())
