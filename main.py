import pandas as pd
import openpyxl


excel_path = 'paises_capitais.xlsx'


df = pd.read_excel(excel_path) # Le o arquivo excel
pais = df[['País']] # Pega todos os valores da coluna 'Pais'
capital = df[['Capital']] # Peaga todos os valores da coluna 'Capital'

brazil = df[df.eq('Brazil').any(axis=1)] # Procura um valor especifico e retona o indice, assim como seu respectivo 'Pais' e 'Capital'

# Prints para os testes
print(pais)
print('\n-----------------------------\n')
print(capital)
print('\n-----------------------------\n')
print(brazil)