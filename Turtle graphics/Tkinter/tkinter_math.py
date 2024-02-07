import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title("Brīnumzemes ievade")
root.geometry('400x300')

teksts = tk.Label(root, text="")
teksts.pack(pady=30)

teksts2 = ttk.Label(root, text="")
teksts.pack(pady = 30)

photo = tk.PhotoImage(file='Turtle graphics/Tkinter/valentines-day.png')
teksts2.pack(pady=30)

ievade1 = tk.Entry(root)
ievade1.pack(pady=10)

ievade2 = tk.Entry(root)
ievade2.pack(pady=10)

def saskaitits():
    teksts.config(text = int(ievade1.get()) + int(ievade2.get()))
    teksts2.config(image=photo) 

poga = tk.Button(root, text = 'Saskaitīt', command = saskaitits)
poga.pack(pady=10)

root.mainloop()