import pandas

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
