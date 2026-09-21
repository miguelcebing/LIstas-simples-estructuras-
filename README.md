# Listas Simples - Estructuras de Datos

Proyecto de implementación de listas enlazadas simples en Python y web.

## Estructura del Proyecto

```
.
├── .agents/SKILL/          # Skills del proyecto
│   ├── SKILL.md           # Definición de la skill
│   └── AGENT.md           # Reglas del proyecto
├── todo_linked_list/       # Implementación Python (Terminal + GUI)
│   ├── models/            # Modelo de datos
│   │   ├── task.py        # Clase Task
│   │   ├── task_node.py   # Clase TaskNode
│   │   └── task_list.py   # Clase TaskList
│   ├── frontend/          # Interfaces
│   │   ├── cli.py         # Terminal
│   │   └── gui.py         # GUI (tkinter)
│   ├── main.py            # Entry point
│   └── test.py            # Pruebas
└── todo_web/              # Implementación Web (HTML/CSS/JS)
    ├── index.html         # Estructura HTML
    ├── styles.css         # Estilos modernos
    ├── app.js             # Lógica con Linked List
    ├── vercel.json        # Configuración Vercel
    └── README.md          # Documentación web
```

## Implementaciones

### Python (todo_linked_list/)
- Interfaz de terminal (CLI)
- Interfaz gráfica (GUI con tkinter)
- Implementación con punteros exclusivamente

### Web (todo_web/)
- HTML/CSS/JavaScript puro
- Diseño moderno oscuro
- Responsive design
- LocalStorage para persistencia
- Lista enlazada en JavaScript

## Despliegue

### Vercel (Web)
```bash
cd todo_web
vercel
```

### Python
```bash
cd todo_linked_list
python main.py
```

## Reglas

- Solo punteros/referencias para navegación
- Prohibido usar list, tuple, dict para almacenamiento
- Código en inglés
- Separación de capas (lógica vs presentación)

## Licencia

MIT
