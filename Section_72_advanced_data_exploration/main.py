import pandas

data_frame = pandas.read_csv('salaries_by_college_major.csv')

print(data_frame.head())
print(data_frame.shape)
print(data_frame.columns)
print(data_frame.isna())
print(data_frame.tail())

clean_data_frame = data_frame.dropna()

print(clean_data_frame['Starting Median Salary'].max())
print(clean_data_frame['Starting Median Salary'].idxmax())
location_id = clean_data_frame['Starting Median Salary'].idxmax()
print(clean_data_frame['Undergraduate Major'].loc[location_id])
print(clean_data_frame['Starting Median Salary'].min())
