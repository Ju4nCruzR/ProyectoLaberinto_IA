"""
Script para generar laberintos de prueba de diferentes tamanos.
"""

import random

def generar_laberinto(tamano, densidad_paredes=0.3):
    """
    Genera un laberinto aleatorio.
    
    Args:
        tamano (int): Dimension NxN del laberinto
        densidad_paredes (float): Porcentaje de paredes (0.0 a 1.0)
    
    Returns:
        list: Matriz del laberinto
    """
    matriz = []
    
    for fila in range(tamano):
        linea = []
        for columna in range(tamano):
            # Inicio en esquina superior izquierda
            if fila == 0 and columna == 0:
                linea.append(2)
            # Meta en esquina inferior derecha
            elif fila == tamano - 1 and columna == tamano - 1:
                linea.append(3)
            # Generar pared o espacio
            else:
                if random.random() < densidad_paredes:
                    linea.append(1)
                else:
                    linea.append(0)
        matriz.append(linea)
    
    return matriz


def guardar_laberinto(matriz, nombre_archivo):
    """Guarda el laberinto en un archivo de texto"""
    with open(nombre_archivo, 'w') as archivo:
        for fila in matriz:
            linea = ' '.join(map(str, fila))
            archivo.write(linea + '\n')


def main():
    """Genera laberintos de diferentes tamanos"""
    
    # Laberinto 50x50
    print("Generando laberinto 50x50...")
    lab_50 = generar_laberinto(50, densidad_paredes=0.25)
    guardar_laberinto(lab_50, 'laberinto_50x50.txt')
    print("Guardado: laberinto_50x50.txt")
    
    # Laberinto 100x100
    print("Generando laberinto 100x100...")
    lab_100 = generar_laberinto(100, densidad_paredes=0.25)
    guardar_laberinto(lab_100, 'laberinto_100x100.txt')
    print("Guardado: laberinto_100x100.txt")
    
    # Laberinto 1000x1000
    print("Generando laberinto 1000x1000...")
    lab_1000 = generar_laberinto(1000, densidad_paredes=0.25)
    guardar_laberinto(lab_1000, 'laberinto_1000x1000.txt')
    print("Guardado: laberinto_1000x1000.txt")
    
    print("\nLaberintos generados exitosamente!")


if __name__ == "__main__":
    main()