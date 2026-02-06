import tkinter as tk

root = tk.Tk()
root.title("Calculator")

a = tk.Entry(root)
b = tk.Entry(root)
a.pack()
b.pack()

result = tk.Label(root)
result.pack()

def calc(op):
    try:
        x = float(a.get())
        y = float(b.get())
        if op == "/" and y == 0:
            raise ZeroDivisionError
        res = eval(f"x {op} y")
        result.config(text=res)
    except:
        result.config(text="Error")

for op in ["+", "-", "*", "/"]:
    tk.Button(root, text=op, command=lambda o=op: calc(o)).pack()

root.mainloop()
