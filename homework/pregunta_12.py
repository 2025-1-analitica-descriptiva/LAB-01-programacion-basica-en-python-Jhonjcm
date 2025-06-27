"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


import csv
import os

def pregunta_12():
    base_path = os.path.dirname(os.path.dirname(__file__))
    full_path = os.path.join(base_path, "files", "input", "data.csv")

    with open(full_path, newline='', encoding='utf-8') as f:
        rows = list(csv.reader(f, delimiter='\t'))

    suma_por_letra = {}

    for row in rows:
        letra = row[0]
        pares = row[4].split(",")
        suma_valores = sum(int(par.split(":")[1]) for par in pares)
        if letra in suma_por_letra:
            suma_por_letra[letra] += suma_valores
        else:
            suma_por_letra[letra] = suma_valores

    return dict(sorted(suma_por_letra.items()))

    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
