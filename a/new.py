import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute("""CREATE TABLE databayo (
    first_name text,
    last_name text,
    email text
)""")

a = ["A", "B", "c"]

print(a)

for x in a:
    print(x)