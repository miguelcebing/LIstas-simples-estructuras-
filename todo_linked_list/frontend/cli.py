from models.task_list import TaskList


class TodoCLI:
    def __init__(self, task_list: TaskList):
        self.task_list = task_list

    def show_menu(self) -> None:
        print("\n========== TODO LIST ==========")
        print("1) Add task")
        print("2) List tasks")
        print("3) Complete task")
        print("4) Delete task")
        print("5) Exit")
        print("================================")

    def list_tasks(self) -> None:
        if len(self.task_list) == 0:
            print("\nNo tasks found.")
            return
        print("\n--- Your Tasks ---")
        index = 0
        for task in self.task_list:
            status = "[x]" if task.completed else "[ ]"
            print(f"{index}. {status} {task.description}")
            index += 1

    def run(self) -> None:
        while True:
            self.show_menu()
            choice = input("Choose an option: ")
            if choice == "1":
                description = input("Task description: ")
                self.task_list.add_task(description)
                print("Task added!")
            elif choice == "2":
                self.list_tasks()
            elif choice == "3":
                self.list_tasks()
                position = int(input("Task number to complete: "))
                if self.task_list.complete_task(position):
                    print("Task completed!")
                else:
                    print("Invalid task number.")
            elif choice == "4":
                self.list_tasks()
                position = int(input("Task number to delete: "))
                if self.task_list.remove_task(position):
                    print("Task deleted!")
                else:
                    print("Invalid task number.")
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid option. Try again.")
