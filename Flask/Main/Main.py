from flask import Flask, render_template, jsonify
from bs4 import BeautifulSoup
import requests
import os

app = Flask(__name__)

def get_delfi_headlines():
    url = 'https://www.delfi.lv'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    headlines = soup.find_all(class_='headline')
    headlines_list = [headline.text.strip() for headline in headlines]
    return headlines_list

def get_news(country, api_key):  
    url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        news_data = response.json()
        articles = news_data.get('articles', [])
        results = []
        for article in articles:
            news_item = {
                'title': article.get('title', 'N/A'),
                'publishedAt': article.get('publishedAt', 'N/A'),
                'url': article.get('url', '#')
            }
            results.append(news_item)
        return results
    else:
        return None


@app.route('/')
def home():
    headlines = get_delfi_headlines()
    api_key = "133792de3d5e436fa582dbbf43dee274"
    news = get_news('us', api_key)  
    if news is None:
        news = "Failed to fetch news."
    return render_template('home.html', headlines=headlines, news=news)

@app.route('/APInews/')
def news():
    api_key = "133792de3d5e436fa582dbbf43dee274" 
    news = get_news('us', api_key)
    if news is None:
        news = "Failed to fetch news."
    return render_template('news.html', news=news)

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/socials/')
def socials():
    return render_template('socials.html')

@app.route('/info/')
def index():
    headlines = get_delfi_headlines()
    return render_template('info.html', headlines=headlines)

if __name__ == '__main__':
    app.run(debug=True)