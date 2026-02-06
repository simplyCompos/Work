import tkinter as tk

root = tk.Tk()
root.title("Questionnaire")

name_var = tk.StringVar()
gender_var = tk.StringVar()
agree_var = tk.BooleanVar()

tk.Label(root, text="Name").grid(row=0, column=0)
tk.Entry(root, textvariable=name_var).grid(row=0, column=1)

tk.Radiobutton(root, text="Male", variable=gender_var, value="M").grid(row=1, column=0)
tk.Radiobutton(root, text="Female", variable=gender_var, value="F").grid(row=1, column=1)

tk.Checkbutton(root, text="Ageeing with terms",
               variable=agree_var).grid(row=2, column=0, columnspan=2)

result = tk.Label(root)
result.grid(row=4, column=0, columnspan=2)

def save():
    if not agree_var.get():
        result.config(text="Terms agreeing required!")
        return
    result.config(text=f"{name_var.get()}, gender: {gender_var.get()}")

tk.Button(root, text="Save", command=save).grid(row=3, column=0, columnspan=2)

root.mainloop()
