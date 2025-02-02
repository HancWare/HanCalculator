import tkinter as tk
from tkinter import ttk
import math

class HancCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Hanc Calculator")
        self.root.geometry("400x600")
        self.root.configure(bg="#1e1e1e")
        
        self.equation = ""
        
        self.display = tk.Entry(root, font=("Arial", 20), bg="#292929", fg="white", bd=0, justify="right")
        self.display.pack(fill="both", padx=10, pady=10, ipady=10)
        
        self.create_buttons()
    
    def create_buttons(self):
        button_frame = tk.Frame(self.root, bg="#1e1e1e")
        button_frame.pack(expand=True, fill="both")

        buttons = [
            ("C", "CE", "⌫", "/"),
            ("7", "8", "9", "*"),
            ("4", "5", "6", "-"),
            ("1", "2", "3", "+"),
            ("0", ".", "π", "="),
            ("sin", "cos", "tan", "√"),
            ("x²", "log", "exp", "mod")
        ]

        for row in buttons:
            row_frame = tk.Frame(button_frame, bg="#1e1e1e")
            row_frame.pack(expand=True, fill="both")
            for btn in row:
                button = ttk.Button(
                    row_frame, text=btn, command=lambda b=btn: self.on_button_click(b),
                    style="TButton"
                )
                button.pack(side="left", expand=True, fill="both", padx=2, pady=2)

        self.root.bind("<Return>", lambda event: self.on_button_click("="))
        self.root.bind("<BackSpace>", lambda event: self.on_button_click("⌫"))

    def on_button_click(self, char):
        if char == "=":
            try:
                self.equation = self.equation.replace("π", str(math.pi))
                self.equation = self.equation.replace("√", "math.sqrt")
                self.equation = self.equation.replace("sin", "math.sin")
                self.equation = self.equation.replace("cos", "math.cos")
                self.equation = self.equation.replace("tan", "math.tan")
                self.equation = self.equation.replace("x²", "**2")
                self.equation = self.equation.replace("log", "math.log10")
                self.equation = self.equation.replace("exp", "math.exp")
                self.equation = self.equation.replace("mod", "%")

                result = eval(self.equation)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
                self.equation = str(result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
                self.equation = ""
        elif char == "C":
            self.equation = ""
            self.display.delete(0, tk.END)
        elif char == "CE":
            self.equation = self.equation[:-1]
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.equation)
        elif char == "⌫":
            self.equation = self.equation[:-1]
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.equation)
        else:
            self.equation += char
            self.display.insert(tk.END, char)

if __name__ == "__main__":
    root = tk.Tk()
    style = ttk.Style()
    style.configure("TButton", font=("Arial", 14), padding=10, background="#333", foreground="white")
    HancCalculator(root)
    root.mainloop()
