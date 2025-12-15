import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",   # connect to default db temporarily
    user="postgres",
    password="Lastking018"
)

cur = conn.cursor()
cur.execute("SELECT datname FROM pg_database;")
rows = cur.fetchall()

for r in rows:
    print(r)

cur.close()
conn.close()
