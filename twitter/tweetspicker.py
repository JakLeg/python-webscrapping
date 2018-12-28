import requests
from bs4 import BeautifulSoup

user_ = str(input('Digite o nome do usuario de quem deseja pegar os tweets: @')) 

url = f'https://twitter.com/{user_}'

response = requests.get(url).text
cont = BeautifulSoup(response, 'lxml')

tweets = cont.find_all('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')


for p in tweets:
	p = str(p.contents[0])
	if str(p) == '':
		print('***IMAGEM***')
	else:
		print(p)
	print('\n',30*'-=-', end = '\n')


