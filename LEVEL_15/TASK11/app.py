from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="shopping_data"
    )

@app.route('/dashboard')
def dashboard():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT MONTH(invoice_date) AS month, COUNT(DISTINCT customer_id) AS customer_count
        FROM invoices
        GROUP BY MONTH(invoice_date)
        ORDER BY month
    """)

    data = cursor.fetchall()
    conn.close()

    months = [f'Month {row[0]}' for row in data]
    counts = [row[1] for row in data]

    return render_template('dashboard.html', labels=months, values=counts)

# More routes below...

if __name__ == '__main__':
    app.run(debug=True)
