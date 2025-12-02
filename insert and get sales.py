import psycopg2


conn = psycopg2.connect(
    host="localhost",
    port="5432",
    user="postgres",
    password="Campmulla",
    dbname="myduka_db"
)
cur = conn.cursor()


def get_products():
    cur.execute("SELECT * FROM products")
    products = cur.fetchall()
    return products


def insert_product(values):
    cur.execute(
        "INSERT INTO products(name, buying_price, selling_price) VALUES (%s, %s, %s)",
        values
    )
    conn.commit()

product1 = ('Ipad', 100000, 120000)
product2 = ('Fridge', 50000, 60000)
insert_product(product1)
insert_product(product2)

products = get_products()
print(products)


cur.close()
conn.close()


