import tkinter as tk
print("enter screen width")
WIDTH = int(input())
print("now height")
HEIGHT = int(input())

root = tk.Tk()
root.title("First program")
root.geometry(f"{WIDTH}x{HEIGHT}")
root.resizable(False, False)

label = tk.Label(root, text="Hello, world!", font=("Arial", 24))
label.pack(pady=50)

button = tk.Button(root, text="Close", command=root.destroy)
button.pack()

root.mainloop()
