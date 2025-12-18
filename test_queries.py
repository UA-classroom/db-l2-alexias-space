from db_setup import get_connection

con = get_connection()
cur = con.cursor()


cur.execute("""
    SELECT table_name 
    FROM information_schema.tables 
    WHERE table_schema='public'
    ORDER BY table_name
""")
print("Tabeller:", cur.fetchall())


cur.execute("SELECT * FROM users;")
print("\nUsers:", cur.fetchall())


cur.execute("SELECT * FROM businesses;")
print("\nBusinesses:", cur.fetchall())


cur.execute("SELECT * FROM staff_members;")
print("\nStaff Members:", cur.fetchall())


cur.execute("SELECT * FROM services;")
print("\nServices:", cur.fetchall())

cur.close()
con.close()