import requests

r = requests.get('https://tukums2.lv/abc')
#response 404 = 'https://tukums2.lv/abc'
#responce 200 = 'https://tukums2.lv'
print(r)