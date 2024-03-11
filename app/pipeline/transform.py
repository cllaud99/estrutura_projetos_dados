import pandas as pd
from typing import List



def concatenacao_lista_dataframe(data_frame_list: List[pd.DataFrame]) -> pd.DataFrame:

    """
    Função para transformar uma lista de dataframe
    em um único dataframe
    """
    return pd.concat(data_frame_list, ignore_index=True)