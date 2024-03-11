from pipeline.extract import extract_files_xlsx
from pipeline.transform import concatenacao_lista_dataframe
from pipeline.load import load_excel


pasta_input = 'data/input'
pasta_output = 'data/output'
nome = 'consolidado'



if __name__ == "__main__":
    data_frame_lista = extract_files_xlsx(pasta_input)
    data_frame = concatenacao_lista_dataframe(data_frame_lista)
    load_excel(data_frame, pasta_output, nome)

