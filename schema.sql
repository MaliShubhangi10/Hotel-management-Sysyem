-- MySQL schema for Hotel Management System (demo)
CREATE DATABASE IF NOT EXISTS hotel_db;
USE hotel_db;

CREATE TABLE IF NOT EXISTS rooms (
  id INT AUTO_INCREMENT PRIMARY KEY,
  room_number VARCHAR(50) NOT NULL,
  room_type VARCHAR(100),
  price DECIMAL(10,2) DEFAULT 0,
  status ENUM('available','booked') DEFAULT 'available'
);

CREATE TABLE IF NOT EXISTS bookings (
  id INT AUTO_INCREMENT PRIMARY KEY,
  room_id INT NOT NULL,
  customer_name VARCHAR(200),
  customer_email VARCHAR(200),
  customer_phone VARCHAR(50),
  check_in DATE,
  check_out DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (room_id) REFERENCES rooms(id) ON DELETE CASCADE
);

-- sample data
INSERT INTO rooms (room_number, room_type, price, status) VALUES
('101','Single',1200.00,'available'),
('102','Double',2000.00,'available'),
('201','Deluxe',3500.00,'available'),
('202','Suite',5000.00,'available');
