import pandas
import matplotlib.pyplot as pyplot
import plotly.express as plotly
import seaborn
import numpy

df = pandas.read_csv('nobel_prize_data.csv')
print(df.shape)
print(df.info())
print(df.describe())
print(df[df.duplicated() == True])
print(df.duplicated().values.any())
print(df[df.isna() == True])
print(df.isna().sum())

df['birth_date'] = pandas.to_datetime(df['birth_date'])
print(df['prize_share'])
prize_share = df['prize_share'].str.split("/", expand=True)
numerator = pandas.to_numeric(prize_share[0])
denominator = pandas.to_numeric(prize_share[1])
df['share_percent'] = numerator / denominator
print(df.info())

sex_data = df['sex'].value_counts()

# fig = plotly.pie(labels=sex_data.index,
#                  values=sex_data.values,
#                  title="Percentage M vs F",
#                  names=sex_data.index,
#                  hole=0.4)
# fig.update_traces(textposition='inside', textfont_size=15, textinfo='percent')
# fig.show()

print(df[df['sex'] == 'Female'].sort_values('year', ascending=True)[:3])

is_winner = df.duplicated(subset=['full_name'], keep=False)
mutiple_winners = df[is_winner]
print(mutiple_winners['full_name'].nunique())

print(df['category'].nunique())

# prizes_per_category = df['category'].value_counts()
# vbar = plotly.bar(
#        x = prizes_per_category.index,
#        y = prizes_per_category.values,
#        color = prizes_per_category.values,
#        color_continuous_scale='Aggrnyl',
#        title='Number of prizes per category'
# )
# vbar.update_layout(xaxis_title='Prize Category',
#                    coloraxis_showscale=False,
#                    yaxis_title='Number of prizes')

# vbar.show()

category_m_f = df.groupby(['category', 'sex'], as_index=False).agg({'prize': pandas.Series.count})
print(category_m_f)

# vbar_split = plotly.bar(x= category_m_f['category'],
#                         y= category_m_f['prize'],
#                         color= category_m_f['sex'],
#                         title='prizes per category split by men and women')

# vbar_split.show()

year_counts = df.groupby('year').size().reset_index(name='count')
year_counts['rolling_avg'] = year_counts['count'].rolling(window=5, min_periods=1).mean()
print(year_counts['rolling_avg'])

# Create a scatter plot
fig = plotly.scatter(year_counts, x='year', y='count', labels={'count': 'Count per Year'}, title='Scatter Plot with 5-Year Rolling Average')

# Add the rolling average line
fig.add_scatter(x=year_counts['year'], y=year_counts['rolling_avg'], mode='lines', name='5-Year Rolling Average')

years_ticks = numpy.arange(1900, 2021, step=5)

# Set x-axis ticks for every 5 years
fig.update_xaxes(tickvals=years_ticks, tickmode='array')

# fig.show()

df_countries = df.groupby(['birth_country_current', 'ISO'], as_index=False).agg(
    {'prize': pandas.Series.count}
)
df_countries.sort_values('prize', ascending=False)

world_map = plotly.choropleth(df_countries,
                          locations='ISO',
                          color='prize',
                          hover_name='birth_country_current',
                          color_continuous_scale=plotly.colors.sequential.matter)

world_map.update_layout(coloraxis_showscale=True,)

world_map.show()
