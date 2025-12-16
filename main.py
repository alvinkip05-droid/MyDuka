from flask import Flask, render_template, request, redirect, url_for, flash
from database import (get_products,get_sales,insert_products,insert_sales,available_stock,get_stock as fetch_stock_from_db,insert_stock,sales_per_product_raw,sales_per_day_raw,profit_per_product_raw,profit_per_day_raw
)

app = Flask(__name__)
app.secret_key = '56709chhe88dhnwjwkixsiixk'


# ---------------- HOME ----------------
@app.route("/")
def home():
    return render_template("index.html")


# ---------------- PRODUCTS ----------------
@app.route('/products')
def fetch_products():
    products = get_products()
    return render_template("products.html", products=products)


@app.route('/add_products', methods=['POST'])
def add_products():
    product_name = request.form["product_name"]
    buying_price = request.form["buying_price"]
    selling_price = request.form["selling_price"]

    insert_products((product_name, buying_price, selling_price))
    flash("Product added successfully", "success")

    return redirect(url_for('fetch_products'))


# ---------------- SALES ----------------
@app.route('/sales')
def fetch_sales():
    sales = get_sales()
    products = get_products()
    return render_template("sales.html", sales=sales, products=products)


@app.route('/add_sale', methods=['POST'])
def add_sale():
    pid = request.form["pid"]
    quantity = float(request.form["quantity"])

    if available_stock(pid) < quantity:
        flash("Insufficient stock", "danger")
        return redirect(url_for('fetch_sales'))

    insert_sales((pid, quantity))
    flash("Sale made successfully", "success")

    return redirect(url_for('fetch_sales'))


# ---------------- STOCK ----------------
@app.route('/stock')
def get_stock():
    stock = fetch_stock_from_db()
    products = get_products()
    return render_template("stock.html", stock=stock, products=products)


@app.route('/add_stock', methods=['POST'])
def add_stock():
    pid = request.form['pid']
    stock_quantity = request.form['s_quantity']

    insert_stock((pid, stock_quantity))
    flash("Stock added successfully", "success")

    return redirect(url_for('get_stock'))


# ---------------- DASHBOARD ----------------
@app.route('/dashboard')
def dashboard():
    return render_template(
        "dashboard.html",
        sales_per_product=sales_per_product_raw(),
        sales_per_day=sales_per_day_raw(),
        profit_per_product=profit_per_product_raw(),
        profit_per_day=profit_per_day_raw()
    )


# ---------------- AUTH ----------------
@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")


# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)
