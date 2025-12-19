# Major Project Report — Hotel Management System (Flask + MySQL)

## 1. Introduction
This Hotel Management System is a web application built using Flask (Python) and MySQL. It helps manage rooms, customer bookings, and generates simple reports for administrators.

## 2. Objectives
- Manage room inventory.
- Allow customers to view and book rooms.
- Admin can add rooms and view bookings.

## 3. Features
- Customer: view rooms, room details, book rooms.
- Admin: login (demo), add rooms, view all bookings.
- Database persistence using MySQL.

## 4. System Design
- Frontend: Jinja2 templates for server-side rendering.
- Backend: Flask routes handling business logic.
- Database: MySQL with two main tables (rooms, bookings).

## 5. Database Schema
See `schema.sql` for table definitions and sample data.

## 6. How to Use
1. Create database and run schema.sql.
2. Configure DB credentials in `.env` or `config.py`.
3. Run `python app.py`.
4. Access via browser: `http://127.0.0.1:5000/`.

## 7. Improvements & Further Work
- Add user authentication and registration.
- Use hashed passwords and role-based access control.
- Add file uploads for room images.
- Integrate payment gateway.
- Add tests and CI/CD.

## 8. Conclusion
This project provides a solid foundation for a more feature-rich hotel management system and can be used as a major project base for academic submissions.
