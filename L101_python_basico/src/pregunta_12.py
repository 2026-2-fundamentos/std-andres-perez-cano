import pandas as pd
from pathlib import Path

ACTIVITY_DIR = Path(__file__).resolve().parents[1]
INPUT_FILE = ACTIVITY_DIR / "data" / "data.csv.gz"

def pregunta_12():
    """
    Para cada letra de la primera columna (`letter`), sume todos los valores
    numéricos de los pares `clave:valor` de la quinta columna (`metrics`).
    Retorne un diccionario `{letra: suma}` con las letras en orden alfabético.

    Ejemplo del formato de la respuesta:

        {"A": 177, "B": 187, "C": 114, ...}
    """

    df = pd.read_csv(INPUT_FILE, sep="\t", header=None, names=["letter", "value", "date", "codes", "metrics"])
    
    letter_metrics = df.groupby("letter")["metrics"].apply(list)
    for letra, lista_cadenas in letter_metrics.items():
        nueva_lista = []
        for cadena in lista_cadenas:
            nueva_lista.extend(cadena.split(","))
        letter_metrics[letra] = nueva_lista

    resultado = [(letra, sum(int(par.split(":")[1]) for par in metrica)) for letra, metrica in letter_metrics.items()]
 
    return dict(resultado)