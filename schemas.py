from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field, ConfigDict


class ORMBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)



class UserBase(ORMBase):
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(..., min_length=1, max_length=50)
    email: EmailStr
    phone: Optional[str] = Field(default=None, max_length=30)


class UserCreate(UserBase):
    password: str = Field(..., min_length=6, max_length=128)


class UserUpdate(ORMBase):
    first_name: Optional[str] = Field(default=None, min_length=1, max_length=50)
    last_name: Optional[str] = Field(default=None, min_length=1, max_length=50)
    email: Optional[EmailStr] = None
    phone: Optional[str] = Field(default=None, max_length=30)
    password: Optional[str] = Field(default=None, min_length=6, max_length=128)


class UserOut(UserBase):
    user_id: int
    created_at: Optional[datetime] = None



class ListingBase(ORMBase):
    title: str = Field(..., min_length=1, max_length=120)
    description: Optional[str] = Field(default=None, max_length=5000)
    price: float = Field(..., ge=0)
    city: Optional[str] = Field(default=None, max_length=80)


class ListingCreate(ListingBase):
    user_id: int


class ListingUpdate(ORMBase):
    title: Optional[str] = Field(default=None, min_length=1, max_length=120)
    description: Optional[str] = Field(default=None, max_length=5000)
    price: Optional[float] = Field(default=None, ge=0)
    city: Optional[str] = Field(default=None, max_length=80)


class ListingOut(ListingBase):
    listing_id: int
    user_id: int
    created_at: Optional[datetime] = None



class ReviewBase(ORMBase):
    rating: int = Field(..., ge=1, le=5)
    comment: Optional[str] = Field(default=None, max_length=2000)


class ReviewCreate(ReviewBase):
    reviewer_user_id: int
    reviewed_user_id: int


class ReviewUpdate(ORMBase):
    rating: Optional[int] = Field(default=None, ge=1, le=5)
    comment: Optional[str] = Field(default=None, max_length=2000)


class ReviewOut(ReviewBase):
    review_id: int
    reviewer_user_id: int
    reviewed_user_id: int
    created_at: Optional[datetime] = None


class MessageBase(ORMBase):
    content: str = Field(..., min_length=1, max_length=4000)


class MessageCreate(MessageBase):
    sender_user_id: int
    receiver_user_id: int


class MessageUpdate(ORMBase):
    content: Optional[str] = Field(default=None, min_length=1, max_length=4000)


class MessageOut(MessageBase):
    message_id: int
    sender_user_id: int
    receiver_user_id: int
    created_at: Optional[datetime] = None
