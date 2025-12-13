import psycopg2
from psycopg2.extras import RealDictCursor

# ==================== USERS ====================

def get_all_users(con):
    """Fetch all users"""
    with con:
        with con.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute("SELECT * FROM users;")
            return cursor.fetchall() 