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
    
    #Users table 
    cursor.execute("""
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
    
    # salons table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS salons (
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
    """)
    
    # services table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS services (
            service_id SERIAL PRIMARY KEY,
            salon_id INTEGER REFERENCES salons(salon_id) NOT NULL,
            name VARCHAR(150) NOT NULL,
            description TEXT NOT NULL, 
            price DECIMAL(10,2) NOT NULL,
            is_active BOOLEAN DEFAULT true,
            created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        );
    """)
    
    #bookings table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bookings (
            booking_id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(user_id) NOT NULL,
            salon_id INTEGER REFERENCES salons(salon_id) NOT NULL,
            service_id INTEGER REFERENCES services(service_id) NOT NULL,
            start_time TIMESTAMP WITH TIME ZONE NOT NULL, 
            end_time TIMESTAMP WITH TIME ZONE NOT NULL, 
            status VARCHAR(50) NOT NULL
        );
    """)
    
    #payments table
    cursor.execute("""
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
    
    # Rewiew table 
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reviews (
            review_id SERIAL PRIMARY KEY,
            salon_id INTEGER REFERENCES salons(salon_id) NOT NULL, 
            user_id INTEGER REFERENCES users(user_id) NOT NULL, 
            rating INTEGER CHECK (rating >= 1 AND rating <= 5) NOT NULL,
            comment TEXT,
            created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        );
    """)
    
    
    connection.commit()
    cursor.close()
    connection.close()












if __name__ == "__main__":
    # Only reason to execute this file would be to create new tables, meaning it serves a migration file
    create_tables()
    print("Tables created successfully.")
