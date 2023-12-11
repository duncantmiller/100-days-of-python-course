import pandas

data_frame = pandas.read_csv('data/colors.csv')

print(data_frame.head())
print(data_frame['rgb'].nunique())
print(data_frame.groupby('is_trans').count())
