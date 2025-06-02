import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_choice.get()

        if operation == "Add (+)":
            result = num1 + num2
        elif operation == "Subtract (-)":
            result = num1 - num2
        elif operation == "Multiply (×)":
            result = num1 * num2
        elif operation == "Divide (÷)":
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2
        else:
            result = "Invalid Operation"

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Cannot divide by zero.")

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x300")
root.resizable(False, False)

root.configure(bg="#f0f0f0")
font_style = ("Arial", 12)

tk.Label(root, text="Enter first number:", bg="#f0f0f0", font=font_style).pack(pady=5)
entry1 = tk.Entry(root, font=font_style)
entry1.pack(pady=5)

tk.Label(root, text="Enter second number:", bg="#f0f0f0", font=font_style).pack(pady=5)
entry2 = tk.Entry(root, font=font_style)
entry2.pack(pady=5)

tk.Label(root, text="Choose operation:", bg="#f0f0f0", font=font_style).pack(pady=5)
operation_choice = ttk.Combobox(root, values=["Add (+)", "Subtract (-)", "Multiply (×)", "Divide (÷)"], state="readonly", font=font_style)
operation_choice.pack(pady=5)
operation_choice.current(0)

calc_btn = tk.Button(root, text="Calculate", command=calculate, font=font_style, bg="#4CAF50", fg="white")
calc_btn.pack(pady=15)

result_label = tk.Label(root, text="Result: ", bg="#f0f0f0", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

root.mainloop()
