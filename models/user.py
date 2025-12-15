import psycopg2
import bcrypt

# ---------------- DATABASE CONNECTION ----------------
conn = psycopg2.connect(
    dbname="Paychat",
    user="postgres",
    password="Lastking018",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# ---------------- PASSWORD HELPERS ----------------
def hash_password(password: str) -> str:
    """Hash a plaintext password."""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed.decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Check if the password matches the hashed password."""
    return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))

# ---------------- USER FUNCTIONS ----------------
def create_user(username: str, email: str, password: str) -> bool:
    """Create a new user with hashed password."""
    try:
        hashed = hash_password(password)
        cur.execute(
            "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
            (username, email, hashed)
        )
        conn.commit()
        return True
    except psycopg2.Error as e:
        print("Database error:", e)
        return False


def get_user_by_email(email: str):
    """Retrieve a user by email."""
    cur.execute("SELECT * FROM users WHERE email = %s", (email,))
    row = cur.fetchone()
    if row:
        return {"id": row[0], "username": row[1], "email": row[2], "password": row[3]}
    return None
