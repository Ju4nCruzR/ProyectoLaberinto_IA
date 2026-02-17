"""
Programa principal para resolver laberintos usando algoritmos de busqueda.
"""

import sys
import time
from src.laberinto import Laberinto
from src.grafo import Grafo
from src.busqueda_ciega import busqueda_anchura, busqueda_profundidad
from src.busqueda_a_estrella import busqueda_a_estrella
from src.visualizacion import visualizar_laberinto, imprimir_resultado, comparar_algoritmos


def main():
    """Funcion principal del programa"""
    
    # Verificar argumentos de linea de comandos
    if len(sys.argv) < 2:
        print("Uso: python main.py <ruta_archivo_laberinto>")
        print("\nEjemplo: python main.py ejemplos/laberinto_10x10.txt")
        return
    
    ruta_archivo = sys.argv[1]
    
    try:
        # Leer el laberinto desde archivo
        print(f"Leyendo laberinto desde: {ruta_archivo}")
        laberinto = Laberinto.desde_archivo(ruta_archivo)
        
        print("\n=== LABERINTO ORIGINAL ===")
        visualizar_laberinto(laberinto)
        
        print(f"\nInicio: {laberinto.inicio}")
        print(f"Meta: {laberinto.meta}")
        print(f"Dimensiones: {laberinto.filas}x{laberinto.columnas}")
        
        # Transformar a grafo
        print("\nTransformando laberinto a grafo...")
        grafo = Grafo(laberinto)
        print(f"Grafo creado con {len(grafo.lista_adyacencia)} nodos")
        
        # Ejecutar BFS
        print("\nEjecutando BFS...")
        inicio_tiempo = time.perf_counter()
        camino_bfs, nodos_bfs = busqueda_anchura(grafo, laberinto.inicio, laberinto.meta)
        tiempo_bfs = time.perf_counter() - inicio_tiempo
        imprimir_resultado("BFS (Busqueda en Anchura)", camino_bfs, nodos_bfs, tiempo_bfs)
        
        if camino_bfs:
            print("\n=== SOLUCION CON BFS ===")
            visualizar_laberinto(laberinto, camino_bfs)
        else:
            print("\nBFS no encontro solucion para este laberinto.")
        
        # Ejecutar DFS
        print("\nEjecutando DFS...")
        inicio_tiempo = time.perf_counter()
        camino_dfs, nodos_dfs = busqueda_profundidad(grafo, laberinto.inicio, laberinto.meta)
        tiempo_dfs = time.perf_counter() - inicio_tiempo
        imprimir_resultado("DFS (Busqueda en Profundidad)", camino_dfs, nodos_dfs, tiempo_dfs)
        
        if camino_dfs:
            print("\n=== SOLUCION CON DFS ===")
            visualizar_laberinto(laberinto, camino_dfs)
        else:
            print("\nDFS no encontro solucion para este laberinto.")
        
        # Ejecutar A*
        print("\nEjecutando A*...")
        inicio_tiempo = time.perf_counter()
        camino_a_estrella, nodos_a_estrella = busqueda_a_estrella(grafo, laberinto.inicio, laberinto.meta)
        tiempo_a_estrella = time.perf_counter() - inicio_tiempo
        imprimir_resultado("A* (A-Estrella)", camino_a_estrella, nodos_a_estrella, tiempo_a_estrella)
        
        if camino_a_estrella:
            print("\n=== SOLUCION CON A* ===")
            visualizar_laberinto(laberinto, camino_a_estrella)
        else:
            print("\nA* no encontro solucion para este laberinto.")
        
        # Comparar resultados
        resultados = {
            'BFS': {'camino': camino_bfs, 'nodos_explorados': nodos_bfs, 'tiempo': tiempo_bfs},
            'DFS': {'camino': camino_dfs, 'nodos_explorados': nodos_dfs, 'tiempo': tiempo_dfs},
            'A*': {'camino': camino_a_estrella, 'nodos_explorados': nodos_a_estrella, 'tiempo': tiempo_a_estrella}
        }
        
        comparar_algoritmos(resultados)
        
    except FileNotFoundError:
        print(f"Error: No se encontro el archivo '{ruta_archivo}'")
    except ValueError as e:
        print(f"Error en el formato del laberinto: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")


if __name__ == "__main__":
    main()
