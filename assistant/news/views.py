from django.shortcuts import render, redirect
import requests
from django.conf import settings
# from .models import News, Topic

import json


# Create your views here.
def main(request):
    return render(request, "news/index.html", {})


def get_news(category='general'):
    url = 'https://newsapi.org/v2/top-headlines'
    parameters = {
        'country': 'us',
        'category': category,
        'apiKey': settings.NEWSAPI_KEY,
    }
    response = requests.get(url, params=parameters)
    data = response.json()
    return data['articles']

def news_list(request):
    news_data = get_news()
    context = {
        'news': news_data
    }
    return render(request, 'news/news_list.html', context)

def fetch_news():
    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=" + settings.NEWSAPI_KEY
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('articles', [])[:5]  # обмежуємо кількість новин до 5
    return []



# def create_topics_news():

#     Topic.objects.all().delete()
#     News.objects.all().delete()

#     # news_data = articles_scraped

#     with open("./data.json", "r", encoding="utf-8") as fl:

#         topic_news = json.load(fl)

#     for key, value in topic_news:
#         Topic.objects.create(
#             name = key
#         )
#         topic_id, data = Topic.objects.get_or_create(name=key)
#         for el in value:
#             News.objects.create(
#                 title = el['title'],
#                 description =el['content'],
#                 url = el['url'],
#                 published_at = el['date'],
#                 topic = topic_id
#                 )

    # return redirect(to="news:news_ua")


def news_list_ua_for_topic(topic: str):
    news_list = []
    with open("./data.json", "r", encoding="utf-8") as fl:

       list_news = json.load(fl)
    for el in list_news:
        context = {
        'news': list_news[topic]
    }
    return context

def news_list_ua_main(request):
    context = news_list_ua_for_topic(topic="main")
    return render(request, 'news/news_ua.html', context)

def news_list_ua_war(request):
    context = news_list_ua_for_topic("war")
    return render(request, 'news/news_ua.html', context)

def news_list_ua_society(request):
    context = news_list_ua_for_topic(topic="society")
    return render(request, 'news/news_ua.html', context) 

def news_list_ua_world(request):
    context = news_list_ua_for_topic(topic="world")
    return render(request, 'news/news_ua.html', context)  

def news_list_ua_economics(request):
    context = news_list_ua_for_topic(topic="economics")
    return render(request, 'news/news_ua.html', context)

def news_list_ua_science(request):
    context = news_list_ua_for_topic(topic="science")
    return render(request, 'news/news_ua.html', context)

def news_list_ua_sport(request):
    context = news_list_ua_for_topic(topic="sport")
    return render(request, 'news/news_ua.html', context)    

def detail(request):
    pass

# <h2>News List</h2>

# <ul>
#     {% for item in news %}
#     <li>
#         <strong><a href="{{ item.url }}" target="_blank">{{ item.title }}</a></strong>
#         <p>{{ item.description }}</p>
#         <small>Published at: {{ item.published_at}}</small>
#     </li>
#     {% endfor %}
# </ul>
