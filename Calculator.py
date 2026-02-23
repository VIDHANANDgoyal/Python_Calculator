import tkinter as tk
from tkinter import messagebox


class Calculator:

    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("350x450")
        self.root.resizable(False, False)

        self.expression = ""

        self.create_ui()

    def create_ui(self):
        # Display
        self.display = tk.Entry(
            self.root,
            font=("Arial", 20),
            borderwidth=5,
            relief="ridge",
            justify="right"
        )
        self.display.pack(fill="both", padx=10, pady=10, ipady=10)

        # Buttons Frame
        button_frame = tk.Frame(self.root)
        button_frame.pack()

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "C", "+"],
            ["="]
        ]

        for row in buttons:
            row_frame = tk.Frame(button_frame)
            row_frame.pack(expand=True, fill="both")

            for btn in row:
                button = tk.Button(
                    row_frame,
                    text=btn,
                    font=("Arial", 16),
                    height=2,
                    width=5,
                    command=lambda b=btn: self.on_button_click(b)
                )
                button.pack(side="left", expand=True, fill="both", padx=3, pady=3)

    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
            self.display.delete(0, tk.END)

        elif char == "=":
            try:
                result = str(eval(self.expression))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
                self.expression = result
            except:
                messagebox.showerror("Error", "Invalid Expression")
                self.display.delete(0, tk.END)
                self.expression = ""

        else:
            self.expression += char
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)


if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()