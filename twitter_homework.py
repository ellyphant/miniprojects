"""
This is my first mini project to get familiar with querying
public API's, in this case, Twitter.
"""
import twitter
import config

# Were using a twitter api python wrapper that requires a few keys that
# we received after registering an app with twitter
API = twitter.Api(\
    consumer_key=config.CONSUMER_KEY,
    consumer_secret=config.CONSUMER_SECRET,
    access_token_key=config.ACCESS_TOKEN_KEY,
    access_token_secret=config.ACCESS_TOKEN_SECRET)

def tentweets(search_term):
    """ Returns the most recent ten tweets with the searched term."""
    # This GetSearch call will return 10 tweets that contain our input
    search = API.GetSearch(term=search_term, count=10)

    if len(search) < 10:
        raise Exception('There are less than 10 tweets for this search.')

    # Next, we will extract the .text value from each tweet and append it
    # into our list_of_tweets
    list_of_tweets = [x.text for x in search]
    return list_of_tweets

if __name__ == '__main__':
    print tentweets('#berkeley')

