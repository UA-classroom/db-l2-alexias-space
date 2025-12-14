-- Create users table
CREATE TABLE users (
  user_id SERIAL PRIMARY KEY, 
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL, 
  phone_number VARCHAR(100) NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP 
);

-- Create salons table
CREATE TABLE salons (
  salon_id SERIAL PRIMARY KEY, 
  owner_id INTEGER NOT NULL REFERENCES users(user_id),
  name VARCHAR(255) UNIQUE NOT NULL,
  adress VARCHAR(255) NOT NULL, 
  city VARCHAR(100) NOT NULL, 
  postal_code VARCHAR(10) NOT NULL, 
  phone_number VARCHAR(20) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  description TEXT, 
  created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create services table
CREATE TABLE services (
   service_id SERIAL PRIMARY KEY,
   salon_id INTEGER REFERENCES salons(salon_id) NOT NULL,
   name VARCHAR(150) NOT NULL,
   description TEXT NOT NULL, 
   price DECIMAL(10,2) NOT NULL,
   is_active BOOLEAN DEFAULT true,
   created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create bookings table
CREATE TABLE bookings (
   booking_id SERIAL PRIMARY KEY,
   user_id INTEGER REFERENCES users(user_id) NOT NULL,
   salon_id INTEGER REFERENCES salons(salon_id) NOT NULL,
   service_id INTEGER REFERENCES services(service_id) NOT NULL,
   start_time TIMESTAMP WITH TIME ZONE NOT NULL, 
   end_time TIMESTAMP WITH TIME ZONE NOT NULL, 
   status VARCHAR(50) NOT NULL
);

-- Create payments table
CREATE TABLE payments (
    payment_id SERIAL PRIMARY KEY,
    booking_id INTEGER REFERENCES bookings(booking_id) NOT NULL,
    user_id INTEGER REFERENCES users(user_id) NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_method VARCHAR(50) NOT NULL,
    transaction_status VARCHAR(50) NOT NULL,
    payment_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create reviews table
CREATE TABLE reviews (
    review_id SERIAL PRIMARY KEY,
    salon_id INTEGER REFERENCES salons(salon_id) NOT NULL, 
    user_id INTEGER REFERENCES users(user_id) NOT NULL, 
    rating INTEGER CHECK (rating >= 1 AND rating <= 5) NOT NULL,
    comment TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);