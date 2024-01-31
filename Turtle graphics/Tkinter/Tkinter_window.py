import tkinter as tk

root = tk.Tk()
root.title('Tkinter Window Demo')
#The following example changes the size of the window to 600x400 and the position of the window to 50 pixels from the top and left of the screen:
root.geometry('600x400+50+50')
message = tk.Label(root, text = "Hello world!")
message.pack()
root.mainloop()