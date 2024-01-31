import tkinter as tk

root = tk.Tk()
root.title('Tkinter Window Demo')
root.geometry('600x400+50+50')
root.resizable(False, True)

message = tk.Label(root, text = "Hello world!")
message.pack()

root.mainloop()