import requests
from bs4 import BeautifulSoup
import time
import json


def scrap_article(url: str):
    article_scrap = {}
    article_text = ""
    response = requests.get(url)
    soup = BeautifulSoup(response.text)

    if response.status_code == 200:
      
        # time.sleep(1)
        time_published = soup.find('div', attrs={'class': "article__info-item time"}).text
        date_published = time_published.split(' ')[1]
        # time.sleep(1)
        text_article = soup.find_all('div', attrs={'class': "article"})
        for n in text_article:
            article = reversed(n.find_all('p'))
            for el in article:
                article_text += el.text
        article_scrap = {'content': article_text, 'date': date_published}

    return article_scrap

def parse_news_ua(url: str, attr: str, limit = 5):
    list_news = []
    news_dict = {}
    response = requests.get(url)
    soup = BeautifulSoup(response.text)

    if response.status_code == 200:
        # time.sleep(1)
        all_news = soup.find_all('a', attrs={'class': attr}, limit=limit)
        # time.sleep(1)

        for n in all_news:
            title_news = f"{n.find('img')['alt']}"
            url_news = n['href']
            article = scrap_article(url_news)
            description = article['content']
            date = article['date']
            news_dict = {'title': title_news,
                         'content': description,
                         'date': date,
                         'url': url_news
                         }
            list_news.append(news_dict)

    return list_news

def articles_scraped():
    articles= {}
    open("data.json","w").close()

    list_topic_news = ['', 'war', 'science', 'world', 'society', 'economics', 'sport']
    class1_topics = ['economics', 'sport']
    class2_topics = ['war', 'science', 'world', 'society']

    for topic in list_topic_news:
        if topic in class1_topics:
            attr_a = 'list-news__image'
        elif topic in class2_topics:
            attr_a = 'list-thumbs__image'
        else:
            attr_a = 'list-news__image psr'
        url = 'https://www.unian.ua/' + topic
        if topic=='':
             topic="main"
        # print(url)
        data_list = parse_news_ua(url, attr_a)
        json_obj = {topic: data_list}
        articles[topic] = data_list
        # list = 
        with open('data.json', 'a', encoding='utf-8') as f:
            json.dump(json_obj, f, ensure_ascii=False)

def articles_scraped1():    
    all_data = {}
    list_topic_news = ['', 'war', 'science', 'world', 'society', 'economics', 'sport']
    class1_topics = ['economics', 'sport']    
    class2_topics = ['war', 'science', 'world', 'society']
    for topic in list_topic_news:
        if topic in class1_topics:
                    attr_a = 'list-news__image'
        elif topic in class2_topics:
                    attr_a = 'list-thumbs__image'
        else:            
                    attr_a = 'list-news__image psr'
        url = 'https://www.unian.ua/' + topic
        if topic == '':
            topic = "main"        
        # Save data to the dictionary        
        all_data[topic] = parse_news_ua(url, attr_a)
        # print(all_data)
        print('***')
    # Write the data to the file after the loop
    with open('data.json', 'w', encoding='utf-8') as f:
        
        json.dump(all_data, f, ensure_ascii=False)
        
    return all_data

if __name__ == "__main__":
    articles_scraped1()
  





    
    
