import tkinter as tk
from tkinter import messagebox

TODO_FILE = "todo.txt"

def add_task():
    task = entry_task.get()
    if task:
        with open(TODO_FILE, "a") as f:
            f.write(task + "\n")
        list_tasks()
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def remove_task():
    try:
        index = int(listbox_tasks.curselection()[0])
        listbox_tasks.delete(index)
        with open(TODO_FILE, "r") as f:
            tasks = f.readlines()
        with open(TODO_FILE, "w") as f:
            for i, task in enumerate(tasks):
                if i != index:
                    f.write(task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")

def list_tasks():
    listbox_tasks.delete(0, tk.END)
    if not tk.messagebox.askyesno("Info", "Reload tasks?"):
        return
    try:
        with open(TODO_FILE, "r") as f:
            tasks = f.readlines()
        for task in tasks:
            listbox_tasks.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass

# Create the main application window
app = tk.Tk()
app.title("Todo List")

# Create the entry field to add tasks
entry_task = tk.Entry(app, width=40)
entry_task.grid(row=0, column=0, padx=10, pady=10)

# Create the "Add Task" button
btn_add_task = tk.Button(app, text="Add Task", width=20, command=add_task)
btn_add_task.grid(row=0, column=1, padx=5, pady=10)

# Create the listbox to display tasks
listbox_tasks = tk.Listbox(app, width=50, height=10)
listbox_tasks.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

# Create the "Remove Task" button
btn_remove_task = tk.Button(app, text="Remove Task", width=20, command=remove_task)
btn_remove_task.grid(row=2, column=0, padx=10, pady=10)

# Create the "List Tasks" button
btn_list_tasks = tk.Button(app, text="List Tasks", width=20, command=list_tasks)
btn_list_tasks.grid(row=2, column=1, padx=5, pady=10)

# Start the main event loop
app.mainloop()
