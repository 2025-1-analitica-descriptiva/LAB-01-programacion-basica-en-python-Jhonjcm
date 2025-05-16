"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
import os

def leer_csv():
    ruta = os.path.join(os.path.dirname(__file__), "..","files","input", "data.csv")
    with open(ruta, newline='', encoding='utf-8') as archivo:
        lector = list(csv.reader(archivo, delimiter='\t'))
    return lector



def pregunta_01():
    suma = 0
    fila = leer_csv()
    for fila in filas:
        suma += int(fila[1])
    return suma

# Uso correcto:
filas = leer_csv()
print(pregunta_01())

    
"""
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
