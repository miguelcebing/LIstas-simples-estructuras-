# Listas Simples - Estructuras de Datos

Proyecto de implementación de listas enlazadas simples en Python y web.

## Estructura del Proyecto

```
.
├── .agents/SKILL/      # Skills del proyecto
│   ├── SKILL.md        # Definición de la skill
│   └── AGENT.md        # Reglas del proyecto
└── todo_web/           # Implementación Web (HTML/CSS/JS)
    ├── index.html      # Estructura HTML
    ├── styles.css      # Estilos modernos
    ├── app.js          # Lógica con Linked List
    └── README.md       # Documentación
```

## Cómo Ejecutar

1. Abre `todo_web/index.html` en tu navegador
2. O usa un servidor local:

```bash
cd todo_web
python -m http.server 8000
```

Luego abre `http://localhost:8000`

## Características

- Tema oscuro moderno con gradientes
- Animaciones suaves
- Filtros (All/Pending/Completed)
- Estadísticas en tiempo real
- Responsive design
- Persistencia con LocalStorage
- Implementación con punteros exclusivamente

## Reglas

- Solo punteros/referencias para navegación
- Prohibido usar list, tuple, dict para almacenamiento
- Código en inglés
- Separación de capas (lógica vs presentación)

## Licencia

MIT
