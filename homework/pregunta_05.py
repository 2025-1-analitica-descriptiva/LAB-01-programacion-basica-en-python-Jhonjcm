"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv
import os

def pregunta_05():
    base_path = os.path.dirname(os.path.dirname(__file__))
    full_path = os.path.join(base_path, "files", "input", "data.csv")

    with open(full_path, newline='', encoding='utf-8') as f:
        rows = list(csv.reader(f, delimiter='\t'))

    extremos = {}

    for row in rows:
        letra = row[0]
        valor = int(row[1])
        if letra not in extremos:
            extremos[letra] = [valor, valor]  # [max, min]
        else:
            if valor > extremos[letra][0]:
                extremos[letra][0] = valor
            if valor < extremos[letra][1]:
                extremos[letra][1] = valor

    resultado = [(letra, extremos[letra][0], extremos[letra][1]) for letra in sorted(extremos)]
    return resultado
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
