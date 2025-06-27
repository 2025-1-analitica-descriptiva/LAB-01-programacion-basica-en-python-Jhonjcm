"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


import csv
import os

def pregunta_06():
    base_path = os.path.dirname(os.path.dirname(__file__))
    full_path = os.path.join(base_path, "files", "input", "data.csv")

    with open(full_path, newline='', encoding='utf-8') as f:
        rows = list(csv.reader(f, delimiter='\t'))

    extremos = {}

    for row in rows:
        columna_5 = row[4]  # columna con los pares clave:valor
        pares = columna_5.split(",")
        for par in pares:
            clave, valor = par.split(":")
            valor = int(valor)
            if clave not in extremos:
                extremos[clave] = [valor, valor]  # [max, min]
            else:
                if valor > extremos[clave][0]:
                    extremos[clave][0] = valor
                if valor < extremos[clave][1]:
                    extremos[clave][1] = valor

    resultado = [(clave, extremos[clave][1], extremos[clave][0]) for clave in sorted(extremos)]
    return resultado
    

    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
