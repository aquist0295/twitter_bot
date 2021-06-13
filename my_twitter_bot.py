import tweepy

print('this is my twitter bot')

CONSUMER_KEY = 'pcF21vdtQOCgJijNZzHIuERGe'
CONSUMER_SECRET = 'OKIxIoPmwzsfcYh2HWSYdTvt6eH4tlGCk5nriAjnI4Ne3hQGuW'
ACCESS_KEY = '191992412-MiAW0JI4mM8cgF4qW9brX3sZKqFbhaIADtwkKW6h'
ACCESS_SECRET = 'FjUrzW352SyAPrct5BuLHaXKDkMXtiP3Yr39YeQpVze4w'


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token (ACCESS_KEY,  ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'
mentions = api.mentions_timeline()

def retrieve_last_id(file_name):
   f_read= open(file_name, 'r')
   last_seen_id = int(f_read.read().strip())
   f_read.close()
   return last_seen_id


def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

# first id tweet 238743839697948673
last_seen_id = retrieve_last_id(FILE_NAME)

mentions = api.mentions_timeline(
    last_seen_id,
    tweet_mode = 'extended')

for mention in reversed(mentions):
    print(str(mention.id) + ' - ' + mention.full_text)
    last_seen_id = mention.id
    store_last_seen_id(last_seen_id, FILE_NAME)
    if '#helloworld' in mention.full_text.lower():
     print ('found #helloworld!')
     print ('Responding back.....') 
     api.update_status('@' + mention.user.screen_name + '#Hellworld back to you, testing reply for', mention.id)

