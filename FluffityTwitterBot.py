import tweepy
import time


auth = tweepy.OAuthHandler('qFudgczsY7yKamnErdX4HsVxA',
                           'TsBZhhdLgLUTEUjyWCiaJ5ueBGtweyVGV5GFwMfix9qpLcbWhN')
auth.set_access_token('1613718392-ji00fZ7L30fCVTyuUDc9ItKPLMfV6s6w5jTVkPJ',
                      '10xt3nlLZ9l6ThYFnXx1yWoDxOdSty9QBtRKe5kyldpSZ')

api = tweepy.API(auth)
user = api.me()


# Twitter has a rate limit to limit the number of times u hit the server in a small window of time,
# so that it costs them less money and so servers don't crash. this function is to handle that
def limit_handler(cursor):
    while True:
        try:
            yield cursor.next()
        # if we surpass the rate limit and get a RateLimitError:
        except tweepy.RateLimitError:
            # stops the program for 300 milliseconds (0.3 seconds)
            time.sleep(300)


# follow back (by looping through followers)
# loop through all your followers
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    # .Cursor passes through all pages of sth, ex followers page 1, 2, 3, etc
    # or also timeline pages bc it doesn't fit in only one page
    # api.followers grabs all the followers
    # .items() turns them into items so that u can loop through them
    if follower.name == 'Usernamehere':
        print(follower.name)
        follower.follow()  # follow this person


search_string = "zerotomastery"
numberOfTweets = 2

# like a tweet containing the word saved in search_string
# api.search searches for
for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
    # tweets that match a specified query
    # and only the number of tweets u say
    try:
        tweet.favorite()  # like (favorite) the tweet
        print('Liked the tweet')
    except tweepy.TweepError as e:  # TweepError is for tweepy errors and twitter errors
        print(e.reason)  # print the reason of the error
    except StopIteration:  # if the iterable ends
        break
