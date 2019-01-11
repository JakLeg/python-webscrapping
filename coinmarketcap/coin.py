import requests
from bs4 import BeautifulSoup

# URL from the site
url = 'https://coinmarketcap.com'

# getting the html source code with requests
r = requests.get(url).text

# initializing a BeautifulSoup object
cont = BeautifulSoup(r, 'lxml')

# creating a list with all elements with TR tag
tr = cont.findAll('tr', {'class':''})

# iterating in the elements and taking the name and price for first 20 coins
for pos, td in enumerate(tr[1:21]):
    name = td.find('a', class_ = 'currency-name-container link-secondary').text
    price = td.find('a', class_ = 'price').text
    #print(td)
    print(f'{pos+1} - {name}: {price}')
