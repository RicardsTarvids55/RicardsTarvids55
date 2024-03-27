from bs4 import BeautifulSoup
import requests

url = "https://www.delfi.lv/"

responce = requests.get(url)

soup = BeautifulSoup(responce.text, 'html.parser')

title = soup.find("title")

print(title.text)

print(responce)