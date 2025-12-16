from db_setup import get_connection

con = get_connection()
cur = con.cursor()

# Radera gamla tabeller
cur.execute("DROP TABLE IF EXISTS reviews CASCADE;")
cur.execute("DROP TABLE IF EXISTS payments CASCADE;")
cur.execute("DROP TABLE IF EXISTS bookings CASCADE;")
cur.execute("DROP TABLE IF EXISTS staff_services CASCADE;")
cur.execute("DROP TABLE IF EXISTS services CASCADE;")
cur.execute("DROP TABLE IF EXISTS staff_members CASCADE;")
cur.execute("DROP TABLE IF EXISTS businesses CASCADE;")
cur.execute("DROP TABLE IF EXISTS salons CASCADE;")
cur.execute("DROP TABLE IF EXISTS users CASCADE;")

con.commit()
print("old tabels deleted!")

cur.close()
con.close()