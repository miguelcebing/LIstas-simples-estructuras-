---
name: todo-linked-list
description: >
  Genera o modifica un script en Python que implementa una lista de tareas
  pendientes (to-do list) usando una lista enlazada simple (singly linked
  list) hecha a mano, con POO, navegación exclusivamente por punteros (sin
  listas/tuplas/diccionarios nativos ni índices) y un frontend tipo menú de
  consola. Úsala cuando pidan un "gestor de tareas con lista enlazada",
  "to-do con nodos y punteros", o una tarea de estructuras de datos sobre
  listas enlazadas simples en Python.
---

# Todo List con Lista Enlazada Simple (POO)

## Cuándo usarla
Cada vez que el usuario pida un to-do list, gestor de tareas o similar
implementado explícitamente con **nodos y punteros** (lista enlazada simple)
en Python, orientado a objetos. Ver `AGENT.md` para las reglas completas del
proyecto (qué está prohibido, checklist de validación, etc.).

## Plantilla de clases (base para generar el script)

```python
class Task:
    """Holds the task data."""
    def __init__(self, description: str, completed: bool = False):
        self.description = description
        self.completed = completed


class TaskNode:
    """A single node: a Task plus a pointer to the next node."""
    def __init__(self, task: Task):
        self.task = task
        self.next = None  # pointer to the next node


class TaskList:
    """Singly linked list of TaskNode. All logic uses pointers only."""
    def __init__(self):
        self.head = None
        self._size = 0

    def add_task(self, description: str) -> None:
        new_node = TaskNode(Task(description))
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self._size += 1

    def remove_task(self, position: int) -> bool:
        if self.head is None or position < 0:
            return False
        if position == 0:
            self.head = self.head.next
            self._size -= 1
            return True
        previous, current, index = self.head, self.head.next, 1
        while current is not None:
            if index == position:
                previous.next = current.next
                self._size -= 1
                return True
            previous, current, index = current, current.next, index + 1
        return False

    def complete_task(self, position: int) -> bool:
        current, index = self.head, 0
        while current is not None:
            if index == position:
                current.task.completed = True
                return True
            current, index = current.next, index + 1
        return False

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.task
            current = current.next

    def __len__(self) -> int:
        return self._size


class TodoCLI:
    """Frontend: console menu. Contains no linked-list logic itself."""
    def __init__(self, task_list: TaskList):
        self.task_list = task_list

    def show_menu(self) -> None:
        print("\n1) Add task  2) List tasks  3) Complete task  4) Delete task  5) Exit")

    def list_tasks(self) -> None:
        for i, task in enumerate(self.task_list):
            status = "x" if task.completed else " "
            print(f"[{status}] {i}. {task.description}")

    def run(self) -> None:
        while True:
            self.show_menu()
            choice = input("Choose an option: ")
            if choice == "1":
                self.task_list.add_task(input("Task description: "))
            elif choice == "2":
                self.list_tasks()
            elif choice == "3":
                self.task_list.complete_task(int(input("Task position: ")))
            elif choice == "4":
                self.task_list.remove_task(int(input("Task position: ")))
            elif choice == "5":
                break


if __name__ == "__main__":
    TodoCLI(TaskList()).run()
```

## Checklist antes de entregar
Ver sección 4 ("Checklist de validación") de `AGENT.md`.
