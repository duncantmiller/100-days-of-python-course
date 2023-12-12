import pandas
import matplotlib.pyplot as pyplot

data_frame = pandas.read_csv('data/sets.csv')

# Create a Pandas Series called parts_per_set that has the year as the index and contains the average
# number of parts per LEGO set in that year.

parts_per_set = data_frame.groupby('year').agg({'num_parts': pandas.Series.mean})
print(parts_per_set.head())

# use the Matplotlib documentation to generate the scatter plot chart.

pyplot.scatter(parts_per_set.index[:-2], parts_per_set['num_parts'][:-2])
pyplot.show()
