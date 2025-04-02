# 📈 Projeto de Web Scraping e Manipulação de Dados com Python

## ✨ Descrição
Este projeto realiza **web scraping** para coletar dados de um site, extrair informações sobre **países e suas capitais** e armazená-las em um arquivo Excel. Após a coleta, o usuário pode pesquisar por um país ou capital interativamente.

## ⚛️ Tecnologias Utilizadas
- **Python 3.x**  
- **Requests** → Para fazer requisições HTTP e obter o HTML do site.  
- **BeautifulSoup** → Para extrair e manipular dados do HTML.  
- **Pandas** → Para manipulação de tabelas e arquivos Excel.  
- **OpenPyXL** → Para salvar e ler arquivos Excel (`.xlsx`).

## 🔧 Instalação
Antes de rodar o projeto, instale as dependências necessárias:
```bash
pip install requests beautifulsoup4 pandas openpyxl
```
## 🎮 Como Rodar o Projeto
1. Execute o script de web scraping para coletar os dados:
```bash
python scraping.py
```

2. Execute o script de manipulação do Excel para buscar informações:
```bash
python buscar_paises.py
```

3. Digite o nome de um país ou capital quando solicitado para pesquisar na tabela

## 📊 Exemplo de Uso
```bash
Digite um nome de país ou capital: Brasil

Resultado encontrado:
País: Brasil
Capital: Brasília

```
