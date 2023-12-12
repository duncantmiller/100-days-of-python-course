import pandas
import matplotlib.pyplot as pyplot

sets_data_frame = pandas.read_csv('data/sets.csv')
themes_data_frame = pandas.read_csv('data/themes.csv')

set_theme_count = pandas.DataFrame(sets_data_frame['theme_id'].value_counts())
merged_data_frame = pandas.merge(set_theme_count, themes_data_frame, left_on='theme_id', right_on='id', how='inner')

print(merged_data_frame)
