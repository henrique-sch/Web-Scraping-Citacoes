import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
button = soup.find_all('li', class_='next')

print(f'Escrevendo página {url}')
while button:
    for quote in soup.find_all('div', class_='quote'):
        text = ((quote.find_all('span')[0]).get_text())
        author = ((((quote.find_all('span')[1]).get_text()).split('\n'))[0])[3:]
        with open('contents.txt', 'a',encoding='utf-8') as arq:
            arq.write(text + '\n')
            arq.write(author + '\n')
            arq.write('\n')
    comp_link = soup.find_all('li', class_='next')[0].find('a')['href']
    url = 'https://quotes.toscrape.com' + comp_link
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    button = soup.find_all('li', class_='next')
    print(f'Escrevendo página {url}')


for quote in soup.find_all('div', class_='quote'):
    text = ((quote.find_all('span')[0]).get_text())
    author = ((((quote.find_all('span')[1]).get_text()).split('\n'))[0])[3:]
    with open('contents.txt', 'a',encoding='utf-8') as arq:
        arq.write(text + "\n")
        arq.write(author + "\n")
        arq.write('\n')

