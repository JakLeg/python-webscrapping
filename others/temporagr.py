import requests
from bs4 import BeautifulSoup
estado = str(input('Digite a sigla do seu estado(Ex: SP): ')).upper().strip()
cidade = str(input('Digite o nome de sua cidade(Ex: Jacarei): ')).lower().strip().replace(' ', '')
url = f'http://www.tempoagora.com.br/previsao-do-tempo/{estado}/{cidade}'
response = requests.get(url).text
cont = BeautifulSoup(response, 'lxml')
temp = cont.find('li', class_ = 'dsp-cell degree').text.strip()

print(temp)

print('\n')
print('-='*25)
print(f'A temperatura atual de {cidade.capitalize()}/{estado} é: {temp}°C')
print('-='*25)
print('\n')
