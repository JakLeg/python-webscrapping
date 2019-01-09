import requests
from bs4 import BeautifulSoup
import json
from wiki import wiki_get

url = input('Search: ')
url = url.split(' ')
url = '+'.join(url)
url = f'https://duckduckgo.com/?q={url}&ia=news'
#print(url)

r = requests.get(url).text
cont = BeautifulSoup(r, 'lxml')
body = cont.body
script = body.find_all('script')[7]

js = str(script.text)
size = len(js)
js = js[39:size-5]

data = json.loads(js)
data = data['data']

wiki_get(data['AbstractURL'])
