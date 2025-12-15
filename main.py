from flask import Flask, render_template, request, redirect, url_for
from database import (
    get_products, get_sales, insert_products, insert_sales,
    get_stock, available_stock,
    get_users, insert_user,
)

#Flask instance
app = Flask(__name__)

#index route
@app.route("/")
def home():
    return render_template("index.html") 


#getting products
@app.route('/products')
def fetch_products():
    products = get_products()
    return render_template("products.html",products=products)


#posting products
@app.route('/add_products',methods=['GET','POST'])
def add_products():
    product_name = request.form["product_name"]
    buying_price = request.form["buying_price"]
    selling_price =request.form["selling_price"]
    new_product = (product_name,buying_price,selling_price)
    insert_products(new_product)
    return redirect(url_for('fetch_products'))


#getting sales
@app.route('/sales')
def fetch_sales():
    sales = get_sales()
    products = get_products()
    return render_template("sales.html",sales=sales,products = products)


#posting sales
@app.route('/add_sale',methods=['GET','POST'])
def add_sale():
    pid = request.form["pid"]
    quantity = request.form["quantity"]
    new_sale = (pid,quantity)
    check_stock = available_stock(pid) 
    if check_stock < quantity:
        print("Insufficient stock")
        return redirect(url_for('fetch_sales'))
    insert_sales(new_sale)
    return redirect(url_for('fetch_sales'))



@app.route('/stock')
def fetch_stock():
    stock = get_stock()
    products = get_products()
    return render_template("stock.html", stock=stock, products=products)

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")


@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    users = get_users()  # fetch all users from DB
    return render_template("register.html", users=users)

@app.route("/add_user", methods=['POST'])
def add_user():
    username = request.form["username"]
    password = request.form["password"]
    email = request.form["email"]

    # Use your insert_user function from database.py
    insert_user((username, password, email))
    
    return redirect(url_for('register'))


app.run(debug=True)


