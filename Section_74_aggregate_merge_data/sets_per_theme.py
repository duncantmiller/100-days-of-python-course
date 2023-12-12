import pandas
import matplotlib.pyplot as pyplot

sets_data_frame = pandas.read_csv('data/sets.csv')
themes_data_frame = pandas.read_csv('data/themes.csv')

set_theme_count = sets_data_frame['theme_id'].value_counts()
print(set_theme_count)
