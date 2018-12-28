import requests 
from bs4 import	BeautifulSoup
import urllib.request

def download_image(url):
    full_name = url.split('/')[4]
    urllib.request.urlretrieve(url,full_name)

user_ =  str(input('Digite o nome do usuario de quem deseja baixar as fotos: ')) 

url = f'https://twitter.com/{user_}'

response = requests.get(url).text
cont = BeautifulSoup(response, 'lxml')

img_src = ''

for i in cont.find_all('img'):	
	try:
		img_src = i['src']
		if 'bigger' not in img_src and 'normal' not in img_src: 
			print(img_src)
			download_image(img_src)
	except:
		pass
