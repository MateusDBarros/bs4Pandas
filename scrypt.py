import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.scrapethissite.com/pages/simple/'

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

paises = []
capitais = []

for h3 in soup.find_all('h3', class_='country-name'):
    pais = h3.text.strip()
    paises.append(pais)

for div in soup.find_all('span', class_='country-capital'):
    capital = div.text.strip()
    capitais.append(capital) if capital else "desconhecido"

df = pd.DataFrame({'País': paises, 'Capital': capitais})
df.to_excel('paises_capitais.xlsx', index=False)

print('Arquivo excel criado com sucesso: "paises_capitais.xlsx"')