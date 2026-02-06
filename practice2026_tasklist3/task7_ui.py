import tkinter as tk
from logic import calculate_average


class AppUI:
    def init(self, root):
        self.root = root
        self.root.title("Modular program")

        self.entry = tk.Entry(root)
        self.entry.pack(pady=10)

        self.result = tk.Label(root, text="")
        self.result.pack(pady=10)

        btn = tk.Button(root, text="Calculate average", command=self.on_click)
        btn.pack()

    def on_click(self):
        try:
            numbers = list(map(float, self.entry.get().split()))
            avg = calculate_average(numbers)
            self.result.config(text=f"Average: {avg:.2f}")
        except ValueError:
            self.result.config(text="Entering Error")
