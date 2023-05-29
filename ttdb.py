import tweepy
import matplotlib.pyplot as plt


consumer_key = "SUA_CONSUMER_KEY"
consumer_secret = "SUA_CONSUMER_SECRET"
access_token = "SEU_ACCESS_TOKEN"
access_token_secret = "SEU_ACCESS_TOKEN_SECRET"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth)


keyword = "python"
tweets = api.search(q=keyword, count=100)


retweets_count = [tweet.retweet_count for tweet in tweets]


plt.bar(range(len(retweets_count)), retweets_count)
plt.xlabel("Tweets")
plt.ylabel("Contagem de Retweets")
plt.title(f"Tweets com a palavra-chave '{keyword}'")
plt.show()
