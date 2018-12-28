import tweepy

auth = tweepy.OAuthHandler('46pvnSwIVylfWepbPsP4433wL', 'xWDPHaUkk0ub93qj1DaYgJcO8QtkPUhNFIE7uBAvzbSVLLpLzR')
auth.set_access_token('1952916806-9WbU9ROPLd4aVPprQZqWJhaW4RSXrBw4oK8A4Ow','gW5iuYPtrTxVhPmQxBemsKz6jCAOqbYx1fT0ewKHFyAkG')
api = tweepy.API(auth)

def obter_tweets(usuario, limite):
	resultados = api.user_timeline(screen_name=usuario, count=limite)
	tweets = []
	for r in resultados:
		tweets.append(r.text)
	return tweets

tweets = obter_tweets('thiagoreisd',100)
with open('tweets.txt', 'w') as f:
	f.write('\n\n\n'.join(tweets))
