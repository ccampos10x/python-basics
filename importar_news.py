import requests
from bs4 import BeautifulSoup

url = "https://base44.com/lp-pt"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

titulos = soup.find_all('a', class_='titlelink')
if not titulos:
    titulos = soup.select('span.titleline > a ')


for i, titulo in enumerate(titulos[:10], start=1):
        print(f"{i}. {titulo.text}")