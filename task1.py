import tkinter as tk
from tkinter import messagebox, simpledialog
import os

# === Initialize the app ===
root = tk.Tk()
root.title("📝 To-Do List Manager")
root.geometry("500x500")
root.resizable(False, False)

# === Task storage ===
tasks = []

# === File to save tasks ===
task_file = "tasks.txt"

# === Load tasks from file ===
def load_tasks():
    if os.path.exists(task_file):
        with open(task_file, 'r') as file:
            for line in file:
                task = line.strip()
                if task:
                    tasks.append(task)
        update_listbox()

# === Save tasks to file ===
def save_tasks():
    with open(task_file, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

# === Update the listbox ===
def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

# === Add task ===
def add_task():
    task = entry.get().strip()
    if task:
        tasks.append(task)
        update_listbox()
        save_tasks()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# === Delete selected task ===
def delete_task():
    try:
        index = listbox.curselection()[0]
        tasks.pop(index)
        update_listbox()
        save_tasks()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# === Mark task as done ===
def mark_done():
    try:
        index = listbox.curselection()[0]
        task = tasks[index]
        if not task.startswith("✔️ "):
            tasks[index] = "✔️ " + task
            update_listbox()
            save_tasks()
        else:
            messagebox.showinfo("Info", "Task is already marked as done.")
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as done.")

# === Clear all tasks ===
def clear_all():
    if messagebox.askyesno("Confirm", "Are you sure you want to clear all tasks?"):
        tasks.clear()
        update_listbox()
        save_tasks()

# === UI Components ===

title_label = tk.Label(root, text="📝 To-Do List", font=("Helvetica", 20, "bold"))
title_label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14), width=30)
entry.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=5)

add_button = tk.Button(button_frame, text="Add Task", command=add_task, width=12, bg="lightgreen")
add_button.grid(row=0, column=0, padx=5)

delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task, width=12, bg="salmon")
delete_button.grid(row=0, column=1, padx=5)

done_button = tk.Button(button_frame, text="Mark as Done", command=mark_done, width=12, bg="lightblue")
done_button.grid(row=0, column=2, padx=5)

clear_button = tk.Button(root, text="Clear All Tasks", command=clear_all, width=20, bg="orange")
clear_button.pack(pady=5)

listbox = tk.Listbox(root, font=("Arial", 12), height=15, selectbackground="skyblue")
listbox.pack(pady=10, fill=tk.BOTH, expand=True)

# === Load existing tasks and run ===
load_tasks()
root.mainloop()
