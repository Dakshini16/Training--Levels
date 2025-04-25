from flask import Flask, render_template
import pandas as pd
import mysql.connector

app = Flask(__name__)

# Database connection
def get_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',  # Replace with your MySQL password
        database='shopping_data'
    )

# Route: Monthly Cumulative Sales
@app.route('/monthly_sales')
def monthly_sales():
    conn = get_connection()
    query = """
        SELECT
            DATE_FORMAT(invoice_date, '%Y-%m') AS month,
            SUM(quantity * price) AS total_sales,
            SUM(SUM(quantity * price)) OVER (ORDER BY DATE_FORMAT(invoice_date, '%Y-%m')) AS cumulative_sales
        FROM Invoices
        JOIN InvoiceDetails USING(invoice_no)
        JOIN Products USING(product_id)
        GROUP BY month
        ORDER BY month;
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return render_template('monthly_sales.html', tables=[df.to_html(classes='data', header="true", index=False)])

# Route: Top 5 Customers by Category
@app.route('/top_customers')
def top_customers():
    conn = get_connection()
    query = """
        SELECT
            category,
            customer_id,
            SUM(quantity * price) AS total_spent
        FROM Invoices
        JOIN InvoiceDetails USING(invoice_no)
        JOIN Products USING(product_id)
        GROUP BY category, customer_id
        ORDER BY category, total_spent DESC;
    """
    df = pd.read_sql(query, conn)
    conn.close()
    # Get top 5 per category
    df_top5 = df.groupby("category").head(5)
    return render_template('top_customers.html', tables=[df_top5.to_html(classes='data', header="true", index=False)])
