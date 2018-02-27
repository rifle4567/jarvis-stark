# importing the module
import tweepy

# personal details
consumer_key ="9ZWamnb3RIGHfi0SRHiqt0rdV"
consumer_secret ="TyL6FGS1qMTXVl2HVSvwo2UV8KKltoourULqelkHmqP65zCGne"
access_token ="966206559264047105-0WzEo91idKS5vQwZL8c2Mju2CS9b473"
access_token_secret ="STQ9Llse4PtwRTLDF2cf1BXBUGW0bjHrmMFLjlltwIL4H"

# authentication of consumer key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# authentication of access token and secret
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# update the status
api.update_status(status ="lionel messi !")
