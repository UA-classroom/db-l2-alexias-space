from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


# ==================== USERS ====================

class UserBase(BaseModel):
    """Common fields for User"""
    first_name: str = Field(..., max_length=100)
    last_name: str = Field(..., max_length=100)
    email: str
    phone_number: str = Field(..., max_length=100)

class UserCreate(UserBase):
    """To create a new user (POST)"""
    password_hash: str = Field(..., max_length=255)

class UserUpdate(BaseModel):
    """To update users (PUT/PATCH)"""
    first_name: Optional[str] = Field(None, max_length=100)
    last_name: Optional[str] = Field(None, max_length=100)
    email: Optional[str] = None
    phone_number: Optional[str] = Field(None, max_length=100)
    password_hash: Optional[str] = Field(None, max_length=255)

class User(UserBase):
    """To return users (GET) - includes auto-generated fields"""
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True


# ==================== SALONS ====================

class SalonBase(BaseModel):
    """Common fields for Salon"""
    name: str = Field(..., max_length=255)
    adress: str = Field(..., max_length=255)
    city: str = Field(..., max_length=100)
    postal_code: str = Field(..., max_length=10)
    phone_number: str = Field(..., max_length=20)
    email: str
    description: Optional[str] = None

class SalonCreate(SalonBase):
    """To create a new salon (POST)"""
    owner_id: int

class SalonUpdate(BaseModel):
    """To update salon (PUT/PATCH)"""
    owner_id: Optional[int] = None
    name: Optional[str] = Field(None, max_length=255)
    adress: Optional[str] = Field(None, max_length=255)
    city: Optional[str] = Field(None, max_length=100)
    postal_code: Optional[str] = Field(None, max_length=10)
    phone_number: Optional[str] = Field(None, max_length=20)
    email: Optional[str] = None
    description: Optional[str] = None

class Salon(SalonBase):
    """To return salon (GET)"""
    salon_id: int
    owner_id: int
    created_at: datetime

    class Config:
        from_attributes = True


# ==================== SERVICES ====================

class ServiceBase(BaseModel):
    """Common fields for Service"""
    name: str = Field(..., max_length=150)
    description: str
    price: float = Field(..., gt=0)  
    is_active: bool = True

class ServiceCreate(ServiceBase):
    """To create a new service (POST)"""
    salon_id: int

class ServiceUpdate(BaseModel):
    """To update service (PUT/PATCH)"""
    salon_id: Optional[int] = None
    name: Optional[str] = Field(None, max_length=150)
    description: Optional[str] = None
    price: Optional[float] = Field(None, gt=0)
    is_active: Optional[bool] = None

class Service(ServiceBase):
    """To return service (GET)"""
    service_id: int
    salon_id: int
    created_at: datetime

    class Config:
        from_attributes = True


# ==================== BOOKINGS ====================

class BookingBase(BaseModel):
    """Common fields for Booking"""
    start_time: datetime
    end_time: datetime
    status: str = Field(..., max_length=50)

class BookingCreate(BookingBase):
    """To create a new booking (POST)"""
    user_id: int
    salon_id: int
    service_id: int

class BookingUpdate(BaseModel):
    """To update booking (PUT/PATCH)"""
    user_id: Optional[int] = None
    salon_id: Optional[int] = None
    service_id: Optional[int] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    status: Optional[str] = Field(None, max_length=50)

class Booking(BookingBase):
    """To return booking (GET)"""
    booking_id: int
    user_id: int
    salon_id: int
    service_id: int

    class Config:
        from_attributes = True


# ==================== PAYMENTS ====================

class PaymentBase(BaseModel):
    """Common fields for Payment"""
    amount: float = Field(..., gt=0)
    payment_method: str = Field(..., max_length=50)
    transaction_status: str = Field(..., max_length=50)

class PaymentCreate(PaymentBase):
    """To create a new payment (POST)"""
    booking_id: int
    user_id: int

class PaymentUpdate(BaseModel):
    """To update payment (PUT/PATCH)"""
    booking_id: Optional[int] = None
    user_id: Optional[int] = None
    amount: Optional[float] = Field(None, gt=0)
    payment_method: Optional[str] = Field(None, max_length=50)
    transaction_status: Optional[str] = Field(None, max_length=50)

class Payment(PaymentBase):
    """To return payment (GET)"""
    payment_id: int
    booking_id: int
    user_id: int
    payment_date: datetime

    class Config:
        from_attributes = True


# ==================== REVIEWS ====================

class ReviewBase(BaseModel):
    """Common fields for Review"""
    rating: int = Field(..., ge=1, le=5)  # Mellan 1-5
    comment: Optional[str] = None

class ReviewCreate(ReviewBase):
    """Common fields for Review"""
    salon_id: int
    user_id: int

class ReviewUpdate(BaseModel):
    """To update review (PUT/PATCH)"""
    salon_id: Optional[int] = None
    user_id: Optional[int] = None
    rating: Optional[int] = Field(None, ge=1, le=5)
    comment: Optional[str] = None

class Review(ReviewBase):
    """To return review (GET)"""
    review_id: int
    salon_id: int
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True
