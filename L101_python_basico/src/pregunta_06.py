import pandas as pd
from pathlib import Path

ACTIVITY_DIR = Path(__file__).resolve().parents[1]
INPUT_FILE = ACTIVITY_DIR / "data" / "data.csv.gz"

def pregunta_06():
    """
    La quinta columna (`metrics`) contiene pares `clave:valor` separados por
    comas. Para cada clave, encuentre el valor mínimo y el valor máximo que
    aparecen en todo el archivo. Retorne una lista de tuplas
    `(clave, mínimo, máximo)` ordenada alfabéticamente por la clave.

    Observe que el orden es mínimo y luego máximo, al contrario de la
    pregunta 5.

    Ejemplo del formato de la respuesta:

        [("aaa", 1, 9), ("bbb", 1, 9), ...]
    """
    df = pd.read_csv(INPUT_FILE, sep="\t", header=None, names=["letter", "value", "date", "c3", "metrics"])

    lista_plana = df["metrics"].str.split(",").explode().tolist()

    grupos = {}
    for item in lista_plana:
        clave, valor = item.split(":")
        valor = int(valor)

        if clave not in grupos:
           grupos[clave] = []
        grupos[clave].append(valor)

    resultado = [
        (clave, min(grupos[clave]), max(grupos[clave]))
        for clave in sorted(grupos.keys())
    ]

    return resultado
    

