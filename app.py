from flask import Flask, render_template, request, redirect, url_for, flash, session
import mysql.connector
from mysql.connector import Error
from config import DB_CONFIG, ADMIN_USERNAME, ADMIN_PASSWORD
from functools import wraps

app = Flask(__name__)
app.secret_key = 'replace_this_with_a_random_secret'  # change for production

def get_db_conn():
    return mysql.connector.connect(**DB_CONFIG)

def admin_required(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        if not session.get('admin_logged_in'):
            return redirect(url_for('admin_login'))
        return f(*args, **kwargs)
    return wrapped

@app.route('/')
def index():
    conn = get_db_conn()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM rooms WHERE status='available'")
    rooms = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', rooms=rooms)

@app.route('/room/<int:room_id>')
def room_detail(room_id):
    conn = get_db_conn()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM rooms WHERE id=%s", (room_id,))
    room = cur.fetchone()
    cur.close()
    conn.close()
    if not room:
        flash('Room not found', 'danger')
        return redirect(url_for('index'))
    return render_template('room.html', room=room)

@app.route('/book/<int:room_id>', methods=['GET','POST'])
def book_room(room_id):
    conn = get_db_conn()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM rooms WHERE id=%s AND status='available'", (room_id,))
    room = cur.fetchone()
    if not room:
        cur.close()
        conn.close()
        flash('Room not available', 'warning')
        return redirect(url_for('index'))
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        checkin = request.form['checkin']
        checkout = request.form['checkout']
        # Insert booking
        cur.execute("""INSERT INTO bookings (room_id, customer_name, customer_email, customer_phone, check_in, check_out)
                       VALUES (%s,%s,%s,%s,%s,%s)""", (room_id, name, email, phone, checkin, checkout))
        # Mark room unavailable (simple flow)
        cur.execute("UPDATE rooms SET status='booked' WHERE id=%s", (room_id,))
        conn.commit()
        cur.close()
        conn.close()
        flash('Booking successful!', 'success')
        return redirect(url_for('index'))
    cur.close()
    conn.close()
    return render_template('book.html', room=room)

@app.route('/admin/login', methods=['GET','POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['admin_logged_in'] = True
            return redirect(url_for('admin_dashboard'))
        flash('Invalid credentials', 'danger')
    return render_template('admin_login.html')

@app.route('/admin/logout')
def admin_logout():
    session.pop('admin_logged_in', None)
    flash('Logged out', 'info')
    return redirect(url_for('admin_login'))

@app.route('/admin')
@admin_required
def admin_dashboard():
    conn = get_db_conn()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT COUNT(*) as rooms_count FROM rooms")
    rooms_count = cur.fetchone()['rooms_count']
    cur.execute("SELECT COUNT(*) as bookings_count FROM bookings")
    bookings_count = cur.fetchone()['bookings_count']
    cur.close()
    conn.close()
    return render_template('admin_dashboard.html', rooms_count=rooms_count, bookings_count=bookings_count)

@app.route('/admin/rooms')
@admin_required
def admin_rooms():
    conn = get_db_conn()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM rooms")
    rooms = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('admin_rooms.html', rooms=rooms)

@app.route('/admin/rooms/add', methods=['GET','POST'])
@admin_required
def add_room():
    if request.method == 'POST':
        number = request.form['number']
        rtype = request.form['rtype']
        price = request.form['price']
        status = request.form.get('status','available')
        conn = get_db_conn()
        cur = conn.cursor()
        cur.execute("INSERT INTO rooms (room_number, room_type, price, status) VALUES (%s,%s,%s,%s)", (number, rtype, price, status))
        conn.commit()
        cur.close()
        conn.close()
        flash('Room added', 'success')
        return redirect(url_for('admin_rooms'))
    return render_template('add_room.html')

@app.route('/admin/bookings')
@admin_required
def admin_bookings():
    conn = get_db_conn()
    cur = conn.cursor(dictionary=True)
    cur.execute("""SELECT b.*, r.room_number, r.room_type 
                   FROM bookings b JOIN rooms r ON b.room_id = r.id ORDER BY b.id DESC""")
    bookings = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('admin_bookings.html', bookings=bookings)

if __name__ == '__main__':
    app.run(debug=True)
