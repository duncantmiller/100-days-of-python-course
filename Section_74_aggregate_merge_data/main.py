import pandas
import matplotlib.pyplot as pyplot

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

top_5_parts_ids = data_frame['num_parts'].sort_values(ascending=False).head(5).index

print(data_frame.loc[top_5_parts_ids]['name'])

# Make a chart of sets by year

sets_by_year = data_frame.groupby('year').count()
sets_by_year_mod = sets_by_year.sort_index()[:-2]
pyplot.plot(sets_by_year_mod.index, sets_by_year_mod)

# use agg function to get themes by year
themes_by_year = data_frame.groupby('year').agg({'theme_id': pandas.Series.nunique})

themes_by_year.rename(columns= {'theme_id': 'theme count'}, inplace = True)
print(themes_by_year.head())

pyplot.show()
