import os

import psycopg2
from dotenv import load_dotenv

load_dotenv(override=True)

DATABASE_NAME = os.getenv("DATABASE_NAME")
PASSWORD = os.getenv("PASSWORD")


def get_connection():

    """
    Function that returns a single connection
    In reality, we might use a connection pool, since
    this way we'll start a new connection each time
    someone hits one of our endpoints, which isn't great for performance
    """
    return psycopg2.connect(
        dbname=DATABASE_NAME,
        user="postgres",  # change if needed
        password=PASSWORD,
        host="localhost",  # change if needed
        port="5432",  # change if needed
    )


def create_tables():
    
   
    connection = get_connection()
    cur = connection.cursor()
    
    # Create users table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id SERIAL PRIMARY KEY, 
            first_name VARCHAR(100) NOT NULL,
            last_name VARCHAR(100) NOT NULL,
            email VARCHAR(255) UNIQUE NOT NULL, 
            phone_number VARCHAR(100) NOT NULL,
            password_hash VARCHAR(255) NOT NULL,
            created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP 
        );
    """)
    
    # Create businesses table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS businesses (
            business_id SERIAL PRIMARY KEY, 
            owner_id INTEGER NOT NULL REFERENCES users(user_id),
            name VARCHAR(255) UNIQUE NOT NULL,
            business_type VARCHAR(50) NOT NULL,
            adress VARCHAR(255) NOT NULL, 
            city VARCHAR(100) NOT NULL, 
            postal_code VARCHAR(10) NOT NULL, 
            phone_number VARCHAR(20) NOT NULL,
            email VARCHAR(255) UNIQUE NOT NULL,
            description TEXT, 
            created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        );
    """)
    
    # Create staff_members
    cur.execute("""
        CREATE TABLE IF NOT EXISTS staff_members (
            staff_id SERIAL PRIMARY KEY,
            business_id INTEGER NOT NULL REFERENCES businesses(business_id),
            first_name VARCHAR(100) NOT NULL,
            last_name VARCHAR(100) NOT NULL,
            email VARCHAR(255),
            phone_number VARCHAR(100),
            role VARCHAR(100),
            is_active BOOLEAN DEFAULT true,
            created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        );
    """)
    
    # Create services table 
    cur.execute("""
        CREATE TABLE IF NOT EXISTS services (
            service_id SERIAL PRIMARY KEY,
            business_id INTEGER REFERENCES businesses(business_id) NOT NULL,
            name VARCHAR(150) NOT NULL,
            description TEXT NOT NULL, 
            price DECIMAL(10,2) NOT NULL,
            is_active BOOLEAN DEFAULT true,
            created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        );
    """)
    
    # Create staff_services 
    cur.execute("""
        CREATE TABLE IF NOT EXISTS staff_services (
            staff_service_id SERIAL PRIMARY KEY,
            staff_id INTEGER NOT NULL REFERENCES staff_members(staff_id),
            service_id INTEGER NOT NULL REFERENCES services(service_id),
            UNIQUE(staff_id, service_id)
        );
    """)
    
    # Create bookings table 
    cur.execute("""
        CREATE TABLE IF NOT EXISTS bookings (
            booking_id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(user_id) NOT NULL,
            business_id INTEGER REFERENCES businesses(business_id) NOT NULL,
            service_id INTEGER REFERENCES services(service_id) NOT NULL,
            staff_id INTEGER REFERENCES staff_members(staff_id),
            start_time TIMESTAMP WITH TIME ZONE NOT NULL, 
            end_time TIMESTAMP WITH TIME ZONE NOT NULL, 
            status VARCHAR(50) NOT NULL
        );
    """)
    
    # Create payments table 
    cur.execute("""
        CREATE TABLE IF NOT EXISTS payments (
            payment_id SERIAL PRIMARY KEY,
            booking_id INTEGER REFERENCES bookings(booking_id) NOT NULL,
            user_id INTEGER REFERENCES users(user_id) NOT NULL,
            amount DECIMAL(10, 2) NOT NULL,
            payment_method VARCHAR(50) NOT NULL,
            transaction_status VARCHAR(50) NOT NULL,
            payment_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        );
    """)
    
    # Create reviews table 
    cur.execute("""
        CREATE TABLE IF NOT EXISTS reviews (
            review_id SERIAL PRIMARY KEY,
            business_id INTEGER REFERENCES businesses(business_id) NOT NULL,
            user_id INTEGER REFERENCES users(user_id) NOT NULL,
            booking_id INTEGER REFERENCES bookings(booking_id),
            rating INTEGER CHECK (rating >= 1 AND rating <= 5) NOT NULL,
            comment TEXT,
            created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        );
    """)
    
    # Commit changes and close
    connection.commit()
    cur.close()
    connection.close()

if __name__ == "__main__":
    create_tables()
    print("Tables created successfully.")
