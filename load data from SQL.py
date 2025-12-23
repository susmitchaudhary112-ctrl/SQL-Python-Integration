import psycopg2
import pandas as pd
conn = psycopg2.connect(
    host = "localhost",
    port = "5432",
    dbname = "postgres",
    user = "postgres",
    password = "9921"
)
df = pd.read_sql("select * from public.balance_sheet;", conn)
print(df)
conn.close()