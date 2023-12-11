import pandas

data_frame = pandas.read_csv('data/colors.csv')

print(data_frame.head())
print(data_frame['rgb'].nunique())
print(data_frame.groupby('is_trans').count())
print(data_frame['is_trans'].value_counts())

data_frame = pandas.read_csv('data/sets.csv')
print(data_frame.head())
# In which year were the first LEGO sets released and what were these sets called?

rows = data_frame[data_frame['year'] == data_frame['year'].min()]
print(rows['name'])

# How many different products did the LEGO company sell in their first year of operation?

print(rows.count()['set_num'])

# What are the top 5 LEGO sets with the most number of parts?
