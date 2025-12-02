import psycopg2

con = psycopg2.connect(host = "localhost", port= "5432", user = "postgres", password= "Campmulla", dbname ="myduka_db")

cur = con.cursor()

cur.execute("select*from products")

products = cur.fetchall()
print(products)

