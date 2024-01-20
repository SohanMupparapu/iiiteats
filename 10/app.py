from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)
DATABASE = 'mydatabase.db'

@app.route('/')
def function():
    return render_template('homepage.html')

@app.route('/add', methods=['POST'])
def add_data():
    status = "not started"
    canteen_name=request.form['category']
   
    name = request.form['name']
    email = request.form['email']
    order_rate = request.form['order_rate']
    location_var = request.form['location']
    order_type =request.form['order_type']
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (status TEXT,name TEXT, email TEXT,order_rate TEXT,location_var TEXT, order_type TEXT,canteen_name TEXT)")
    conn.commit()
    cursor.execute("INSERT INTO users (status,name, email,order_rate,location_var, order_type, canteen_name) VALUES (?,?, ?,?,?,?,?)", (status,name, email,order_rate,location_var,order_type,canteen_name))
    conn.commit()
    # cursor.execute("CREATE TABLE IF NOT EXISTS current_order (item_name TEXT NOT NULL)")
    
    # cursor.execute("INSERT INTO  current_order (item_name) VALUES (?)", ())

  
    conn.close()

    return redirect('/orders')
@app.route('/home')
def home():
    return render_template('homepage.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/order')
def order():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()

    orders = []
    for row in rows:
        order = {
            "status": row[0],
            "name": row[1],
            "email": row[2],
            "order_rate": row[3],
            "location_var": row[4],
            "order_type" : row[5],
            "canteen_name" : row[6]
        }

        orders.append(order)

    return render_template('order.html', orders=orders)


@app.route('/orders')
def show_orders():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()

    orders = []
    for row in rows:
        order = {
            "status": row[0],
            "name": row[1],
            "email": row[2],
            "order_rate": row[3],
            "location_var": row[4],
            "order_type" : row[5],
            "canteen_name" : row[6]

        }
        orders.append(order)

    return render_template('order.html', orders=orders)

if __name__ == '__main__':
    app.run(debug=True)
