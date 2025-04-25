from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

def get_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='shopping_data'
    )

@app.route('/')
def home():
    return redirect('/report')

@app.route('/input', methods=['GET', 'POST'])
def input_page():
    if request.method == 'POST':
        customer_id = request.form['customer_id']
        customer_name = request.form['customer_name']
        invoice_no = request.form['invoice_no']
        invoice_date = request.form['invoice_date']
        product_id = request.form['product_id']
        quantity = request.form['quantity']

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Customers (customer_id, customer_name) VALUES (%s, %s)", (customer_id, customer_name))
        cursor.execute("INSERT INTO Invoices (invoice_no, customer_id, invoice_date) VALUES (%s, %s, %s)", (invoice_no, customer_id, invoice_date))
        cursor.execute("INSERT INTO InvoiceDetails (invoice_no, product_id, quantity) VALUES (%s, %s, %s)", (invoice_no, product_id, quantity))
        conn.commit()
        conn.close()
        return redirect('/report')

    return render_template('input.html')

@app.route('/report')
def report_page():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT i.invoice_no, i.invoice_date, c.customer_id, p.product_id, d.quantity
        FROM Invoices i
        JOIN Customers c ON i.customer_id = c.customer_id
        JOIN InvoiceDetails d ON i.invoice_no = d.invoice_no
        JOIN Products p ON d.product_id = p.product_id
        ORDER BY i.invoice_date DESC
        """)
    data = cursor.fetchall()
    conn.close()
    return render_template('report.html', records=data)

if __name__ == '__main__':
    app.run(debug=True)

