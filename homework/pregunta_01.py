"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
import os


def pregunta_01():
    base_path = os.path.dirname(os.path.dirname(__file__))
    full_path = os.path.join(base_path, "files", "input", "data.csv")

    with open(full_path, newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo, delimiter='\t')
        suma = 0
        for fila in lector:
            suma += int(fila[1])

    return suma

    
"""
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
