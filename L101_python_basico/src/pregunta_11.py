import pandas as pd
from pathlib import Path

ACTIVITY_DIR = Path(__file__).resolve().parents[1]
INPUT_FILE = ACTIVITY_DIR / "data" / "data.csv.gz"

def pregunta_11():
    """
    La cuarta columna (`codes`) contiene letras minúsculas separadas por
    comas. Para cada una de esas letras, sume los valores de la segunda
    columna (`value`) de los registros en los que aparece. Retorne un
    diccionario `{letra: suma}` con las letras en orden alfabético.

    Ejemplo del formato de la respuesta:

        {"a": 122, "b": 49, "c": 91, ...}
    """

    df = pd.read_csv(INPUT_FILE, sep="\t", header=None, names=["letter", "value", "date", "codes", "metrics"])
    df["codes_lista"] = df["codes"].str.split(",")

    acumulador = {}

    for valor, lista_letras in zip(df["value"], df["codes_lista"]):
        for letra in lista_letras:
            # Si la letra no existe en el diccionario, empieza en 0 y le suma el valor
            acumulador[letra] = acumulador.get(letra, 0) + valor
 
    # Convertimos el diccionario a la lista de tuplas final
    resultado = dict(sorted(acumulador.items()))
    
    return resultado
