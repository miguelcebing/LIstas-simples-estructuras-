class Task {
    constructor(description, completed = false) {
        this.description = description;
        this.completed = completed;
    }
}

class TaskNode {
    constructor(task) {
        this.task = task;
        this.next = null;
    }
}

class TaskList {
    constructor() {
        this.head = null;
        this._size = 0;
    }

    addTask(description) {
        const newTask = new Task(description);
        const newNode = new TaskNode(newTask);
        
        if (this.head === null) {
            this.head = newNode;
        } else {
            let current = this.head;
            while (current.next !== null) {
                current = current.next;
            }
            current.next = newNode;
        }
        this._size++;
    }

    removeTask(position) {
        if (this.head === null || position < 0) {
            return false;
        }
        
        if (position === 0) {
            this.head = this.head.next;
            this._size--;
            return true;
        }
        
        let previous = this.head;
        let current = this.head.next;
        let index = 1;
        
        while (current !== null) {
            if (index === position) {
                previous.next = current.next;
                this._size--;
                return true;
            }
            previous = current;
            current = current.next;
            index++;
        }
        return false;
    }

    completeTask(position) {
        let current = this.head;
        let index = 0;
        
        while (current !== null) {
            if (index === position) {
                current.task.completed = !current.task.completed;
                return true;
            }
            current = current.next;
            index++;
        }
        return false;
    }

    toArray() {
        const tasks = [];
        let current = this.head;
        while (current !== null) {
            tasks.push(current.task);
            current = current.next;
        }
        return tasks;
    }

    get size() {
        return this._size;
    }
}

class TodoApp {
    constructor() {
        this.taskList = new TaskList();
        this.currentFilter = 'all';
        
        this.taskInput = document.getElementById('taskInput');
        this.addBtn = document.getElementById('addBtn');
        this.taskListElement = document.getElementById('taskList');
        this.emptyState = document.getElementById('emptyState');
        this.totalTasksEl = document.getElementById('totalTasks');
        this.completedTasksEl = document.getElementById('completedTasks');
        this.pendingTasksEl = document.getElementById('pendingTasks');
        this.filterBtns = document.querySelectorAll('.filter-btn');
        
        this.init();
    }
    
    init() {
        this.addBtn.addEventListener('click', () => this.addTask());
        this.taskInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') this.addTask();
        });
        
        this.filterBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                this.filterBtns.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                this.currentFilter = btn.dataset.filter;
                this.render();
            });
        });
        
        this.loadFromStorage();
        this.render();
    }
    
    addTask() {
        const description = this.taskInput.value.trim();
        if (description) {
            this.taskList.addTask(description);
            this.taskInput.value = '';
            this.saveToStorage();
            this.render();
            this.taskInput.focus();
        }
    }
    
    toggleTask(position) {
        this.taskList.completeTask(position);
        this.saveToStorage();
        this.render();
    }
    
    deleteTask(position) {
        this.taskList.removeTask(position);
        this.saveToStorage();
        this.render();
    }
    
    updateStats() {
        const tasks = this.taskList.toArray();
        const total = tasks.length;
        const completed = tasks.filter(t => t.completed).length;
        const pending = total - completed;
        
        this.totalTasksEl.textContent = total;
        this.completedTasksEl.textContent = completed;
        this.pendingTasksEl.textContent = pending;
    }
    
    render() {
        const tasks = this.taskList.toArray();
        let filteredTasks = tasks;
        
        if (this.currentFilter === 'pending') {
            filteredTasks = tasks.filter(t => !t.completed);
        } else if (this.currentFilter === 'completed') {
            filteredTasks = tasks.filter(t => t.completed);
        }
        
        this.taskListElement.innerHTML = '';
        
        if (filteredTasks.length === 0) {
            this.emptyState.classList.add('show');
        } else {
            this.emptyState.classList.remove('show');
            
            let index = 0;
            tasks.forEach((task) => {
                if (this.currentFilter === 'all' || 
                    (this.currentFilter === 'pending' && !task.completed) ||
                    (this.currentFilter === 'completed' && task.completed)) {
                    
                    const li = document.createElement('li');
                    li.className = `task-item ${task.completed ? 'completed' : ''}`;
                    li.innerHTML = `
                        <div class="task-checkbox ${task.completed ? 'checked' : ''}" data-action="toggle" data-index="${index}"></div>
                        <span class="task-text">${this.escapeHtml(task.description)}</span>
                        <button class="task-delete" data-action="delete" data-index="${index}">
                            <svg width="18" height="18" viewBox="0 0 18 18" fill="none">
                                <path d="M4 4L14 14M14 4L4 14" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
                            </svg>
                        </button>
                    `;
                    this.taskListElement.appendChild(li);
                }
                index++;
            });
        }
        
        this.taskListElement.querySelectorAll('[data-action]').forEach(el => {
            el.addEventListener('click', (e) => {
                const action = e.currentTarget.dataset.action;
                const index = parseInt(e.currentTarget.dataset.index);
                
                if (action === 'toggle') {
                    this.toggleTask(index);
                } else if (action === 'delete') {
                    this.deleteTask(index);
                }
            });
        });
        
        this.updateStats();
    }
    
    escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }
    
    saveToStorage() {
        const tasks = this.taskList.toArray();
        localStorage.setItem('todoTasks', JSON.stringify(tasks));
    }
    
    loadFromStorage() {
        const saved = localStorage.getItem('todoTasks');
        if (saved) {
            const tasks = JSON.parse(saved);
            tasks.forEach(task => {
                const newTask = new Task(task.description, task.completed);
                const newNode = new TaskNode(newTask);
                
                if (this.taskList.head === null) {
                    this.taskList.head = newNode;
                } else {
                    let current = this.taskList.head;
                    while (current.next !== null) {
                        current = current.next;
                    }
                    current.next = newNode;
                }
                this.taskList._size++;
            });
        }
    }
}

document.addEventListener('DOMContentLoaded', () => {
    new TodoApp();
});
