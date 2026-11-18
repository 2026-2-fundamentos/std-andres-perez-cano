import pandas as pd
from pathlib import Path

ACTIVITY_DIR = Path(__file__).resolve().parents[1]
INPUT_FILE = ACTIVITY_DIR / "data" / "data.csv.gz"

def pregunta_08():
    """
    Repita la pregunta 7, pero ahora cada lista de letras debe contener cada
    letra una sola vez y estar ordenada alfabéticamente. Retorne una lista de
    tuplas `(valor, letras)` ordenada por el valor.

    Ejemplo del formato de la respuesta:

        [(0, ["C"]), (1, ["B", "E"]), (2, ["A", "E"]), ...]
    """

    df = pd.read_csv(INPUT_FILE, sep="\t", header=None, names=["letter", "value", "date", "c3", "metrics"])
        
    valores = df.groupby("value")["letter"].apply(lambda x: sorted(set(x)))
    resultado = [(int(valor), sorted(letras)) for valor, letras in valores.items()]
        
    return resultado
