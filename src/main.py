# Team Project: Calculator Application
# Version: 1.3.0

import tkinter as tk
from tkinter import messagebox


# Calculator logic
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# GUI Logic
class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        self.expression = ""

        self.display = tk.Entry(
            root,
            font=("Arial", 20),
            borderwidth=2,
            relief="solid",
            justify="right"
        )
        self.display.pack(fill="x", padx=10, pady=10)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ("7", "8", "9", "/"),
            ("4", "5", "6", "*"),
            ("1", "2", "3", "-"),
            ("0", ".", "=", "+")
        ]

        for row in buttons:
            frame = tk.Frame(self.root)
            frame.pack(expand=True, fill="both")
            for char in row:
                btn = tk.Button(
                    frame,
                    text=char,
                    font=("Arial", 16),
                    command=lambda c=char: self.on_button_click(c)
                )
                btn.pack(side="left", expand=True, fill="both")

        clear_btn = tk.Button(
            self.root,
            text="Clear",
            font=("Arial", 16),
            bg="lightgray",
            command=self.clear
        )
        clear_btn.pack(fill="both", padx=10, pady=5)

    def on_button_click(self, char):
        if char == "=":
            self.calculate()
        else:
            self.expression += char
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)

    def calculate(self):
        try:
            result = eval(self.expression)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
            self.expression = str(result)
        except Exception:
            messagebox.showerror("Error", "Invalid calculation")
            self.clear()

    def clear(self):
        self.expression = ""
        self.display.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
