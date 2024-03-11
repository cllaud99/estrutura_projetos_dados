from pipeline.extract import extract_files_xlsx as e_xlsx


pasta = 'data/input'

lista = e_xlsx(pasta)

print(lista)