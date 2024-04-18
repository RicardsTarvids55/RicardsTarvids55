from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

def get_delfi_headlines():
    url = 'https://www.delfi.lv/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    headlines = soup.find_all(class_='headline')
    headlines_list = [headline.text.strip() for headline in headlines]
    return headlines_list

@app.route('/')
def home():
    return render_template('home.html')

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