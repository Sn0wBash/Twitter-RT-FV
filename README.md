# Twitter-RT-FV

Written for Python3
This is a bot for Twitter using the Tweepy library, which will need installing before use. It will ReTweet and FaVourite items from the relevant lists and will wait a random amount of time between actions.
RT_List & FV_List should be modified with whatever search terms you wish to use. The lists can be as short or as long as you like and list entries will be selected randomly. If you requier a heavier weighting for certain elements include them multiple times accordingly.
Wait time can be configured with the min_time and max_time variables, units are in seconds and setting these to the same amount will remove the random element.
The keys.py file should be modified with account keys, available at https://apps.twitter.com/
FV_bot.py will function exactly the same but will only favourite.
unfollow.py will unfollow anyone who is not following you.
