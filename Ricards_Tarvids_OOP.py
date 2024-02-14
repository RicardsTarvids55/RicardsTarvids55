import math
import tkinter as tk
from tkinter import messagebox
#Definēju tk par root 
root = tk.Tk()

#Formula ir I = U/R
root.title("Fizikas strāvas stipruma formula (oma likums)")
#ierakstu loga izmērus
root.geometry('500x400')
#padaru iespējamu logu izmērus mainīt
root.resizable(True, True)
#definēju funkciju, ko izmantošu aprēķiniem un rezultātu izvadei
def formula():
    try:
            result = float(ievade1.get()) / float(ievade2.get())
            Message3.config(text = "Rezultāts ir: " + str(result) + " Ampēri")
            photo_label.pack()
    except ValueError:
        messagebox.showerror("Error","Nav ievadīts skaitlis!")
#Izveidoju logus, kuros rakstīt datus
Message = tk.Label(root, text = "Ievadiet strāvas spriegumu:", bg= 'light blue')
Message.pack()

ievade1 = tk.Entry(root)
ievade1.pack(pady=10)

Message2 = tk.Label(root, text = "Ievadiet strāvas pretestību:", bg= 'light green')
Message2.pack()

ievade2 = tk.Entry(root)
ievade2.pack(pady=10)
#Izveidoju pogu, kas, uzspiesta, izvadīs rezultātu
poga = tk.Button(root, text = 'Izrēķināt strāvas stiprumu', command = formula, fg = 'Black', bg = 'Sky blue', activebackground = 'gold' )
poga.pack(pady=10)
#definēju funkciju, kas notīrīs parādītos rezultātus
def delete_button():
    Message3.configure(text = "")
    photo_label.pack_forget()
#Izveidoju pogu, kas notīrīs rezultātu
poga2 = tk.Button(root, text = "Notīrīt rezultātu", command=delete_button, fg = 'White', bg = 'Dark red', activebackground = 'Black' )
poga2.pack()
#izveidoju atsevišķu label, kur tiks parādīt rezultāts
Message3 = tk.Label(root, text= "")
Message3.pack(pady=30)

#Uzrakstu kodu, kas palīdzēs parādīt foto, kopā ar rezultātu
photo = tk.PhotoImage(file='small yellow victory cup (1).png')
photo_label = tk.Label(root, image=photo)
#Beidzu darbību
root.mainloop()