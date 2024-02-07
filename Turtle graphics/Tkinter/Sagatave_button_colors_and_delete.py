import tkinter as tk
#definē galveno logu
root = tk.Tk()

#Loga virsraksts
root.title("Pogu programma")
#loga izmēri (widthXlenght)
root.geometry('400x300')
Message = tk.Label(root, text = "VAI TU PROGRAMMĒ?")
Message.pack()

def clciked():
    Message.configure(text = "KO TU DARI!?")

btn = tk.Button(root, text = "NESPIEST", command=clciked, fg='RED', activebackground = 'Light Blue')
btn.pack()

def delete_button():
    Message.configure(text = "")

btn = tk.Button(root, text = "DZĒST", command=delete_button, fg = 'White', bg = 'Dark red', activebackground = 'Black' )
btn.pack()
#Palaiž programmu
root.mainloop()