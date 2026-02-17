 # Solucionador de Laberintos con IA

Proyecto de Inteligencia Artificial que implementa algoritmos de búsqueda para resolver laberintos.

# Integrantes

Juan Sebastián Cruz
Juan Diego Soler
Santiago Rayo

## Descripción

Este proyecto implementa diferentes algoritmos de búsqueda para encontrar la solución óptima en laberintos representados como matrices NxN:

- **Búsqueda a Ciegas**: BFS (Breadth-First Search) y DFS (Depth-First Search)
- **Búsqueda Heurística**: A* (A-Star)

El programa transforma un laberinto (matriz) en un grafo y aplica los algoritmos para encontrar el camino desde la entrada hasta la meta.

## Características

- Lectura de laberintos desde matriz Python
- Transformación de matriz a grafo (lista de adyacencia)
- Búsqueda en Anchura (BFS)
- Búsqueda en Profundidad (DFS)
- Algoritmo A* con heurística Manhattan
- Visualización de la solución
- Soporte para laberintos de tamaño NxN

## Estructura del Proyecto

laberinto-ia/
├── src/
│   ├── nodo.py                    # Clase Nodo para el grafo
│   ├── laberinto.py               # Lectura y manejo del laberinto
│   ├── grafo.py                   # Transformación matriz → grafo
│   ├── heuristica.py              # Cálculo de heurísticas
│   ├── busqueda_ciega.py          # Implementación BFS y DFS
│   ├── busqueda_a_estrella.py     # Implementación A*
│   └── visualizacion.py           # Visualización de resultados
├── tests/                          # Tests unitarios
├── ejemplos/                       # Laberintos de ejemplo
├── main.py                         # Programa principal
└── README.md
```

##  Instalación

### Requisitos
- Python 3.8 o superior

### Pasos

1. Clonar el repositorio:
```bash
git clone https://github.com/Ju4nCruzR/ProyectoLaberinto_IA.git
cd ProyectoLaberinto_IA
```

2. (Opcional) Crear entorno virtual:
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Uso

### Formato del Laberinto

El laberinto se representa como una matriz NxN donde:
- `0` = Espacio libre
- `1` = Pared
- `2` = Entrada (salida)
- `3` = Meta (objetivo)

**Ejemplo:**
```python
laberinto = [
    [2, 1, 1, 1, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 1, 1, 1, 0, 0, 1, 0],
    [1, 1, 0, 0, 0, 1, 0, 1, 1, 1],
    [0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 1, 0, 1, 0, 1, 0, 0, 1, 1],
    [0, 0, 0, 1, 0, 3, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 1]
]
```

### Ejecutar el Programa
```bash
python main.py
```

El programa mostrará:
1. El laberinto original
2. La ruta encontrada por BFS
3. La ruta encontrada por DFS
4. La ruta encontrada por A*
5. Comparación de rendimiento

## Ejemplo de Salida
```
=== LABERINTO ORIGINAL ===
S # # # . . # # # #
. . . # # # . . # .
# # . . . # . # # #
. # # # . # . # . #
# # . # . # . . # #
. . . # . M # . # .
# # # # # . # . # #
# . . . . # # # . #
# # # # # # . # . #
# . # . # . # # # #

=== SOLUCION CON BFS ===
Solucion encontrada!
Longitud del camino: 12
Nodos explorados: 45
Camino: [(0,0), (1,0), (1,1), ..., (5,5)]

=== SOLUCION CON DFS ===
Solucion encontrada!
Longitud del camino: 18
Nodos explorados: 32
Camino: [(0,0), (1,0), (2,0), ..., (5,5)]

=== SOLUCION CON A* ===
Solucion encontrada!
Longitud del camino: 12
Nodos explorados: 18
Camino: [(0,0), (1,0), (1,1), ..., (5,5)]
```

##  Algoritmos Implementados

### BFS (Breadth-First Search)
- Explora por niveles
- Garantiza encontrar el camino más corto
- Complejidad: O(V + E)

### DFS (Depth-First Search)
- Explora en profundidad
- No garantiza el camino más corto
- Complejidad: O(V + E)

### A* (A-Star)
- Búsqueda informada con heurística
- Garantiza el camino óptimo
- Heurística: Distancia Manhattan
- Complejidad: O(b^d) donde b es el factor de ramificación

##  Proyecto Académico

**Universidad:** Pontificia Universidad Javeriana  
**Curso:** Introducción a la Inteligencia Artificial  
**Profesor:** Ing. Julio Omar Palacio Niño, M.Sc.  
**Período:** 2026-1

## Licencia

Este proyecto es de uso académico para la Pontificia Universidad Javeriana.