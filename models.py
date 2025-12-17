import psycopg2
from psycopg2.extras import RealDictCursor
import bcrypt

# DATABASE CONNECTION 
def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="paychat_db",  # change to your database name
        user="postgres",        # change to your PostgreSQL username
        password="yourpassword" # change to your PostgreSQL password
    )
    return conn

# CREATE USER 
def create_user(username, email, password):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)

        # Hash the password
        hashed_pw = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

        # Insert user into DB
        cursor.execute(
            "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
            (username, email, hashed_pw)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        print("Error creating user:", e)
        return False

# GET USER BY EMAIL 
def get_user_by_email(email):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        return user
    except Exception as e:
        print("Error fetching user:", e)
        return None

# VERIFY PASSWORD 
import bcrypt


def hash_password(plain_password):
    return bcrypt.hashpw(plain_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
