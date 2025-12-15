import psycopg2

conn = psycopg2.connect(host='localhost',port='5432',user='postgres',password='Campmulla',dbname='myduka_db')

cur = conn.cursor()


def get_products():
    cur.execute("select * from products")
    products = cur.fetchall()
    return products



def insert_products(values):
    cur.execute(f"insert into products(name,buying_price,selling_price)values{values}")
    conn.commit()


def get_sales():
    cur.execute("select * from sales")
    sales = cur.fetchall()
    return sales


def insert_sales(values):
    cur.execute(f"insert into sales(pid,quantity)values{values}")
    conn.commit()


def available_stock(pid):
    cur.execute(f'select sum(stock_quantity) from stock where pid = {pid} ')
    total_stock = cur.fetchone()[0] or 0

    cur.execute(f'select sum(quantity) from sales where pid = {pid}')
    total_sales = cur.fetchone()[0] or 0

    return total_stock - total_sales


def get_stock():
    cur.execute("SELECT id, name FROM products")
    products = cur.fetchall()  # list of tuples: (id, name)

    stock_list = []

    for pid, name in products:
        cur.execute(f'select sum(stock_quantity) from stock where pid = {pid} ')
        total_stock = cur.fetchone()[0] or 0

        cur.execute(f'select sum(quantity) from sales where pid = {pid}')
        total_sales = cur.fetchone()[0] or 0

        available = total_stock - total_sales
        stock_list.append((name, available))

    return stock_list

# fetch all users
def get_users():
    cur.execute("select * from users")
    users = cur.fetchall()
    return users

def insert_user(values):
    cur.execute(f"insert into users(username,password,email) values{values}")
    conn.commit()



