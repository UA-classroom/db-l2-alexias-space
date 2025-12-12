import os

import psycopg2
from db_setup import get_connection
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get ("/")
def home ():
    return {"message": "API is running!"}

@app.get("/users")
def get_users():
    con = get_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM users;")
    return cur.fetchall()

@app.get("/users/{user_id}")
def get_user(user_id: int):
    con = get_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE user_id = %s;", (user_id,))
    return cur.fetchone()

@app.get("/salons")
def get_salons():
    con = get_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM salons;")
    return cur.fetchall()

@app.get("/salons/{salon_id}")
def get_salon(salon_id: int):
    con = get_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM salons WHERE salon_id = %s;", (salon_id,))
    return cur.fetchone()

@app.get("/services")
def get_services():
    con = get_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM services;")
    return cur.fetchall()

@app.get("/services/{service_id}")
def get_service(service_id: int):
    con = get_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM services WHERE service_id = %s;", (service_id,))
    return cur.fetchone()

@app.get("/bookings")
def get_bookings():
    con = get_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM bookings;")
    return cur.fetchall()

@app.get("/bookings/{booking_id}")
def get_booking(booking_id: int):
    con = get_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM bookings WHERE booking_id = %s;", (booking_id,))
    return cur.fetchone()

@app.get("/payments")
def get_payments():
    con = get_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM payments;")
    return cur.fetchall()

@app.get("/payments/{payment_id}")
def get_payment(payment_id: int):
    con = get_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM payments WHERE payment_id = %s;", (payment_id,))
    return cur.fetchone()

@app.post("/users")
def create_user(user: usercreate):
    con = get_connection()
    return {"user_id": add_user(con, user)}

@app.post("/salons")
def create_salon(salon: SalonCreate):
    con = get_connection()
    return {"salon_id": add_salon(con, salon)}

@app.post("/services")
def create_service(service: ServiceCreate):
    con = get_connection()
    return {"service_id": add_service(con, service)}

@app.post("/bookings")
def create_booking(booking: BookingCreate):
    con = get_connection()
    return {"booking_id": add_booking(con, booking)}

@app.post("/payments")
def create_payment(payment: PaymentCreate):
    con = get_connection()
    return {"payment_id": add_payment(con, payment)}

@app.post("/reviews")
def create_review(review: ReviewCreate):
    con = get_connection()
    return {"review_id": add_review(con, review)}

@app.post("/salons/{salon_id}/services")
def create_service_for_salon(salon_id: int, service: ServiceCreate):
    con = get_connection()
    service.salon_id = salon_id
    return {"service_id": add_service(con, service)}

@app.post("/bookings/{booking_id}/status")
def create_booking_status(booking_id: int, status: BookingStatusCreate):
    con = get_connection()
    return update_booking_status(con, booking_id, status)

@app.post("/login")
def login_user(login: LoginCreate):
    con = get_connection()
    return login_user_db(con, login)

@app.post("/admin/salons")
def admin_create_salon(salon: SalonCreate):
    con = get_connection()
    return {"salon_id": add_salon(con, salon)}
