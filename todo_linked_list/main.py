import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "models"))

from models.task_list import TaskList
from frontend.gui import TodoGUI


if __name__ == "__main__":
    task_list = TaskList()
    gui = TodoGUI(task_list)
    gui.run()
