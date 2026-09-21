# AGENT.md — Proyecto: Lista de Tareas Pendientes (Linked List To-Do)

## 1. Objetivo
Construir en **Python**, con **POO**, un gestor de tareas pendientes cuya única
estructura interna sea una **lista enlazada simple** hecha a mano (nodos + puntero
`next`), con un **frontend** (menú de consola) que la consuma.

## 2. Reglas obligatorias
1. **Solo punteros/referencias.** Cada tarea vive en un `TaskNode` con su dato y
   un puntero `next` al siguiente nodo. Toda la lógica (agregar, buscar,
   recorrer, eliminar, completar) se resuelve recorriendo con `current = current.next`.
2. **Prohibido usar `list`, `tuple`, `dict`, `set`, `deque` u otras estructuras
   nativas/`collections`** para almacenar o recorrer las tareas. Nada de
   índices, *slicing*, `.append()`, `.pop()`, `.insert()` como sustituto de punteros.
3. **Clases mínimas (POO):**
   - `Task`: el dato (descripción, completado).
   - `TaskNode`: envuelve una `Task` + puntero `next`.
   - `TaskList`: la lista enlazada (guarda `head`, expone `add_task`,
     `remove_task`, `complete_task`, `__iter__`, `__len__`).
   - `TodoCLI`: frontend, separado de `TaskList` (solo imprime/pide datos).
4. **Código en inglés** (clases, métodos, variables, comentarios).
5. **Frontend obligatorio:** menú con agregar, listar, completar, eliminar, salir.
6. **Separación de capas:** `TaskList` no imprime ni hace `input()`; eso es del frontend.

## 3. Estructura de archivos sugerida

```
todo_linked_list/
├── models/
│   ├── task.py         # class Task
│   ├── task_node.py    # class TaskNode (task + next)
│   └── task_list.py    # class TaskList (singly linked list logic)
├── frontend/
│   └── cli.py           # class TodoCLI (console menu, uses TaskList)
└── main.py               # entry point: wires TaskList + TodoCLI together
```

## 4. Checklist de validación (Definition of Done)
- [ ] Nada de `list`/`tuple`/`dict` para guardar tareas.
- [ ] Recorrido siempre vía `node.next`, nunca por índice.
- [ ] Existen `Task`, `TaskNode`, `TaskList` y `TodoCLI`.
- [ ] Insertar/eliminar/completar mantienen bien los punteros (`head`, `next`).
- [ ] Nombres en inglés.
- [ ] `TaskList` sin `print()`/`input()`.

## 5. Referencia
La skill `todo-linked-list` (`SKILL.md`) contiene la plantilla de clases y el
script de ejemplo que cumple estas reglas.