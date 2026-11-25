import pandas as pd
from pathlib import Path

ACTIVITY_DIR = Path(__file__).resolve().parents[1]
INPUT_FILE1 = ACTIVITY_DIR / "data" / "tbl0.tsv"
INPUT_FILE2 = ACTIVITY_DIR / "data"/ "tbl2.tsv"

def pregunta_13():
    """
    Combine las tablas `data/tbl0.tsv` y `data/tbl2.tsv` usando la columna
    `c0`, que ambas comparten. Luego, sume los valores de la columna `c5b`
    para cada categoría de la columna `c1`. Retorne una Serie de Pandas cuyo
    índice son las categorías, en orden alfabético, y cuyos valores son las
    sumas.

    Ejemplo del formato de la respuesta:

        c1
        A    146
        B    134
        C     81
        ...
    """

    df1 = pd.read_csv(INPUT_FILE1, sep='\t')
    df2 = pd.read_csv(INPUT_FILE2, sep='\t')

    resultado = pd.merge(df1, df2, on="c0", how="inner")
    frame = resultado.groupby("c1")["c5b"].sum()
    return frame
