import psycopg2
from psycopg2.extras import RealDictCursor

def get_db():
    """
    Returns a connection to the Paychat PostgreSQL database
    """
    return psycopg2.connect(
        host="localhost",
        database="Paychat",
        user="postgres",
        password="Lastking018",
        cursor_factory=RealDictCursor
    )