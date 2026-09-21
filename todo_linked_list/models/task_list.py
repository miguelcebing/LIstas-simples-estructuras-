from models.task import Task
from models.task_node import TaskNode


class TaskList:
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
        previous = self.head
        current = self.head.next
        index = 1
        while current is not None:
            if index == position:
                previous.next = current.next
                self._size -= 1
                return True
            previous = current
            current = current.next
            index += 1
        return False

    def complete_task(self, position: int) -> bool:
        current = self.head
        index = 0
        while current is not None:
            if index == position:
                current.task.completed = True
                return True
            current = current.next
            index += 1
        return False

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.task
            current = current.next

    def __len__(self) -> int:
        return self._size
