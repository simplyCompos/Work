import tkinter as tk
from tkinter import filedialog, messagebox

root = tk.Tk()
root.title("Notepad")
root.geometry("600x400")

text = tk.Text(root)
text.pack(expand=True, fill="both")

current_file = None
is_saved = True
def open_file():
    global current_file, is_saved
    file_path = filedialog.askopenfilename(
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if file_path:
        with open(file_path, "r", encoding="utf-8") as f:
            text.delete("1.0", tk.END)
            text.insert(tk.END, f.read())
        current_file = file_path
        is_saved = True
def save_file():
    global current_file, is_saved
    if current_file is None:
        current_file = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt")]
        )
    if current_file:
        with open(current_file, "w", encoding="utf-8") as f:
            f.write(text.get("1.0", tk.END))
        is_saved = True
def on_change(event):
    global is_saved
    is_saved = False

text.bind("<Key>", on_change)
def exit_app():
    if not is_saved:
        answer = messagebox.askyesno(
            "Warning",
            "You have not saved changes, do you want to exit without saving?"
        )
        if not answer:
            return
    root.destroy()
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="file", menu=file_menu)

file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
root.protocol("WM_DELETE_WINDOW", exit_app)
root.mainloop()
