import tkinter as tk
from tkinter import ttk
from tkinter import *


root = tk.Tk()
root.title('Mana pirmā programma!!!')
root.geometry('600x400+100+100')
root.resizable(False, False)
# root.attributes('-alpha', 0.5)
root.iconbitmap('Turtle graphics/Tkinter/electron_94377.ico')
# place a label on the root window
message = tk.Label(root, text="Sveika pasaule!")
message.pack()
ttk.Label(root, text='Themed Label').pack()

def button_clicked():
    print('Button clicked')


button = ttk.Button(root, text='Click Me', command=button_clicked)

button.pack()

def select(option):
    print(option)


ttk.Button(root, text='Rock', command=lambda: print('Rock')).place(x = 100, y = 200)
ttk.Button(root, text='Paper',command=lambda: print('Paper')).place(x = 200, y = 200)
ttk.Button(root, text='Scissors', command=lambda: print('Scissors')).place(x = 300, y = 200)
# keep the window displaying

photo = tk.PhotoImage(file='Turtle graphics/Tkinter/valentines-day.png')
image_label = ttk.Label(root,image=photo,padding=5)
image_label.pack()

message = tk.Label(root, text="Ievade")
message.place(x = 200, y = 250)

def button_clicked():
    print('Button clicked')


button = ttk.Button(root, text='Do a click', command=button_clicked)
button.place(x=200, y=300)

root.mainloop()