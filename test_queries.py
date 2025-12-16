from db_setup import get_connection

con = get_connection()
cur = con.cursor()


cur.execute("""
    SELECT table_name 
    FROM information_schema.tables 
    WHERE table_schema='public'
""")
print("Tabeller:", cur.fetchall())


cur.execute("SELECT * FROM users;")
print("Users:", cur.fetchall())


cur.execute("SELECT * FROM salons;")
print("Salons:", cur.fetchall())

cur.close()
con.close()