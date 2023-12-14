import pandas
import matplotlib.pyplot as pyplot
import plotly.express as plotly
import seaborn

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

prizes_per_category = df['category'].value_counts()
vbar = plotly.bar(
       x = prizes_per_category.index,
       y = prizes_per_category.values,
       color = prizes_per_category.values,
       color_continuous_scale='Aggrnyl',
       title='Number of prizes per category'
)
vbar.update_layout(xaxis_title='Prize Category',
                   coloraxis_showscale=False,
                   yaxis_title='Number of prizes')

vbar.show()
