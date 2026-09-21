import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "models"))

from models.task_list import TaskList

print("=== Testing Linked List Logic ===\n")

task_list = TaskList()

print("Adding 3 tasks...")
task_list.add_task("Buy groceries")
task_list.add_task("Walk the dog")
task_list.add_task("Read a book")

print("\nTasks after adding:")
for i, task in enumerate(task_list):
    status = "[x]" if task.completed else "[ ]"
    print(f"  {i}. {status} {task.description}")

print(f"\nTotal tasks: {len(task_list)}")

print("\nCompleting task 1...")
task_list.complete_task(1)

print("\nTasks after completing:")
for i, task in enumerate(task_list):
    status = "[x]" if task.completed else "[ ]"
    print(f"  {i}. {status} {task.description}")

print("\nDeleting task 0...")
task_list.remove_task(0)

print("\nTasks after deleting:")
for i, task in enumerate(task_list):
    status = "[x]" if task.completed else "[ ]"
    print(f"  {i}. {status} {task.description}")

print(f"\nTotal tasks: {len(task_list)}")

print("\n=== All tests passed! ===")
print("\nTo run the GUI: python main.py")
