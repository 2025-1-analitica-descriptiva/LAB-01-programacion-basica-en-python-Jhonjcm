"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
import os

def pregunta_07():
    base_path = os.path.dirname(os.path.dirname(__file__))
    full_path = os.path.join(base_path, "files", "input", "data.csv")

    with open(full_path, newline='', encoding='utf-8') as f:
        rows = list(csv.reader(f, delimiter='\t'))

    asociaciones = {}

    for row in rows:
        letra = row[0]
        numero = int(row[1])
        if numero not in asociaciones:
            asociaciones[numero] = [letra]
        else:
            asociaciones[numero].append(letra)

    resultado = sorted(asociaciones.items())
    return resultado


    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

    """
