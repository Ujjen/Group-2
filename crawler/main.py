import requests
from key import API_KEY
#import pyttsx3
from Article import *
import os

response = requests.Session()

# take user input for the news
user = input("Search Any News: ")
URL = "https://newsapi.org/v2/everything?q=" + user +"&apiKey=" + API_KEY
result = response.get(URL)

# extract json from the url
result_json = result.json()
articles = result_json["articles"]

articleObjs = []        # article objects
for article in articles:
    atcl = Article("", "", "")
    atcl.setSource(article["source"]['name'])
    atcl.setTitle(article["title"])
    print(atcl.getTitle())
    atcl.setDate(article["publishedAt"])
    articleObjs.append(atcl)



# set pyttsx3 engine to speak
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
# method to speak the news
def speak(article):


    text = article.getTitle()
    os.system("say" + text)
    #engine.say(text)
    #engine.runAndWait()

for article in articleObjs:
    speak(article)
