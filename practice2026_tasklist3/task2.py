import tkinter as tk

root = tk.Tk()
root.title("Buttons")

text = tk.StringVar()

label = tk.Label(root, textvariable=text, font=("Arial", 14))
label.pack(pady=20)

tk.Button(root, text="Greet",
          command=lambda: text.set("Greetings user")
          ).pack()

tk.Button(root, text="Clear",
          command=lambda: text.set("")
          ).pack()

tk.Button(root, text="Exit", command=root.destroy).pack()

root.mainloop()
