import numpy as np
import datetime as dt
from tkinter import *
import joblib

current_year = dt.datetime.today().year


def show_entry_fields():
    p1 = float(e1.get())
    # p4=float(e4.get())

    text = clicked.get()
    if text == "OUT010":
        p2 = 0
        print(p2)
    elif text == "OUT013":
        p2 = 1
        print(p2)
    elif text == "OUT017":
        p2 = 2
        print(p2)
    elif text == "OUT018":
        p2 = 3
        print(p2)
    elif text == "OUT019":
        p2 = 4
        print(p2)
    elif text == "OUT027":
        p2 = 5
        print(p2)
    elif text == "OUT035":
        p2 = 6
        print(p2)
    elif text == "OUT045":
        p2 = 7
        print(p2)
    elif text == "OUT046":
        p2 = 8
        print(p2)
    elif text == "OUT049":
        p2 = 9
        print(p2)
    text0 = clicked0.get()
    if text0 == "High":
        p3 = 0
        print(p3)
    elif text0 == "Medium":
        p3 = 1
        print(p3)
    elif text0 == "Small":
        p3 = 2
        print(p3)

    text1 = clicked1.get()
    if text1 == "Supermarket Type1":
        p4 = 1
        print(p4)
    elif text1 == "Supermarket Type2":
        p4 = 2
        print(p4)
    elif text1 == "Supermarket Type3":
        p4 = 3
        print(p4)
    elif text1 == "Grocery Store":
        p4 = 0
        print(p4)

    p5 = current_year - int(e5.get())
    print(p5)

    model = joblib.load('bigmart_model')
    result = model.predict(np.array([[p1, p2, p3, p4, p5]]))
    Label(master, text="Sales").grid(row=8)
    Label(master, text=result).grid(row=10)
    print("Sales amount", result)


master = Tk()
master.title("Big Mart Sales Prediction using Machine Learning")

label = Label(master, text=" Big Mart Sales Prediction using ML"
              , bg="black", fg="white"). \
    grid(row=0, columnspan=2)

# Item_MRP	Outlet_Identifier	Outlet_Size	Outlet_Type	Outlet_age
Label(master, text="Item_MRP").grid(row=1)
Label(master, text="Outlet_Identifier").grid(row=2)
Label(master, text="Outlet_Size").grid(row=3)
Label(master, text="Outlet_Type").grid(row=4)
Label(master, text="Outlet_Establishment_Year").grid(row=5)

clicked = StringVar()
options = ['OUT010', 'OUT013', 'OUT017', 'OUT018', 'OUT019', 'OUT027',
           'OUT035', 'OUT045', 'OUT046', 'OUT049']

clicked0 = StringVar()

options0 = ['High', 'Medium', 'Small']

clicked1 = StringVar()
options1 = ['Grocery Store', 'Supermarket Type1', 'Supermarket Type2',
            'Supermarket Type3']

e1 = Entry(master)

e2 = OptionMenu(master, clicked, *options)
e2.configure(width=15)

e3 = OptionMenu(master, clicked0, *options0)
e3.configure(width=15)

e4 = OptionMenu(master, clicked1, *options1)
e4.configure(width=15)

e5 = Entry(master)

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)
e4.grid(row=4, column=1)
e5.grid(row=5, column=1)

Button(master, text='Predict', command=show_entry_fields).grid()

mainloop()
