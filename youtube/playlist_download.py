from bs4 import BeautifulSoup
import requests
import pytube

url = str(input('Playlist link: '))

response = requests.get(url)
cont = BeautifulSoup(response.text, 'html.parser')
body = cont.body
videos = body.findAll('tr', {'class':'pl-video yt-uix-tile '})
channels = body.findAll('a', {'class':' yt-uix-sessionlink spf-link '})

print('''
Index:         Channel:        Title:''')

for i, video in enumerate(videos):
	title = str(video['data-title'])
	path = str(video['data-video-id'])
	
	channel = str(channels[i].text)	
		
	link = f'https://www.youtube.com/watch?v={path}'
	
	print(f'''
     {i+1}          {channel}       {title}
 	''')	

	yt = pytube.YouTube(link)
	stream = yt.streams.first()
	stream.download()

