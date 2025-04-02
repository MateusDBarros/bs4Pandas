import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.scrapethissite.com/pages/simple/'

# Faz uma requisição para a URL da pagina e baixa o HTML
response = requests.get(url)

# Se a URL for invalida gera um erro e pausa o codigo
response.raise_for_status()

# Obtem e analisa o HTML e com o 'html.parser' cria uma estrutura navegavel
soup = BeautifulSoup(response.text, 'html.parser')

# Listas para armazernar os dados
paises = []
capitais = []


# Encontar todas as tags h3 com a classe country-name
for h3 in soup.find_all('h3', class_='country-name'):
    pais = h3.text.strip() # Pega o texto de h3 e remove os espaços extras
    paises.append(pais)

# Encontar todas as tags div com a classe country-capital
for div in soup.find_all('span', class_='country-capital'):
    capital = div.text.strip() # Pega o texto da div e remove os espaços
    capitais.append(capital) if capital else "desconhecido" # Armazena caso tenha encontrado o texto, caso contrario, armazena 'Desconhecido'

# Cria um dataframe com os dados
df = pd.DataFrame({'País': paises, 'Capital': capitais})

# Salva os dados em uma arquivo excel
df.to_excel('paises_capitais.xlsx', index=False)

print('Arquivo excel criado com sucesso: "paises_capitais.xlsx"')