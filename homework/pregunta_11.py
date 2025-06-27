"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


import csv
import os

def pregunta_11():
    base_path = os.path.dirname(os.path.dirname(__file__))
    full_path = os.path.join(base_path, "files", "input", "data.csv")

    with open(full_path, newline='', encoding='utf-8') as f:
        rows = list(csv.reader(f, delimiter='\t'))

    suma_por_letra = {}

    for row in rows:
        valor = int(row[1])
        letras = row[3].split(",")
        for letra in letras:
            inicial = letra[0]
            if inicial not in suma_por_letra:
                suma_por_letra[inicial] = valor
            else:
                suma_por_letra[inicial] += valor

    return dict(sorted(suma_por_letra.items()))

    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
