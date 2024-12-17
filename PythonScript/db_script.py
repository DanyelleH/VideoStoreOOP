import psycopg2
# 172.17.0.3
import psycopg2

with psycopg2.connect(
    host="172.17.0.3",
    port="5432",  # the port on your host machine that will forward requests to 5432 in the container
    database="videostore",
    user="postgres",
    password="password") as conn:
    with conn.cursor() as cursor:
        cursor.execute("select * from MoviesAvailable")
        data = cursor.fetchall()
        for line in data:
            print(line)
    
