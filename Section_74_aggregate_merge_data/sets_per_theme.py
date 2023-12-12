import pandas
import matplotlib.pyplot as pyplot

data_frame = pandas.read_csv('data/sets.csv')

set_theme_count = data_frame['theme_id'].value_counts()
print(set_theme_count)
