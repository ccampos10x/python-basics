import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

titulos = soup.find_all('a', class_='titlelink')
if not titulos:
    titulos = soup.select('span.titleline > a ')


for i, titulo in enumerate(titulos[:20], start=1):
        print(f"{i}. {titulo.text}")