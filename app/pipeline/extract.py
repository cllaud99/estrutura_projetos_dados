import pandas as pd
import os
import glob
from typing import List


path_input = 'data/input'


def extract_files_xlsx (path: str) -> List[pd.DataFrame]:

    """
    Função para ler os arquivos de 
    uma pasta data/input e retornar uma lista de df

    args: input_path (str:) caminho da pasta com os arquivos

    return: lista de dataframes
    """

    all_files = glob.glob(os.path.join(path_input, "*.xlsx"))
    df_list = []
    for arquivo in all_files:
        df_list.append(pd.read_excel(arquivo))
    return df_list

if __name__== "__main__":
    lista_df = extract_files_xlsx(path_input)
    print(lista_df)