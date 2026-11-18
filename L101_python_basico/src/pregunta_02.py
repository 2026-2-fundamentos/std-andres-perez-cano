from pathlib import Path
import pandas as pd

ACTIVITY_DIR = Path(__file__).resolve().parents[1]
INPUT_FILE = ACTIVITY_DIR / "data" / "data.csv.gz"
def pregunta_02():
    """
    Cuente cuántos registros hay para cada letra de la primera columna
    (`letter`). Retorne una lista de tuplas `(letra, cantidad)` ordenada
    alfabéticamente por la letra.

    Ejemplo del formato de la respuesta:

        [("A", 8), ("B", 7), ("C", 5), ...]
    """
    df = pd.read_csv(INPUT_FILE, sep="\t", header=None, names=["letter", "value", "c2", "c3", "c4"])
    conteo = df["letter"].value_counts().sort_index()
    resultado = [(letra, int(cantidad)) for letra, cantidad in conteo.items()]
    
    return resultado
