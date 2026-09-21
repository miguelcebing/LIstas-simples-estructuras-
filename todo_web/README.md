# TODO LIST - Linked List Implementation

A beautiful, modern TODO list application built with vanilla HTML, CSS, and JavaScript, using a **Singly Linked List** data structure.

## Features

- **Pure Linked List Implementation**: All operations (add, remove, complete) use pointer-based navigation
- **Modern UI**: Dark theme with smooth animations and responsive design
- **Filter System**: View all, pending, or completed tasks
- **Statistics Dashboard**: Real-time task counters
- **Local Storage**: Tasks persist across browser sessions
- **No Framework Dependencies**: Built with vanilla JavaScript

## Data Structure

This project demonstrates a **Singly Linked List** implementation:

- **Task**: Holds task data (description, completed status)
- **TaskNode**: Wraps a Task with a pointer to the next node
- **TaskList**: Manages the linked list with pointer-based operations

### Key Operations

- **Add Task**: Traverses to the end and links a new node
- **Remove Task**: Updates pointers to skip the removed node
- **Complete Task**: Traverses by position and toggles status
- **Iteration**: Uses `current.next` for traversal (no arrays)

## Project Structure

```
.
├── .agents/SKILL/      # Project skills
│   ├── SKILL.md
│   └── AGENT.md
└── todo_web/
    ├── index.html      # Main HTML structure
    ├── styles.css      # Modern CSS styling
    ├── app.js          # Linked List + UI logic
    └── README.md
```

## How to Run

1. Open `todo_web/index.html` in your browser
2. Or use a local server:

```bash
cd todo_web
python -m http.server 8000
```

Then open `http://localhost:8000`

## Rules Followed

- Only pointers/referenced used (no arrays for task storage)
- No `list`, `tuple`, `dict`, or `set` for task management
- All traversal via `node.next`
- Code in English
- Clean separation of concerns

## License

MIT
