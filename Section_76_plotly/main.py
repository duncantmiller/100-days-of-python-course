import pandas
import plotly.express as plotly

df_apps = pandas.read_csv('apps.csv')
df_apps.drop(columns=['Last_Updated', 'Android_Ver'], inplace=True)
print(df_apps.shape)
print(df_apps.sample())
df_apps_clean = df_apps.dropna()
print(df_apps.sample())
print(df_apps_clean.shape)
df_apps_clean.drop_duplicates(inplace=True)
print(df_apps_clean.duplicated().sum())
print(df_apps_clean[df_apps_clean['App'] == 'Instagram'])
df_apps_clean.drop_duplicates(inplace=True, subset=['App', 'Type', 'Price'])
print(df_apps_clean[df_apps_clean['App'] == 'Instagram'])
print(df_apps_clean.sort_values("Rating"))
rating_counts = df_apps_clean.value_counts("Content_Rating")
print(rating_counts)
# fig = plotly.pie(
#     labels=rating_counts.index,
#     values=rating_counts.values,
#     title="Content Rating",
#     names=rating_counts.index,
#     hole=0.6
# )
# fig.update_traces(textposition='inside', textinfo='percent', textfont_size=15)
# fig.show()

print(type(df_apps_clean["Installs"].values[0]))

def clean_string(value):
    """cleans string"""
    no_commas = value.replace(',', '')
    clean_str = no_commas.replace('$', '')
    return clean_str

df_apps_clean["Installs"] = pandas.to_numeric(df_apps_clean["Installs"].apply(clean_string))

print(type(df_apps_clean["Installs"].values[0]))
print(df_apps_clean[['App', 'Installs']].groupby('Installs').count())

df_apps_clean["Price"] = pandas.to_numeric(df_apps_clean["Price"].apply(clean_string))
print(type(df_apps_clean["Price"].values[0]))
