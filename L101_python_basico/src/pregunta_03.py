from pathlib import Path
import pandas as pd

ACTIVITY_DIR = Path(__file__).resolve().parents[1]
INPUT_FILE = ACTIVITY_DIR / "data" / "data.csv.gz"

def pregunta_03():
    """
    Sume los valores de la segunda columna (`value`) para cada letra de la
    primera columna (`letter`). Retorne una lista de tuplas `(letra, suma)`
    ordenada alfabéticamente por la letra.

    Ejemplo del formato de la respuesta:

        [("A", 53), ("B", 36), ("C", 27), ...]
    """
    
    df = pd.read_csv(INPUT_FILE, sep="\t", header=None, names=["letter", "value", "c2", "c3", "c4"])
    suma = df.groupby("letter")["value"].sum()
    resultado = [(letra, int(valor)) for letra, valor in suma.items()]

    return resultado
    
