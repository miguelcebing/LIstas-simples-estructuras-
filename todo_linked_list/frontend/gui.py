import tkinter as tk
from tkinter import messagebox
from models.task_list import TaskList


class TodoGUI:
    def __init__(self, task_list: TaskList):
        self.task_list = task_list
        self.window = tk.Tk()
        self.window.title("TODO LIST - Linked List")
        self.window.geometry("450x500")
        self.window.configure(bg="#2c3e50")

        self.create_widgets()
        self.refresh_task_list()

    def create_widgets(self):
        title_label = tk.Label(
            self.window,
            text="TODO LIST",
            font=("Arial", 24, "bold"),
            bg="#2c3e50",
            fg="#ecf0f1"
        )
        title_label.pack(pady=15)

        input_frame = tk.Frame(self.window, bg="#2c3e50")
        input_frame.pack(pady=10, padx=20, fill=tk.X)

        self.task_entry = tk.Entry(
            input_frame,
            font=("Arial", 14),
            bg="#ecf0f1",
            fg="#2c3e50",
            insertbackground="#2c3e50"
        )
        self.task_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=8)
        self.task_entry.bind("<Return>", lambda event: self.add_task())

        add_button = tk.Button(
            input_frame,
            text="Add",
            font=("Arial", 12, "bold"),
            bg="#27ae60",
            fg="white",
            command=self.add_task,
            padx=15,
            pady=8
        )
        add_button.pack(side=tk.RIGHT, padx=(10, 0))

        list_frame = tk.Frame(self.window, bg="#2c3e50")
        list_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        self.task_listbox = tk.Listbox(
            list_frame,
            font=("Arial", 12),
            bg="#34495e",
            fg="#ecf0f1",
            selectbackground="#3498db",
            selectforeground="white",
            activestyle="none",
            borderwidth=0,
            highlightthickness=1,
            highlightbackground="#3498db"
        )
        self.task_listbox.pack(fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(self.task_listbox)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.task_listbox.yview)

        button_frame = tk.Frame(self.window, bg="#2c3e50")
        button_frame.pack(pady=15, padx=20, fill=tk.X)

        complete_button = tk.Button(
            button_frame,
            text="Complete",
            font=("Arial", 11, "bold"),
            bg="#f39c12",
            fg="white",
            command=self.complete_task,
            padx=10,
            pady=8
        )
        complete_button.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))

        delete_button = tk.Button(
            button_frame,
            text="Delete",
            font=("Arial", 11, "bold"),
            bg="#e74c3c",
            fg="white",
            command=self.delete_task,
            padx=10,
            pady=8
        )
        delete_button.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=(5, 0))

        self.counter_label = tk.Label(
            self.window,
            text="Total tasks: 0",
            font=("Arial", 11),
            bg="#2c3e50",
            fg="#bdc3c7"
        )
        self.counter_label.pack(pady=(0, 15))

    def refresh_task_list(self):
        self.task_listbox.delete(0, tk.END)
        index = 0
        for task in self.task_list:
            status = "[x]" if task.completed else "[ ]"
            self.task_listbox.insert(tk.END, f"  {status}  {task.description}")
            if task.completed:
                self.task_listbox.itemconfig(index, fg="#27ae60")
            index += 1
        self.counter_label.config(text=f"Total tasks: {len(self.task_list)}")

    def add_task(self):
        description = self.task_entry.get().strip()
        if description:
            self.task_list.add_task(description)
            self.task_entry.delete(0, tk.END)
            self.refresh_task_list()
        else:
            messagebox.showwarning("Warning", "Please enter a task description.")

    def complete_task(self):
        selection = self.task_listbox.curselection()
        if selection:
            position = selection[0]
            if self.task_list.complete_task(position):
                self.refresh_task_list()
        else:
            messagebox.showwarning("Warning", "Please select a task to complete.")

    def delete_task(self):
        selection = self.task_listbox.curselection()
        if selection:
            position = selection[0]
            if self.task_list.remove_task(position):
                self.refresh_task_list()
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def run(self):
        self.window.mainloop()
