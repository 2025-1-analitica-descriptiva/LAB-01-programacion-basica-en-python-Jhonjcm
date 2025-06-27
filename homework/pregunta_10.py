"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


import csv
import os

def pregunta_10():
    base_path = os.path.dirname(os.path.dirname(__file__))
    full_path = os.path.join(base_path, "files", "input", "data.csv")

    with open(full_path, newline='', encoding='utf-8') as f:
        rows = list(csv.reader(f, delimiter='\t'))

    resultado = []

    for row in rows:
        letra = row[0]
        col_4_count = len(row[3].split(","))
        col_5_count = len(row[4].split(","))
        resultado.append((letra, col_4_count, col_5_count))

    return resultado

    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
