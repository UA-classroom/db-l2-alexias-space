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
        
def get_salon_by_id(con, salon_id):
    """Fetch a specific salon"""
    with con:
        with con.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute("SELECT * FROM salons WHERE salon_id = %s;", (salon_id,))
            salon = cursor.fetchone()
            if not salon:
                raise Exception(f"Salon with id {salon_id} not found")
            return salon
        
def add_salon(con, salon):
    """Create new salon"""
    with con:
        with con.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(
                """
                INSERT INTO salons (owner_id, name, adress, city, postal_code, phone_number, email, description)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING salon_id;
                """,
                (salon.owner_id, salon.name, salon.adress, salon.city, 
                 salon.postal_code, salon.phone_number, salon.email, salon.description)
            )
            result = cursor.fetchone()
            return result["salon_id"]
        
def update_salon_db(con, salon_id, salon):
    """Update salon"""
    with con:
        with con.cursor(cursor_factory=RealDictCursor) as cursor:
            updates = []
            values = []
            
            if salon.owner_id is not None:
                updates.append("owner_id = %s")
                values.append(salon.owner_id)
            if salon.name is not None:
                updates.append("name = %s")
                values.append(salon.name)
            if salon.adress is not None:
                updates.append("adress = %s")
                values.append(salon.adress)
            if salon.city is not None:
                updates.append("city = %s")
                values.append(salon.city)
            if salon.postal_code is not None:
                updates.append("postal_code = %s")
                values.append(salon.postal_code)
            if salon.phone_number is not None:
                updates.append("phone_number = %s")
                values.append(salon.phone_number)
            if salon.email is not None:
                updates.append("email = %s")
                values.append(salon.email)
            if salon.description is not None:
                updates.append("description = %s")
                values.append(salon.description)
            
            if not updates:
                raise Exception("No fields to update")
            
            values.append(salon_id)
            query = f"UPDATE salons SET {', '.join(updates)} WHERE salon_id = %s RETURNING *;"
            cursor.execute(query, values)
            result = cursor.fetchone()
            
            if not result:
                raise Exception(f"Salon with id {salon_id} not found")
            return result
        

def delete_salon_db(con, salon_id):
    """Delete salon"""
    with con:
        with con.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute("DELETE FROM salons WHERE salon_id = %s RETURNING salon_id;", (salon_id,))
            result = cursor.fetchone()
            if not result:
                raise Exception(f"Salon with id {salon_id} not found")
            return {"message": f"Salon {salon_id} deleted successfully"}

# ==================== SERVICES ====================

def get_all_services(con):
    """Fetch all services"""
    with con:
        with con.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute("SELECT * FROM services;")
            return cursor.fetchall()
        
def get_service_by_id(con, service_id):
    """Fetch a specific service"""
    with con:
        with con.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute("SELECT * FROM services WHERE service_id = %s;", (service_id,))
            service = cursor.fetchone()
            if not service:
                raise Exception(f"Service with id {service_id} not found")
            return service
        
def add_service(con, service):
    """Create new service"""
    with con:
        with con.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(
                """
                INSERT INTO services (salon_id, name, description, price, is_active)
                VALUES (%s, %s, %s, %s, %s)
                RETURNING service_id;
                """,
                (service.salon_id, service.name, service.description, service.price, service.is_active)
            )
            result = cursor.fetchone()
            return result["service_id"]
        
def update_service_db(con, service_id, service):
    """Update service"""
    with con:
        with con.cursor(cursor_factory=RealDictCursor) as cursor:
            updates = []
            values = []
            
            if service.salon_id is not None:
                updates.append("salon_id = %s")
                values.append(service.salon_id)
            if service.name is not None:
                updates.append("name = %s")
                values.append(service.name)
            if service.description is not None:
                updates.append("description = %s")
                values.append(service.description)
            if service.price is not None:
                updates.append("price = %s")
                values.append(service.price)
            if service.is_active is not None:
                updates.append("is_active = %s")
                values.append(service.is_active)
            
            if not updates:
                raise Exception("No fields to update")
            
            values.append(service_id)
            query = f"UPDATE services SET {', '.join(updates)} WHERE service_id = %s RETURNING *;"
            cursor.execute(query, values)
            result = cursor.fetchone()
            
            if not result:
                raise Exception(f"Service with id {service_id} not found")
            return result
