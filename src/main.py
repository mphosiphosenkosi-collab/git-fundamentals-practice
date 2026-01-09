import tkinter as tk
from tkinter import font as tkfont
import ast
import operator
import os

class BitCubeCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("BitCube Pro Calculator")
        self.root.geometry("380x550")
        self.root.configure(bg="#1A1A2E")
        
        # Make window slightly transparent for modern look
        self.root.attributes('-alpha', 0.97)
        
        self.expression = ""
        
        # BITCUBE COLOR SCHEME
        self.colors = {
            "bg": "#1A1A2E",
            "display_bg": "#0F0F1E",
            "display_fg": "#00FF9D",  # Neon green text
            "num_btn": "#2A3B8F",     # Deep blue
            "num_fg": "#FFFFFF",
            "op_btn": "#00C2FF",      # Electric blue
            "op_fg": "#000000",
            "equals_btn": "#00FF9D",  # Lime green
            "equals_fg": "#000000",
            "clear_btn": "#FF375F",   # BitCube red accent
            "clear_fg": "#FFFFFF"
        }
        
        self.setup_ui()
    
    def setup_ui(self):
        # Custom fonts
        self.title_font = tkfont.Font(family="Segoe UI", size=12, weight="bold")
        self.display_font = tkfont.Font(family="Consolas", size=28, weight="bold")
        self.btn_font = tkfont.Font(family="Segoe UI", size=16, weight="bold")
        
        # Header with BitCube branding
        header = tk.Frame(self.root, bg=self.colors["bg"])
        header.pack(fill="x", padx=20, pady=(20, 10))
        
        tk.Label(
            header,
            text="⚡ BITCUBE PRO CALCULATOR",
            font=self.title_font,
            bg=self.colors["bg"],
            fg=self.colors["op_btn"],
            anchor="w"
        ).pack(side="left")
        
        tk.Label(
            header,
            text="v2.0.0",
            font=("Segoe UI", 10),
            bg=self.colors["bg"],
            fg=self.colors["display_fg"],
            anchor="e"
        ).pack(side="right")
        
        # Display with modern look
        display_frame = tk.Frame(self.root, bg=self.colors["display_bg"], relief="flat")
        display_frame.pack(fill="x", padx=20, pady=10)
        
        self.display = tk.Entry(
            display_frame,
            font=self.display_font,
            borderwidth=0,
            relief="flat",
            justify="right",
            bg=self.colors["display_bg"],
            fg=self.colors["display_fg"],
            insertbackground=self.colors["display_fg"],
            readonlybackground=self.colors["display_bg"]
        )
        self.display.pack(fill="x", padx=15, pady=15)
        self.display.config(state='readonly')
        
        # Buttons grid with BitCube styling
        self.create_buttons()
        
        # Footer
        footer = tk.Frame(self.root, bg=self.colors["bg"], height=30)
        footer.pack(fill="x", side="bottom", pady=(10, 0))
        tk.Label(
            footer,
            text="Built with Python • CI/CD Powered • Portfolio Ready",
            font=("Segoe UI", 9),
            bg=self.colors["bg"],
            fg="#666699"
        ).pack()
    
    def create_buttons(self):
        # Button layout
        buttons = [
            ["C", "⌫", "%", "÷"],
            ["7", "8", "9", "×"],
            ["4", "5", "6", "−"],
            ["1", "2", "3", "+"],
            ["00", "0", ".", "="]
        ]
        
        button_frame = tk.Frame(self.root, bg=self.colors["bg"])
        button_frame.pack(expand=True, fill="both", padx=20, pady=10)
        
        # Configure grid
        for i in range(5):
            button_frame.grid_rowconfigure(i, weight=1)
        for j in range(4):
            button_frame.grid_columnconfigure(j, weight=1)
        
        # Create buttons
        for row_idx, row in enumerate(buttons):
            for col_idx, text in enumerate(row):
                # Determine button style
                if text in ["C", "⌫"]:
                    bg, fg = self.colors["clear_btn"], self.colors["clear_fg"]
                elif text in ["÷", "×", "−", "+", "%"]:
                    bg, fg = self.colors["op_btn"], self.colors["op_fg"]
                elif text == "=":
                    bg, fg = self.colors["equals_btn"], self.colors["equals_fg"]
                else:
                    bg, fg = self.colors["num_btn"], self.colors["num_fg"]
                
                btn = tk.Button(
                    button_frame,
                    text=text,
                    font=self.btn_font,
                    bg=bg,
                    fg=fg,
                    activebackground=self.lighten_color(bg, 20),
                    activeforeground=fg,
                    borderwidth=0,
                    relief="flat",
                    cursor="hand2",
                    command=lambda t=text: self.on_button_click(t)
                )
                
                # Add hover effect
                btn.bind("<Enter>", lambda e, b=btn: b.config(bg=self.lighten_color(b['bg'], 10)))
                btn.bind("<Leave>", lambda e, b=btn, c=bg: b.config(bg=c))
                
                btn.grid(
                    row=row_idx,
                    column=col_idx,
                    sticky="nsew",
                    padx=3,
                    pady=3
                )
    
    def lighten_color(self, hex_color, percent):
        """Lighten a hex color by given percent"""
        # Convert hex to RGB, lighten, convert back
        # (Implementation for color manipulation)
        # Simplified version - in full code we'd implement proper color math
        return hex_color
    
    def on_button_click(self, char):
        # Your button logic here (updated for new symbols)
        pass
    
    # Rest of your methods (calculate, clear, etc.) with adjustments for new symbols

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
            result = safe_eval(self.expression)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
            self.expression = str(result)
        except Exception:
            messagebox.showerror("Error", "Invalid calculation")
            self.clear()

    def clear(self):
        self.expression = ""
        self.display.delete(0, tk.END)

# -----------------------------
# CLI Demo (for CI mode)
# -----------------------------
def run_cli_demo():
    print("Calculator v1.4.0")
    print(f"10 + 5 = {add(10, 5)}")
    print(f"10 - 5 = {subtract(10, 5)}")
    print(f"10 x 5 = {multiply(10, 5)}")
    print(f"10 / 5 = {divide(10, 5)}")

# -----------------------------
# Entry point
# -----------------------------
if __name__ == "__main__":
    if os.environ.get("CI") == "true":
        run_cli_demo()
    else:
        root = tk.Tk()
        app = CalculatorApp(root)
        root.mainloop()
