import tkinter as tk
from tkinter import ttk, colorchooser

def choose_color():
    color = colorchooser.askcolor()[1]
    if color:
        root.configure(bg=color)
        with open("color.txt", "w") as f:
            f.write(color)

root = tk.Tk()
root.title("Notebook")

try:
    with open("color.txt") as f:
        root.configure(bg=f.read())
except:
    pass

nb = ttk.Notebook(root)
nb.pack(fill="both", expand=True)

tab1 = tk.Frame(nb)
tab2 = tk.Frame(nb)
tab3 = tk.Frame(nb)

nb.add(tab1, text="Main")
nb.add(tab2, text="Settings")
nb.add(tab3, text="About program")

tk.Button(tab2, text="Background color", command=choose_color).pack()
tk.Label(tab3, text="Author: Compos").pack()

root.mainloop()
