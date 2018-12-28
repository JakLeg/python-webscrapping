import requests
from bs4 import	BeautifulSoup
import urllib.request
from random import randint
from selenium import webdriver
from time import sleep

lista = []

def get_url(user_):
	global lista
	url = f'https://www.instagram.com/{user_}/'
	i = 1
	driver = webdriver.Chrome('/home/james/Documents/Dev/Python/chromedriver_linux64/chromedriver')
	driver.get(url)
	sleep(3)

	last_height = driver.execute_script("return document.body.scrollHeight")

	while True:
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

		sleep(1.5)

		new_height = driver.execute_script("return document.body.scrollHeight")
		
		if new_height == last_height:
		    break
		else:
		    response = driver.page_source
		    last_height = new_height


	cont = BeautifulSoup(response, 'lxml')
	driver.close()
	body = cont.body

	divs = body.find_all('div', class_='v1Nh3 kIKUG _bz0w')

	for div in divs:
		lista.append(str(div.a['href']))

def download_image(url):

	response = requests.get(url).text
	cont = BeautifulSoup(response, 'lxml')
	head = cont.head
	filt1 = cont.find_all('meta')
	filt2 = str(filt1).split('"')
	url3 = filt2[37]
	download_final(url3)

j = 1

def download_final(url):
	global j
	full_name = str(j)
	urllib.request.urlretrieve(url,full_name)
	j+=1

user_ =  str(input('Digite o nome do usuario de quem deseja baixar as fotos: @'))

get_url(user_)

for k,i in enumerate(lista):
	url = f'https://www.instagram.com{i}?taken-by={user_}'
	print(f'{k+1} - Baixando img = {i}')
	download_image(url)









	

