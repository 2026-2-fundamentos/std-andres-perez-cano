import pandas as pd
from pathlib import Path

ACTIVITY_DIR = Path(__file__).resolve().parents[1]
INPUT_FILE = ACTIVITY_DIR / "data" / "data.csv.gz"

def pregunta_10():
    """
    Para cada registro del archivo, en el mismo orden en que aparecen,
    retorne una tupla con la letra de la primera columna (`letter`), la
    cantidad de elementos de la cuarta columna (`codes`) y la cantidad de
    pares de la quinta columna (`metrics`). El resultado es una lista con una
    tupla por registro.

    Ejemplo del formato de la respuesta:

        [("E", 3, 5), ("A", 3, 4), ("B", 4, 4), ...]
    """

    df = pd.read_csv(INPUT_FILE, sep="\t", header=None, names=["letter", "value", "date", "codes", "metrics"])
        
    df["metrics_lista"] = df["metrics"].str.split(",")
    df["codes_lista"] = df["codes"].str.split(",")
    lista_tuplas = []

    for letra, code, metrica in zip(df["letter"],df["codes_lista"], df["metrics_lista"]):
        lista_tuplas.append((letra, len(code), len(metrica)))

    return lista_tuplas