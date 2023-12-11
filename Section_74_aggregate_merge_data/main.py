import pandas

data_frame = pandas.read_csv('data/colors.csv')

print(data_frame.head())
print(data_frame['rgb'].nunique())
print(data_frame.groupby('is_trans').count())
print(data_frame['is_trans'].value_counts())

data_frame = pandas.read_csv('data/sets.csv')
print(data_frame.head())
# In which year were the first LEGO sets released and what were these sets called?

print(data_frame.loc[data_frame['year'].idxmin()]['name'])

# How many different products did the LEGO company sell in their first year of operation?

# What are the top 5 LEGO sets with the most number of parts?
