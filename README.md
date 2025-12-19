
🏨 Hotel Management System
📌 Project Overview
The Hotel Management System is a web-based application developed to manage hotel operations such as room booking, customer details, check-in/check-out, and billing.
This system helps reduce manual work, improves efficiency, and ensures better data management through a centralized platform.
The project is built to demonstrate real-world application development using backend logic, database handling, and user-friendly interfaces.

✨ Features
🔐 User authentication (Admin/User)
🛏️ Room management (Add, update, delete rooms)
👤 Customer management
📅 Room booking & reservation system
🚪 Check-in & check-out management
💰 Billing and payment tracking
📊 Organized data storage using database
🖥️ Simple and user-friendly interface

**Contents**
- Flask web application (app.py)
- Templates (Jinja2)
- Static files (CSS)
- SQL schema and sample data (schema.sql)
- Requirements (requirements.txt)
- Project report and documentation (report.md)
- Configuration example (.env.example)

 🛠️ Technologies Used
Frontend: HTML, CSS, JavaScript
Backend: Python (Django / Flask) (use whichever applies)
Database: MySQL / SQLite
Tools: VS Code, GitHub
Version Control: Git

## How to run (local)
1. Install dependencies:
   ```
   python3 -m pip install -r requirements.txt
   ```
2. Create a MySQL database and user. Example SQL (also in `schema.sql`):
   - Database name: `hotel_db`
3. Update `config.py` or create a `.env` file from `.env.example` and put your DB credentials.
4. Run the schema:
   ```
   mysql -u root -p hotel_db < schema.sql
   ```
5. Start the app:
   ```
   python app.py
   ```
   The app runs at http://127.0.0.1:5000/

## Default admin login
- username: `admin`
- password: set in `config.py` (default: adminpass) — change before production.

## Project structure
```
hotel_management_system/
├─ app.py
├─ config.py
├─ requirements.txt
├─ templates/
├─ static/
├─ schema.sql


👩‍💻 Developer
Shubhangi Mali
📧 Email: malishubhangi552@gmail.com
🔗 LinkedIn: https://www.linkedin.com/in/shubhangi-mali-a93498331/


## Notes
- This project is a **starting point / major project template**: adapt and expand features (user auth, secure password hashing, payment gateway integration, image uploads, role-based access, validations).
- For a production-ready app, use environment variables, hashed passwords, CSRF protection, HTTPS, and input validation.
