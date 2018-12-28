from bs4 import BeautifulSoup
import requests
import pytube
import os

if not os.path.exists('videos'):
    os.makedirs('videos')

os.chdir('videos')

video = str(input('Search: '))
video = video.split(' ')
video = '+'.join(video)

url = f'https://www.youtube.com/results?search_query={video}'

response = requests.get(url).text
cont = BeautifulSoup(response, 'lxml')
body = cont.body
link = body.findAll('a', class_ = 'yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link ')

for j, i in enumerate(link):
    print(f'{j+1}: ', i['title'])

n = int(input('CHoose the video: '))

flink = link[n - 1]

print(flink['title'])

watch = str(flink['href'])

title = str(flink['title'])
path = f'http://www.youtube.com{watch}'

print(f'LINK: {path}')
print(f'Downloading {title}...')

yt = pytube.YouTube(path)
stream = yt.streams.first()
stream.download()
