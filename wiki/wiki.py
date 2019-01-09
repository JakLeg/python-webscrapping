import requests
from bs4 import BeautifulSoup

def wiki_get(url):
    #print(url)

    r = requests.get(url).text
    cont = BeautifulSoup(r, 'lxml')
    paragraphs = cont.body.findAll('p')
    print('-=-'*20)
    print()
    print(paragraphs[2].text)
    print()
    print('-=-'*20)

'''
# treating the url
url = input('Search: ')
url = str(input('search: ')).strip()
url = url.split(' ')
url = '_'.join(url)
url = f'https://pt.wikipedia.org/wiki/{url}'
'''
