from flask import Flask, render_template, jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

def get_delfi_headlines():
    url = 'https://www.delfi.lv'
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

@app.route('/api/headlines')
def get_headlines():
    headlines = get_delfi_headlines()
    return render_template('headlines.html', title='API Headlines', heading='API Headlines', content=[f'<li>{headline}</li>' for headline in headlines])

@app.route('/export_headlines')
def export_headlines():
    url = 'https://www.delfi.lv/laika-zinas'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        headlines = soup.find_all('span', class_='d-inline')
        headlines_list = [headline.text.strip() for headline in headlines]
        return render_template('headlines.html', title='Exported Headlines', heading='Exported Headlines', content=[f'<li>{headline}</li>' for headline in headlines_list])
    else:
        return f'Error: Unable to fetch data from {url}'

@app.route('/headlines_api')
def headlines_api():
    headlines = get_delfi_headlines()
    return render_template('headlines.html', title='API Headlines', heading='API Headlines', content=[f'<li>{headline}</li>' for headline in headlines])

@app.route('/headlines_export')
def headlines_export():
    url = 'https://www.delfi.lv/laika-zinas'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        headlines = soup.find_all('span', class_='d-inline')
        headlines_list = [headline.text.strip() for headline in headlines]
        return render_template('headlines.html', title='Exported Headlines', heading='Exported Headlines', content=[f'<li>{headline}</li>' for headline in headlines_list])
    else:
        return f'Error: Unable to fetch data from {url}'

if __name__ == '__main__':
    app.run(debug=True)