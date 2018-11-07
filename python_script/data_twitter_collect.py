import tweepy
import twitter_credentials
import sys
import time

class TwitterClient():
           def __init__(self):
                      self.api=tweepy.API(TwitterAuthenticator().authenticate_twitter_app())
           def get_api(self):
                      return self.api


class TwitterAuthenticator():
           """
         This method differs from GET oauth / authorize in that if the user has already granted the application permission,
        the redirect will occur without the user having to re-approve the application.

        .. warning:: user twitter_credentials are request
        .. todo:: you must fill your account in the twitter_credentials.py file account
            """
           def authenticate_twitter_app(self):
                      """
                         
                              The next step is creating an OAuthHandler instance.
                              This tries to make OAuth. To begin the process we need to register our client application with Twitter.
                              Create a new application and once you are done you should have your consumer token and secret. Keep these two handy, you’ll need them.
                              
                       
                              :return: return authenticate of twitter
                              :Example:
                              >>> TwitterAuthenticator().authenticate_twitter_app()
 
                      """
                      auth = tweepy.OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
                      auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
                      return auth




class TweetExtract():
           def __init__(self,times=None,q="israel"):
                      '''

                              :param a: The time that the program must to work in seconde
                              :param b: the items of tweet search
                              :type a: int
                              :type b: str
                              :Example:
                       
                              >>> TweetExtract(5,'instagood')
                      '''
                      self.times=times
                      self.q=q
                      self.hasthtag=[]
                      self.totaltweet=0 #verifier si jai bien compris
                      self.api=TwitterClient().get_api()

           def get_hasthtags(self):
                      """
                              The Twitter streaming API is used to download twitter messages in real time. It is useful for obtaining a high volume
                              of tweets, or for creating a live feed using a site stream or user stream. See the Twitter Streaming API Documentation.
                              The streaming api is quite different from the REST api because the REST api is used to pull data from twitter but the
                              streaming api pushes messages to a persistent session. This allows the streaming api to download more data in real
                              time than could be done using the REST API.
                       
                              :return: dictionnaire with the count of tweet he has checked and all hashtag is check
                              :rtype: dict
                       
                              :Example:
                       
                              >>> TweetExtract().get_hasthtags()
                              
                       
                              .. seealso:: TweetExtract(),TwitterAuthenticator(),TwitterClient()
                      """
                      print('Start Time:  '+time.strftime("%H:%M:%S"))
                      if self.times:
                                 end = time.time()+self.times
                                 while time.time()<end:
                                            new_tweets=tweepy.Cursor(self.api.search,q=self.q, count = 243, result_type = "recent").items(243)
                                            for tweets in new_tweets:
                                                       self.totaltweet+=1
                                                       for hasthtags in tweets.entities['hashtags']:
                                                                  self.hasthtag.append(hasthtags['text'])
                      else:
                                 new_tweets=tweepy.Cursor(self.api.search,q=self.q, count = 200, result_type = "recent").items(200)
                                 for tweets in new_tweets:
                                            self.totaltweet+=1
                                            for hasthtags in tweets.entities['hashtags']:
                                                       self.hasthtag.append(hasthtags['text'])
                      print('End Time:  '+time.strftime("%H:%M:%S"))

                      return {'count_tweet':self.totaltweet,'hasthtag':self.hasthtag}
                                            
