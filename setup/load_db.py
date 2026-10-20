import pandas as pd
import sqlite3

# create a db called yc_startups.db
conn = sqlite3.connect("data/yc_startups.db")
cursor = conn.cursor()

# load csv file into a pandas dataframe
df = pd.read_csv('data/yc_companies_2026-05-07.csv')

# observe contents
print(df.head())
print(df.columns)
print(df.shape)

# place into sqlite database
df.to_sql('yc_companies', conn, if_exists='replace', index=False)