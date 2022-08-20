# Akhbaar padhke sunaao
'''from win32com.client import Dispatch
   speak = Dispatch("SAPI.SpVoice")
   speak.Speak("hello World")
 my api key is  083d48b8f4d04be9912a545ae165aa44
 '''
# --------------------------------------Main Program-------------------------------------------------------------------
import requests
import json
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    speak("News For Today")
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=083d48b8f4d04be9912a545ae165aa44"
    news = requests.get(url).text
    news_dict = json.loads(news)
    print(news_dict['articles'])
    arts = news_dict['articles']
    for articles in arts:
        speak(articles['title'])
        speak("Moving to the next news... Listen carefully ")
    speak("Thanks for listening")
