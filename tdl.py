import tkinter as tk
from tkinter import messagebox, ttk

def save_tasks(tasks, filename="tasks.txt"):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def load_tasks(filename="tasks.txt"):
    tasks = []
    try:
        with open(filename, "r") as file:
            tasks = [line.strip() for line in file]
    except FileNotFoundError:
        print("Invalid file name. New one will be created.")
    return tasks

def update_task_list():
    task_list.delete(0, tk.END)
    for i, task in enumerate(tasks):
        task_list.insert(tk.END, f"{i + 1}. {task}")

def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        task_entry.delete(0, tk.END)
        update_task_list()
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    try:
        selected_index = task_list.curselection()[0]
        tasks.pop(selected_index)
        update_task_list()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")

def complete_task():
    try:
        selected_index = task_list.curselection()[0]
        if "(completed)" not in tasks[selected_index]:
            tasks[selected_index] += " (completed)"
        update_task_list()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as completed.")

def uncomplete_task():
    try:
        selected_index = task_list.curselection()[0]
        if "(completed)" in tasks[selected_index]:
            tasks[selected_index] = tasks[selected_index].replace(" (completed)", "")
        update_task_list()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as uncompleted.")

def exit_and_save():
    save_tasks(tasks)
    root.destroy()

root = tk.Tk()
root.title("Modern To-Do List Application")
root.geometry("400x500")
root.configure(bg="#2e2e2e")

tasks = load_tasks()

style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Helvetica", 10), padding=5, background="#4CAF50", foreground="white", borderwidth=0)
style.map("TButton", background=[("active", "#66BB6A")])
style.configure("TLabel", background="#2e2e2e", foreground="white")
style.configure("TFrame", background="#2e2e2e")
style.configure("TEntry", padding=10, background="#4e4e4e", foreground="black")

task_entry = ttk.Entry(root, width=40, font=("Helvetica", 12))
task_entry.pack(pady=(20, 10))

button_frame = ttk.Frame(root)
button_frame.pack(pady=10)

add_button = ttk.Button(button_frame, text="Add Task", command=add_task)
add_button.grid(row=0, column=0, padx=5)

remove_button = ttk.Button(button_frame, text="Remove Task", command=remove_task)
remove_button.grid(row=0, column=1, padx=5)

complete_button = ttk.Button(button_frame, text="Complete", command=complete_task)
complete_button.grid(row=0, column=2, padx=5)

uncomplete_button = ttk.Button(button_frame, text="Uncomplete", command=uncomplete_task)
uncomplete_button.grid(row=0, column=3, padx=5)

task_list_frame = ttk.Frame(root)
task_list_frame.pack(pady=10)
task_list = tk.Listbox(task_list_frame, width=50, height=15, selectmode=tk.SINGLE, bg="#4e4e4e", fg="white", font=("Helvetica", 10), bd=0, highlightthickness=0)
task_list.pack(side="left", fill="y")
scrollbar = ttk.Scrollbar(task_list_frame, orient="vertical", command=task_list.yview)
scrollbar.pack(side="right", fill="y")
task_list.config(yscrollcommand=scrollbar.set)

exit_button = ttk.Button(root, text="Exit and Save", command=exit_and_save)
exit_button.pack(pady=15)

update_task_list()

root.mainloop()
