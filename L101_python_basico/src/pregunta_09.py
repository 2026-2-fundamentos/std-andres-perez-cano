import pandas as pd
from pathlib import Path

ACTIVITY_DIR = Path(__file__).resolve().parents[1]
INPUT_FILE = ACTIVITY_DIR / "data" / "data.csv.gz"

def pregunta_09():
    """
    Cuente cuántas veces aparece cada clave en la quinta columna (`metrics`)
    de todo el archivo. Retorne un diccionario `{clave: cantidad}` con las
    claves en orden alfabético.

    Ejemplo del formato de la respuesta:

        {"aaa": 13, "bbb": 16, "ccc": 23, ...}
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

    resultado = [(clave, len(grupos[clave])) for clave in sorted(grupos.keys())]

    return dict(resultado)
