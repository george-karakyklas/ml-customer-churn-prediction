import pandas as pd
import sqlite3

# Load CSV
df = pd.read_csv('telco_churn.csv')

# Create SQLite database (or connect if exists)
conn = sqlite3.connect('telco_churn.db')

# Write DataFrame to SQL table
df.to_sql('telco_customers', conn, if_exists='replace', index=False)

# Confirm table exists (optional)
print(pd.read_sql("SELECT * FROM telco_customers LIMIT 5;", conn))

conn.close()