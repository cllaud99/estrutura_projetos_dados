import pandas as pd
import os




def load_excel(data_frame: pd.DataFrame, output_path: str, file_name: str) -> str:
    """
        Recebe um dataframe e salva como excel
        args:
            data_frame (pd.DataFrame): dataframe a ser salvo como excel
            output (str): pasta onde será salvo o arquivo
            file_name (str): o nome do arquivo
        return
            arquivo salvo com sucesso
    """
    if not os.path.exists(output_path):
        os.makedirs(output_path)
        
    data_frame.to_excel(f"{output_path}/{file_name}.xlsx", index=False)
    return "Arquivo salvo"