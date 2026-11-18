import pandas as pd
from pathlib import Path

ACTIVITY_DIR = Path(__file__).resolve().parents[1]
INPUT_FILE = ACTIVITY_DIR / "data" / "data.csv.gz"

def pregunta_05():
    """
    Para cada letra de la primera columna (`letter`), encuentre el valor
    máximo y el valor mínimo de la segunda columna (`value`). Retorne una lista
    de tuplas `(letra, máximo, mínimo)` ordenada alfabéticamente por la letra.

    Ejemplo del formato de la respuesta:

        [("A", 9, 2), ("B", 9, 1), ...]
    """
    df = pd.read_csv(INPUT_FILE, sep="\t", header=None, names=["letter", "value", "date", "c3", "c4"])
    valores = df.groupby("letter")["value"].agg(["max", "min"])
    resultado = [(letra, int(fila["max"]), int(fila["min"])) for letra, fila in valores.iterrows()]

    return resultado
