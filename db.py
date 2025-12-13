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
        
def update_user_db(con, user_id, user):
    """Update user (PUT - all fields)"""
    with con:
        with con.cursor(cursor_factory=RealDictCursor) as cursor:
            # Build UPDATE dynamically based on which fields exist
            updates = []
            values = []
            
            if user.first_name is not None:
                updates.append("first_name = %s")
                values.append(user.first_name)
            if user.last_name is not None:
                updates.append("last_name = %s")
                values.append(user.last_name)
            if user.email is not None:
                updates.append("email = %s")
                values.append(user.email)
            if user.phone_number is not None:
                updates.append("phone_number = %s")
                values.append(user.phone_number)
            if user.password_hash is not None:
                updates.append("password_hash = %s")
                values.append(user.password_hash)
            
            if not updates:
                raise Exception("No fields to update")
            
            values.append(user_id)
            query = f"UPDATE users SET {', '.join(updates)} WHERE user_id = %s RETURNING *;"
            cursor.execute(query, values)
            result = cursor.fetchone()
            
            if not result:
                raise Exception(f"User with id {user_id} not found")
            return result 
        
def delete_user_db(con, user_id):
    """Delete user"""
    with con:
        with con.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute("DELETE FROM users WHERE user_id = %s RETURNING user_id;", (user_id,))
            result = cursor.fetchone()
            if not result:
                raise Exception(f"User with id {user_id} not found")
            return {"message": f"User {user_id} deleted successfully"}
        
def update_user_email_db(con, user_id, email):
    """Update only email (PATCH)"""
    with con:
        with con.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(
                "UPDATE users SET email = %s WHERE user_id = %s RETURNING *;",
                (email.email, user_id)
            )
            result = cursor.fetchone()
            if not result:
                raise Exception(f"User with id {user_id} not found")
            return result
        
# ==================== SALONS ====================

def get_all_salons(con):
    """Fetch all salons"""
    with con:
        with con.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute("SELECT * FROM salons;")
            return cursor.fetchall()