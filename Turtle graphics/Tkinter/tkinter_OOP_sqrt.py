import tkinter as tk
import math
from tkinter import messagebox

root = tk.Tk()

root.title("Kvadrātsaknes izvilkšana")
root.geometry('400x300')

teksts = tk.Label(root, text="")
teksts.pack(pady=30)

ievade1 = tk.Entry(root)
ievade1.pack(pady=10)

Label1 = tk.Label(master=root, text= "Ievadiet skaitli", fg="green", bg= "light blue")
Label1.place(relx=0.05, rely=0.25, width=100, height=50)

def kvadratsakne():
    try:
       number = float(ievade1.get())       
       result = math.sqrt(number)
       teksts.config(text = f"Kvadrātsakne no ievadītā skaitļa ir {result}")  
    except ValueError:
        messagebox.showerror("Error", "Jūs neesat ievadījis skaitli!")

poga = tk.Button(root, text = 'Izvilkt kvadrātsakni', command = kvadratsakne)
poga.pack(pady=10)


root.mainloop()