from fastapi import FastAPI, HTTPException
from db_setup import get_connection
from schema import (
    UserCreate, User, UserUpdate,
    SalonCreate, Salon, SalonUpdate,
    ServiceCreate, Service, ServiceUpdate,
    BookingCreate, Booking, BookingUpdate,
    PaymentCreate, Payment, PaymentUpdate,
    ReviewCreate, Review, ReviewUpdate
)
import db

app = FastAPI()

#HOME 
   
@app.get("/")
def home():
    return {"message": "Booking System API is running!"}


# USERS

@app.get("/users", response_model=list[User])
def get_users():
    """Fetch all users"""
    try:
        con = get_connection()
        return db.get_all_users(con)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    """Fetch a specific user"""
    try:
        con = get_connection()
        return db.get_user_by_id(con, user_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.post("/users", response_model=dict)
def create_user(user: UserCreate):
    """Create new user"""
    try:
        con = get_connection()
        user_id = db.add_user(con, user)
        return {"user_id": user_id, "message": "User created successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user: UserUpdate):
    """Update user"""
    try:
        con = get_connection()
        return db.update_user_db(con, user_id, user)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    """Delete user"""
    try:
        con = get_connection()
        return db.delete_user_db(con, user_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


#SALONS 

@app.get("/salons", response_model=list[Salon])
def get_salons():
    """Fetch all salons"""
    try:
        con = get_connection()
        return db.get_all_salons(con)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/salons/{salon_id}", response_model=Salon)
def get_salon(salon_id: int):
    """Fetch a specific salon"""
    try:
        con = get_connection()
        return db.get_salon_by_id(con, salon_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.post("/salons", response_model=dict)
def create_salon(salon: SalonCreate):
    """Create new salon"""
    try:
        con = get_connection()
        salon_id = db.add_salon(con, salon)
        return {"salon_id": salon_id, "message": "Salon created successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.put("/salons/{salon_id}", response_model=Salon)
def update_salon(salon_id: int, salon: SalonUpdate):
    """Update salon"""
    try:
        con = get_connection()
        return db.update_salon_db(con, salon_id, salon)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.delete("/salons/{salon_id}")
def delete_salon(salon_id: int):
    """Delete salon"""
    try:
        con = get_connection()
        return db.delete_salon_db(con, salon_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


#SERVICES

@app.get("/services", response_model=list[Service])
def get_services():
    """Fetch all services"""
    try:
        con = get_connection()
        return db.get_all_services(con)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/services/{service_id}", response_model=Service)
def get_service(service_id: int):
    """Fetch a specific service"""
    try:
        con = get_connection()
        return db.get_service_by_id(con, service_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.post("/services", response_model=dict)
def create_service(service: ServiceCreate):
    """Create new service"""
    try:
        con = get_connection()
        service_id = db.add_service(con, service)
        return {"service_id": service_id, "message": "Service created successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.put("/services/{service_id}", response_model=Service)
def update_service(service_id: int, service: ServiceUpdate):
    """Update service"""
    try:
        con = get_connection()
        return db.update_service_db(con, service_id, service)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.delete("/services/{service_id}")
def delete_service(service_id: int):
    """Delete service"""
    try:
        con = get_connection()
        return db.delete_service_db(con, service_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.post("/salons/{salon_id}/services", response_model=dict)
def create_service_for_salon(salon_id: int, service: ServiceCreate):
    """Create service for specific salon"""
    try:
        con = get_connection()
        service.salon_id = salon_id  # Set salon_id automatically
        service_id = db.add_service(con, service)
        return {"service_id": service_id, "message": f"Service created for salon {salon_id}"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


#BOOKINGS

@app.get("/bookings", response_model=list[Booking])
def get_bookings():
    """Fetch all bookings"""
    try:
        con = get_connection()
        return db.get_all_bookings(con)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/bookings/{booking_id}", response_model=Booking)
def get_booking(booking_id: int):
    """Fetch a specific booking"""
    try:
        con = get_connection()
        return db.get_booking_by_id(con, booking_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.post("/bookings", response_model=dict)
def create_booking(booking: BookingCreate):
    """Create new booking"""
    try:
        con = get_connection()
        booking_id = db.add_booking(con, booking)
        return {"booking_id": booking_id, "message": "Booking created successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.put("/bookings/{booking_id}", response_model=Booking)
def update_booking(booking_id: int, booking: BookingUpdate):
    """Update booking"""
    try:
        con = get_connection()
        return db.update_booking_db(con, booking_id, booking)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.delete("/bookings/{booking_id}")
def delete_booking(booking_id: int):
    """Delete booking"""
    try:
        con = get_connection()
        return db.delete_booking_db(con, booking_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


#PAYMENTS

@app.get("/payments", response_model=list[Payment])
def get_payments():
    """Fetch all payments"""
    try:
        con = get_connection()
        return db.get_all_payments(con)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/payments/{payment_id}", response_model=Payment)
def get_payment(payment_id: int):
    """Fetch a specific payment"""
    try:
        con = get_connection()
        return db.get_payment_by_id(con, payment_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.post("/payments", response_model=dict)
def create_payment(payment: PaymentCreate):
    """Create new payment"""
    try:
        con = get_connection()
        payment_id = db.add_payment(con, payment)
        return {"payment_id": payment_id, "message": "Payment created successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.put("/payments/{payment_id}", response_model=Payment)
def update_payment(payment_id: int, payment: PaymentUpdate):
    """Update payment"""
    try:
        con = get_connection()
        return db.update_payment_db(con, payment_id, payment)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.delete("/payments/{payment_id}")
def delete_payment(payment_id: int):
    """Delete payment"""
    try:
        con = get_connection()
        return db.delete_payment_db(con, payment_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


#REVIEWS

@app.get("/reviews", response_model=list[Review])
def get_reviews():
    """Fetch all reviews"""
    try:
        con = get_connection()
        return db.get_all_reviews(con)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/reviews/{review_id}", response_model=Review)
def get_review(review_id: int):
    """Fetch a specific review"""
    try:
        con = get_connection()
        return db.get_review_by_id(con, review_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.post("/reviews", response_model=dict)
def create_review(review: ReviewCreate):
    """Create new review"""
    try:
        con = get_connection()
        review_id = db.add_review(con, review)
        return {"review_id": review_id, "message": "Review created successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.put("/reviews/{review_id}", response_model=Review)
def update_review(review_id: int, review: ReviewUpdate):
    """Update review"""
    try:
        con = get_connection()
        return db.update_review_db(con, review_id, review)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.delete("/reviews/{review_id}")
def delete_review(review_id: int):
    """Delete review"""
    try:
        con = get_connection()
        return db.delete_review_db(con, review_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


#PATCH ENDPOINTS (Partial updates)

from pydantic import BaseModel

class UpdateEmail(BaseModel):
    email: str

class UpdateStatus(BaseModel):
    status: str

@app.patch("/users/{user_id}/email", response_model=User)
def update_user_email(user_id: int, email: UpdateEmail):
    """Update only email for user"""
    try:
        con = get_connection()
        return db.update_user_email_db(con, user_id, email)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.patch("/bookings/{booking_id}/status", response_model=Booking)
def update_booking_status(booking_id: int, status: UpdateStatus):
    """Update only status for booking"""
    try:
        con = get_connection()
        return db.update_booking_status_db(con, booking_id, status)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


#SPECIAL ENDPOINTS

class LoginCreate(BaseModel):
    email: str
    password_hash: str

@app.post("/login")
def login_user(login: LoginCreate):
    """Login endpoint"""
    try:
        con = get_connection()
        return db.login_user_db(con, login)
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))

@app.post("/admin/salons", response_model=dict)
def admin_create_salon(salon: SalonCreate):
    """Admin endpoint to create salon"""
    try:
        con = get_connection()
        salon_id = db.add_salon(con, salon)
        return {"salon_id": salon_id, "message": "Salon created by admin"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))