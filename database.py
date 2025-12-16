import psycopg2

# connection
conn = psycopg2.connect(host='localhost',port='5432',user='postgres',password='Campmulla',dbname='myduka_db')

cur = conn.cursor()

# ---------------- PRODUCTS ----------------
def get_products():
    cur.execute("SELECT * FROM products")
    return cur.fetchall()


def insert_products(values):
    cur.execute(
        "INSERT INTO products(name,buying_price,selling_price) VALUES (%s,%s,%s)",
        values
    )
    conn.commit()

# ---------------- SALES ----------------
def get_sales():
    cur.execute("SELECT * FROM sales")
    return cur.fetchall()


def insert_sales(values):
    cur.execute(
        "INSERT INTO sales(pid,quantity) VALUES (%s,%s)",
        values
    )
    conn.commit()


def available_stock(pid):
    cur.execute("SELECT SUM(stock_quantity) FROM stock WHERE pid=%s", (pid,))
    total_stock = cur.fetchone()[0] or 0

    cur.execute("SELECT SUM(quantity) FROM sales WHERE pid=%s", (pid,))
    total_sold = cur.fetchone()[0] or 0

    return total_stock - total_sold


# ---------------- STOCK ----------------
def insert_stock(values):
    cur.execute(
        "INSERT INTO stock(pid,stock_quantity) VALUES (%s,%s)",
        values
    )
    conn.commit()


def get_stock():
    cur.execute("SELECT * FROM stock")
    return cur.fetchall()


# ---------------- DASHBOARD (RAW METHODS) ----------------

# SALES PER PRODUCT
def sales_per_product_raw():
    cur.execute("""
        SELECT p.name, s.quantity
        FROM sales s
        JOIN products p ON s.pid = p.id
    """)
    rows = cur.fetchall()

    result = {}
    for name, qty in rows:
        result[name] = result.get(name, 0) + qty

    return list(result.items())


# SALES PER DAY
def sales_per_day_raw():
    cur.execute("""
        SELECT DATE(created_at), quantity
        FROM sales
    """)
    rows = cur.fetchall()

    result = {}
    for date, qty in rows:
        result[date] = result.get(date, 0) + qty

    return list(result.items())


# PROFIT PER PRODUCT
def profit_per_product_raw():
    cur.execute("""
        SELECT p.name, p.buying_price, p.selling_price, s.quantity
        FROM sales s
        JOIN products p ON s.pid = p.id
    """)
    rows = cur.fetchall()

    result = {}
    for name, bp, sp, qty in rows:
        profit = (sp - bp) * qty
        result[name] = result.get(name, 0) + profit

    return list(result.items())


# PROFIT PER DAY
def profit_per_day_raw():
    cur.execute("""
        SELECT DATE(s.created_at), p.buying_price, p.selling_price, s.quantity
        FROM sales s
        JOIN products p ON s.pid = p.id
    """)
    rows = cur.fetchall()

    result = {}
    for date, bp, sp, qty in rows:
        profit = (sp - bp) * qty
        result[date] = result.get(date, 0) + profit

    return list(result.items())
