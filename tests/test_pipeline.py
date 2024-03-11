from typing import List

import pandas as pd

from app.pipeline.transform import concatenacao_lista_dataframe

df_1 = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
df_2 = pd.DataFrame({'col1': [5, 6], 'col2': [7, 8]})


def test_transform():
    lista_dataframes = [df_1, df_2]
    df = concatenacao_lista_dataframe(lista_dataframes)

    assert df.shape == (4, 2)
    assert df.equals(df)
