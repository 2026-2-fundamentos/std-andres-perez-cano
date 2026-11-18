import pandas as pd
from pathlib import Path

ACTIVITY_DIR = Path(__file__).resolve().parents[1]
INPUT_FILE = ACTIVITY_DIR / "data" / "data.csv.gz"

def pregunta_07():
    """
    Para cada valor distinto de la segunda columna (`value`), construya la
    lista de letras de la primera columna (`letter`) que aparecen con ese
    valor. Conserve las letras repetidas y el orden en que aparecen en el
    archivo. Retorne una lista de tuplas `(valor, letras)` ordenada por el
    valor.

    Ejemplo del formato de la respuesta:

        [(0, ["C"]), (1, ["E", "B", "E"]), (2, ["A", "E"]), ...]
    """
    df = pd.read_csv(INPUT_FILE, sep="\t", header=None, names=["letter", "value", "date", "c3", "metrics"])
    
    valores = df.groupby("value")["letter"].apply(list)
    resultado = [(int(valor), letras) for valor, letras in valores.items()]
    
    return resultado

    
