import requests
from .views import fetch_news

def news_widget(request):
    latest_news = fetch_news()
    return {'latest_news': latest_news}
