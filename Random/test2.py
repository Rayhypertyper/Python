from tkinter import *
import sqlite3


root = Tk()
root.title('databazio')
root.geometry("400x400")
conn = sqlite3.connect('database.db')
c = conn.cursor()

# c.execute("""CREATE TABLE addresses (
#     first_name text,
#     last_name,
#     city text,
#     country text,
#     fav_num integer
# )""")
def submit():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :city, :country, :fav_num)",
        {
            'f_name':f_name.get(),
            'l_name':l_name.get(),
            'city':city.get(),
            'country':country.get(),
            'fav_num':fav_num.get()
        }
    
    )
    conn.commit()
    conn.close()

    f_name.delete(0, END)
    l_name.delete(0, END)
    city.delete(0, END)
    country.delete(0, END)
    fav_num.delete(0, END)

f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)

city = Entry(root, width=30)
city.grid(row=2, column=1)

country = Entry(root, width=30)
country.grid(row=3, column=1)

fav_num = Entry(root, width=30)
fav_num.grid(row=4, column=1)

first_name_label = Label(root, text="First Name")
first_name_label.grid(row=0, column=0)
last_name_label = Label(root, text="Last Name")
last_name_label.grid(row=1, column=0)
city_label = Label(root, text="City")
city_label.grid(row=2, column=0)
country_label = Label(root, text="Country")
country_label.grid(row=3, column=0)
fav_num_label = Label(root, text="Fav Num")
fav_num_label.grid(row=4, column=0)

submitbtn = Button(root, text="add record to database", command=submit)
submitbtn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

conn.commit()

conn.close()










#query_btn = Button(root, text="Show Records", command=query)
#query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)


root.mainloop()