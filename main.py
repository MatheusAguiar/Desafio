import requests
import hashlib
from bs4 import BeautifulSoup

#Link da página
url = 'http://www.stf.jus.br/portal/diariojusticaeletronico/pesquisardiarioeletronico.asp'

#Cabeçalho de requisição
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'}

#Solicita URL e obtém objeto de resposta
response = requests.get(url, headers=headers)


#Analisa o texto da URL
soup = BeautifulSoup(response.text, "html5lib")

# Encontre todos os links da página
links = soup.find_all('a')








