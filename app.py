from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Database connection
db = mysql.connector.connect(
    host="localhost",       # Change this if the database is hosted elsewhere
    user="root",            # Your MySQL username
    password="root",    # Your MySQL password
    database="user_data"    # The database you want to use
)

cursor = db.cursor()

# Create table if not exists
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(100),
        middle_name VARCHAR(100),
        last_name VARCHAR(100),
        father_name VARCHAR(100),
        mother_name VARCHAR(100)
    )
""")
db.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    first_name = request.form['fname']
    middle_name = request.form['mname']
    last_name = request.form['lname']
    father_name = request.form['fathername']
    mother_name = request.form['mothername']

    sql = "INSERT INTO users (first_name, middle_name, last_name, father_name, mother_name) VALUES (%s, %s, %s, %s, %s)"
    values = (first_name, middle_name, last_name, father_name, mother_name)
    cursor.execute(sql, values)
    db.commit()

    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090, debug=True)
