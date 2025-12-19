# Hotel Management System (Flask + MySQL)

**Contents**
- Flask web application (app.py)
- Templates (Jinja2)
- Static files (CSS)
- SQL schema and sample data (schema.sql)
- Requirements (requirements.txt)
- Project report and documentation (report.md)
- Configuration example (.env.example)

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
├─ report.md
```

## Notes
- This project is a **starting point / major project template**: adapt and expand features (user auth, secure password hashing, payment gateway integration, image uploads, role-based access, validations).
- For a production-ready app, use environment variables, hashed passwords, CSRF protection, HTTPS, and input validation.
