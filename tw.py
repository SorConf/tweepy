import tweepy
import requests
import json

class qiitaHttpRequest:
    def __init__(self):
        self.__url = "https://qiita.com/api/v2/items?page=1&per_page=5&query=tag%3Apython+or+tag%3Aphp+or+tag%3Aruby+or+tag%3Ahtml+or+tag%3Acss+or+tag%3ALinux+or+tag%3AGitLaby"
        self.__httprequest = requests.get(self.__url)
        self.__dataList = json.loads(self.__httprequest.text)
    def data(self):
        return(self.__dataList)

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
qiitaApi = qiitaHttpRequest()

for response in qiitaApi.data():
    OAuth.api().update_status(str(response["title"]) + str("　") + str(response["url"]))