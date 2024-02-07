import tkinter as tk

root = tk.Tk()

root.title("Sveiciens!")
root.geometry('400x300')
Message = tk.Label(root, text = "Ievadiet vārdu:")
Message.pack()

ievade = tk.Entry(root)
ievade.pack(pady=10)


#poga = tk.Button(root, text = "Sveiki!", command = lambda: Message.config(text= ievade.get()))
def iev_teksts():
    Message.config(text= 'Sveiki,'+ ievade.get()+ ' !')
poga = tk.Button(root, text="Sveiki!", command= iev_teksts)
poga.pack(pady=10)

root.mainloop()