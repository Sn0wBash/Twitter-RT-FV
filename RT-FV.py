import tweepy
from random import randint
from time import sleep
from keys import *

#List of search terms for Retweets.
RT_List = ["#DnB", "#DrumAndBass", "#DnB", "#DrumAndBass", "#linux", "#python"]

#List of  search terms for Favourits.
FV_List = ["#linux", "#python", "#DnB", "#DrumAndBass"]

#Set the minimum wait time in seconds, too low could result in a ban.
min_time = 1500 #25 minuets

#Set the maximum wait time in seconds, must be equal to or higher than min_time
max_time = 2100 #35 minuets

#Twitter authentication
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#Lists to customise the rt_fv() function
RT = [RT_List, 0, "Reetweeted"]
FV = [FV_List, 1, "Favorited"]

def rt_fv(a):                                   #Retweet & Favourite function
    roll = randint(0, len(a[0]) - 1)            #Determine a random list element
    try:
        for tweet in tweepy.Cursor(api.search_tweets, q=a[0][roll], lang="en").items(1):
            print("\n%s Tweet by: @" % a[0][roll] + tweet.user.screen_name)
            if a[1] == 0:                       #Retweet
                tweet.retweet()
            elif a[1] == 1:                     #Favorite
                tweet.favorite()
            print("%s the tweet" % a[2])
            if not tweet.user.following:        #If we don't follow the user
                tweet.user.follow()             #Follow the user
                print("Followed the user")
    except tweepy.errors.TweepError as e:       #Check for an error
        print(e.reason)
    sleep(randint(min_time, max_time))          #Sleep for random amount of time

def run():                                      #Looping function
    while (1):                                  #Keep the loop running
        rt_fv(RT)                               #Run function with Retweet List
        rt_fv(FV)                               #Run function with Retweet List
run()                                           #Start the loop
