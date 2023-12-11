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

difference = clean_data_frame['Mid-Career 90th Percentile Salary'] - clean_data_frame['Mid-Career 10th Percentile Salary']
print(difference)
clean_data_frame.insert(5, 'Difference', difference)
print(clean_data_frame.head())
low_risk = clean_data_frame.sort_values('Difference')
print(low_risk[['Undergraduate Major', 'Difference']].head())
print(clean_data_frame.groupby('Group').count())
pandas.options.display.float_format = '{:,.2f}'.format
print(clean_data_frame.groupby('Group')['Starting Median Salary'].mean())
