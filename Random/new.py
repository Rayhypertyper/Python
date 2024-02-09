# import sqlite3

# conn = sqlite3.connect('database.db')
# c = conn.cursor()

# c.execute("""CREATE TABLE databayo (
#     first_name text,
#     last_name text,
#     email text
# )""")

x = '1'
a = 5
while True:
      if x.isdigit():  
        if 0<int(x)<=a:
            x = int(x)
            break
print(x+2)
    
while not x.isdigit():
      x = input("Please enter a number within the range of the list")
      if x.isdigit():  
        if int(x)<a and int(x)>0:
            x = int(x)
print(x+2)