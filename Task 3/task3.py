import tkinter as tk
from tkinter import ttk, messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showerror("Error", "Password length must be at least 4.")
            return
        complexity = complexity_choice.get()
        char_sets = {
            'Low': string.ascii_lowercase,
            'Medium': string.ascii_letters + string.digits,
            'High': string.ascii_letters + string.digits + string.punctuation
        }
        characters = char_sets.get(complexity, char_sets['High'])
        password = ''.join(random.choice(characters) for _ in range(length))
        password_output.config(state='normal')
        password_output.delete(0, tk.END)
        password_output.insert(0, password)
        password_output.config(state='readonly')
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for password length.")

root = tk.Tk()
root.title("🔐 Password Generator")
root.geometry("400x250")
root.resizable(False, False)

ttk.Label(root, text="Advanced Password Generator", font=("Arial", 16)).pack(pady=10)

frame = ttk.Frame(root)
frame.pack(pady=5)
ttk.Label(frame, text="Password Length:").grid(row=0, column=0, padx=5, pady=5)
length_entry = ttk.Entry(frame, width=10)
length_entry.grid(row=0, column=1)
length_entry.insert(0, "12")

ttk.Label(frame, text="Complexity:").grid(row=1, column=0, padx=5, pady=5)
complexity_choice = ttk.Combobox(frame, values=["Low", "Medium", "High"], state="readonly", width=8)
complexity_choice.set("High")
complexity_choice.grid(row=1, column=1)

ttk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

ttk.Label(root, text="Generated Password:").pack()
password_output = ttk.Entry(root, width=40, font=("Courier", 12), justify="center")
password_output.pack(pady=5)
password_output.config(state='readonly')

root.mainloop()
