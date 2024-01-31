#The following program illustrates how to pass an argument to the callback function associated with the button command:
import tkinter as tk
from tkinter import ttk

root = tk.Tk()


def select(option):
    print(option)

#labāk ir ja definē pogas, piemēram poga1, poga2
ttk.Button(root, text='Rock', command=lambda: select('Rock')).pack()
ttk.Button(root, text='Paper',command=lambda: select('Paper')).pack()
ttk.Button(root, text='Scissors', command=lambda: select('Scissors')).pack()

root.mainloop()