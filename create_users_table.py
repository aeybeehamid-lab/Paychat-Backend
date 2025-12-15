import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="Paychat",
    user="postgres",
    password="Lastking018"
)

cur = conn.cursor()

# First, list existing tables
cur.execute("""
    SELECT table_schema, table_name
    FROM information_schema.tables
    WHERE table_catalog = current_database()
      AND table_schema NOT IN ('pg_catalog','information_schema')
    ORDER BY table_schema, table_name;
""")

print("Existing tables:")
rows = cur.fetchall()
if rows:
    for row in rows:
        print(f"  {row[0]}.{row[1]}")
else:
    print("  (none)")

# Create users table if it doesn't exist
print("\nCreating users table...")
cur.execute("""
CREATE TABLE IF NOT EXISTS public.users (
    id SERIAL PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    email TEXT,
    created_at TIMESTAMPTZ DEFAULT now()
);
""")
conn.commit()
print("Done! users table ready.")

cur.close()
conn.close()