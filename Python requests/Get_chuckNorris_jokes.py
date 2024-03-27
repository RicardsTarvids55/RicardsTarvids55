import requests

res = requests.get("https://api.chucknorris.io/jokes/SUluEumSSWqDibkGiJ-VUA")
joke = res.json()
print(joke['value'])
#['value'] is used to only see the joke and nothing else when its printed 