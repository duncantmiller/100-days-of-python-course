import pandas

df_apps = pandas.read_csv('apps.csv')
df_apps.drop(columns=['Last_Updated', 'Android_Ver'])
print(df_apps.shape)
print(df_apps.sample())
