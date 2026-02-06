import tkinter as tk
from tkinter import colorchooser, filedialog

root = tk.Tk()
root.title("Ghraphic")

current_color = "black"
mode = tk.StringVar(value="line")

canvas = tk.Canvas(root, width=600, height=400, bg="white")
canvas.pack()
def choose_color():
    global current_color
    color = colorchooser.askcolor()[1]
    if color:
        current_color = color
def clear_canvas():
    canvas.delete("all")
def save_canvas():
    file = filedialog.asksaveasfilename(
        defaultextension=".ps",
        filetypes=[("PostScript", "*.ps")]
    )
    if file:
        canvas.postscript(file=file)
start_x = start_y = 0

def start_draw(event):
    global start_x, start_y
    start_x, start_y = event.x, event.y

def draw(event):
    if mode.get() == "line":
        canvas.create_line(start_x, start_y, event.x, event.y,
                           fill=current_color)
    elif mode.get() == "circle":
        r = abs(event.x - start_x)
        canvas.create_oval(start_x - r, start_y - r,
                           start_x + r, start_y + r,
                           outline=current_color)
canvas.bind("<Button-1>", start_draw)
canvas.bind("<B1-Motion>", draw)
controls = tk.Frame(root)
controls.pack(pady=5)

tk.Radiobutton(controls, text="Line",
               variable=mode, value="line").pack(side="left")

tk.Radiobutton(controls, text="Circle",
               variable=mode, value="circle").pack(side="left")

tk.Button(controls, text="Color",
          command=choose_color).pack(side="left")

tk.Button(controls, text="Clear",
          command=clear_canvas).pack(side="left")

tk.Button(controls, text="Save",
          command=save_canvas).pack(side="left")
root.mainloop()
