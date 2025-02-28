import psycopg2
from .Customer import Customer

conn = psycopg2.connect(
    host="172.17.0.3",
    port="5432",  # the port on your host machine that will forward requests to 5432 in the container
    database="videostore",
    user="postgres",
    password="password")

customers=[]
cursor = conn.cursor()
cursor.execute("select id,account_type,first_name,last_name from Customer JOIN ")
data = cursor.fetchall()
for row in data:
    customer = Customer(id=row[0],account_type=row[1],first_name=row[2],last_name=row[3])
    print(customers)