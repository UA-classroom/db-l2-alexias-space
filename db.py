import psycopg2
from psycopg2.extras import RealDictCursor

# ==================== USERS ====================

def get_all_users(con):
    """Fetch all users"""
    with con:
        with con.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute("SELECT * FROM users;")
            return cursor.fetchall() 
        
def get_user_by_id(con, user_id):
    """Fetch a specific user"""
    with con:
        with con.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute("SELECT * FROM users WHERE user_id = %s;", (user_id,))
            user = cursor.fetchone()
            if not user:
                raise Exception(f"User with id {user_id} not found")
            return user
        
def add_user(con, user):
    """Create new user"""
    with con:
        with con.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(
                """
                INSERT INTO users (first_name, last_name, email, phone_number, password_hash)
                VALUES (%s, %s, %s, %s, %s)
                RETURNING user_id;
                """,
                (user.first_name, user.last_name, user.email, user.phone_number, user.password_hash)
            )
            result = cursor.fetchone()
            return result["user_id"]