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
print(df_apps_clean[["App", "Installs"]].groupby("Installs").count())

df_apps_clean["Price"] = pandas.to_numeric(df_apps_clean["Price"].apply(clean_string))
print(type(df_apps_clean["Price"].values[0]))
df_apps_clean["Revenue"] = df_apps_clean["Price"] * df_apps_clean["Installs"]
print(df_apps_clean.sort_values("Revenue", ascending=False).head(10))
df_apps_clean = df_apps_clean[df_apps_clean['Price'] < 250]
print(df_apps_clean.sort_values("Revenue", ascending=False).head(10))

top_10_category = df_apps_clean["Category"].value_counts().head(10)
print(top_10_category)

bar = plotly.bar(x=top_10_category.index, y=top_10_category.values)
# bar.show()

category_installs = df_apps_clean.groupby("Category").agg({"Installs": pandas.Series.sum})
apps_per_category = df_apps_clean.groupby("Category").agg({"App": pandas.Series.count})
new_df = category_installs.merge(apps_per_category, on="Category", how="inner")

# h_bar = plotly.bar(x=category_installs["Installs"], y=category_installs.index, orientation="h", title='Category Popularity')
# h_bar.update_layout(xaxis_title="Number of Downloads", yaxis_title="Category")

# h_bar.show()

print(new_df)

# scatter = plotly.scatter(
#     new_df,
#     x="App",
#     y="Installs",
#     title="Category concentration",
#     size="App",
#     hover_name=new_df.index,
#     color="Installs"
# )

# scatter.update_layout(
#     xaxis_title="Number of Apps",
#     yaxis_title="Installs",
#     yaxis=dict(type="log")
# )

# scatter.show()

genre_stack = df_apps_clean["Genres"].str.split(';', expand=True).stack(future_stack=True)
print(genre_stack.value_counts())
value_counts = genre_stack.value_counts()
# bar = plotly.bar(
#     x=value_counts.index,
#     y=value_counts.values,
#     title="Genres",
#     hover_name=value_counts.index,
#     color=value_counts.values,
#     color_continuous_scale='Agsunset'
# )
# bar.update_layout(
#     xaxis_title="Genre",
#     yaxis_title="Number of Apps",
#     coloraxis_showscale=False,
#     xaxis_tickangle=45
# )
# bar.show()

box = plotly.box(df_apps_clean,
             y='Installs',
             x='Type',
             color='Type',
             notched=True,
             points='all',
             title='How Many Downloads are Paid Apps Giving Up?')

box.update_layout(yaxis=dict(type='log'))

box.show()
