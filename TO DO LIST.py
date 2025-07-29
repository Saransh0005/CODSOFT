import tkinter as tk
from tkinter import messagebox

tasks = []

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

def add_task():
    task = entry.get()
    if task != "":
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Enter a task!")

def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        tasks.pop(selected_task_index)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to delete.")

def mark_done():
    try:
        index = listbox.curselection()[0]
        tasks[index] = "✔️ " + tasks[index]
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to mark as done.")

# GUI setup
root = tk.Tk()
root.title("To-Do List App")

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

frame = tk.Frame(root)
frame.pack()

add_btn = tk.Button(frame, text="Add Task", width=12, command=add_task)
add_btn.grid(row=0, column=0)

done_btn = tk.Button(frame, text="Mark Done", width=12, command=mark_done)
done_btn.grid(row=0, column=1)

delete_btn = tk.Button(frame, text="Delete Task", width=12, command=delete_task)
delete_btn.grid(row=0, column=2)

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=20)

root.mainloop()
