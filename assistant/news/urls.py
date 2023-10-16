from django.urls import path

from . import views

app_name = "news"

urlpatterns = [
    path("", views.main, name="root"),
    path("news/", views.news_list, name="news_list"),
    path("news_ua/", views.news_list_ua_main, name="news_ua"),
    path("news_ua/", views.detail, name="detail_news"),
    path("news_ua/", views.news_list_ua_war, name="war"),
    path("news_ua/", views.news_list_ua_society, name="society"),
    path("news_ua/", views.news_list_ua_world, name="world"),
    path("news_ua/", views.news_list_ua_science, name="science"),
    path("news_ua/", views.news_list_ua_economics, name="economics"),
    path("news_ua/sport", views.news_list_ua_sport, name="sport"),

]