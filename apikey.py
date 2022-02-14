import tweepy

# APIkey
apiKey = ''
apiSecretKey = ''
accessToken = ''
accessTokenSecret = ''
# OAuth authentication settings
auth = tweepy.OAuthHandler(apiKey, apiSecretKey)
auth.set_access_token(accessToken, accessTokenSecret)

api = tweepy.API(auth)

class authTwitter:
    def __init__(self):
        self.__accessToken = ''
        self.__accessTokenSecret = ''
        self.__apiKey = ''
        self.__apiSecretKey = ''
        self.__auth = tweepy.OAuthHandler(self.__apiKey, self.__apiSecretKey)
        self.__auth.set_access_token(self.__accessToken, self.__accessTokenSecret)
        self.__api = tweepy.API(self.__auth)
    def api(self):
        return(self.__api)
    def auth(self):
        return(self.__auth)

OAuth = authTwitter()

